from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .decorators import SESSION_USER_ID_KEY, login_required_custom
from .forms import LoginForm, UserCreateForm, UserUpdateForm
from .models import User


# ---------------------------------------------------------------------------
# Autenticación (login / logout / registro)
# ---------------------------------------------------------------------------
def register_view(request):
    """Alta pública de un usuario nuevo (también reutilizable como 'Create' del CRUD)."""
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuario "{user.full_name}" creado correctamente. Ahora inicia sesión.')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Crear cuenta',
        'is_create': True,
    })


def login_view(request):
    """
    Login manual: busca el usuario por email, y valida la contraseña
    recalculando el hash PBKDF2 con el salt guardado (User.check_password).
    """
    if request.session.get(SESSION_USER_ID_KEY):
        return redirect('user_list')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower().strip()
            raw_password = form.cleaned_data['password']
            try:
                user = User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                user = None

            if user is None or not user.check_password(raw_password):
                messages.error(request, 'Correo o contraseña incorrectos.')
            elif not user.is_active:
                messages.error(request, 'Esta cuenta está inactiva. Contacta al administrador.')
            else:
                request.session[SESSION_USER_ID_KEY] = user.pk
                messages.success(request, f'Bienvenido, {user.first_name}.')
                next_url = request.GET.get('next') or reverse('user_list')
                return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    request.session.pop(SESSION_USER_ID_KEY, None)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')


# ---------------------------------------------------------------------------
# CRUD de usuarios (protegido por sesión)
# ---------------------------------------------------------------------------
@login_required_custom
def user_list(request):
    query = request.GET.get('q', '').strip()
    users = User.objects.all()
    if query:
        users = users.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )
    return render(request, 'users/user_list.html', {'users': users, 'query': query})


@login_required_custom
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user_obj': user})


@login_required_custom
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuario "{user.full_name}" creado correctamente.')
            return redirect('user_list')
    else:
        form = UserCreateForm()
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Nuevo usuario',
        'is_create': True,
    })


@login_required_custom
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario "{user.full_name}" actualizado correctamente.')
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': f'Editar usuario: {user.full_name}',
        'is_create': False,
        'user_obj': user,
    })


@login_required_custom
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        full_name = user.full_name
        user.delete()
        messages.success(request, f'Usuario "{full_name}" eliminado correctamente.')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user_obj': user})
