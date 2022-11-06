from django.urls import path

from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, \
    EditProfilePageView

# Using class based url
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserEditView.as_view(), name='edit_settings'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile"),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name="edit_profile"),
]
