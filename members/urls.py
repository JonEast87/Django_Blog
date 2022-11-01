from django.urls import path
from .views import UserRegisterView


# Using class based url
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
