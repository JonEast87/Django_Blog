from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import SignupForm, EditProfileForm, PasswordUpdateForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
