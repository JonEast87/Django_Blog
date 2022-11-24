from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import UserRegisterView, UserEditSettingsView, PasswordsChangeView, ShowProfilePageView, \
    EditProfilePageView, CreateProfilePageView

# Using class based url
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserEditSettingsView.as_view(), name='edit_settings'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
