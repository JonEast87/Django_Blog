from django.urls import path

from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView

# Using class based url
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
]
