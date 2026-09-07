from django.shortcuts import get_object_or_404, redirect, render
from users.forms import UserCreateForm
from users.forms import UserUpdateForm
from users.models import User

# Create your views here.

def user_list(request):
   users = User.objects.all()
   return render(request, 'users/user_list.html', {'users': users})

def user_view(request, pk):
   user = get_object_or_404(User, pk = pk)
   return render(request, 'users/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
           user = form.save()
        return redirect('user_list')
    else:
       form = UserCreateForm()
    return render(request, 'users/user_create.html', {
      'form': form
    })

def user_edit(request, pk):
    user = get_object_or_404(User, pk = pk)
    if request.method == 'POST':
      form = UserUpdateForm(request.POST, instance=user)
      if form.is_valid():
         form.save()
      return redirect('user_list')
    else:
      form = UserUpdateForm(instance=user)
    return render(request, 'users/user_create.html', {
       'form': form,
       'user': user
    })

def user_delete(request, pk):
   user = get_object_or_404(User, pk = pk)
   user.delete()
   return redirect('user_list')