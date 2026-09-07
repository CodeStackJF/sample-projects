from django.urls import path

from . import views

urlpatterns = [
    # Autenticación
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # CRUD de usuarios
    path('users/', views.user_list, name='user_list'),
    path('users/nuevo/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/editar/', views.user_update, name='user_update'),
    path('users/<int:pk>/eliminar/', views.user_delete, name='user_delete'),
]
