from django.urls import path

from .views import UserRegisterView, UserEditView

# Using class based url
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
