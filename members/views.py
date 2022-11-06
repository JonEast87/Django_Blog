from JonsBlog.models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView

from .forms import SignupForm, PasswordUpdateForm, EditSettingsForm, EditProfileForm, \
    CreateProfileForm


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_user_profile.html"
    form_class = CreateProfileForm

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


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


class UserEditSettingsView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class EditProfilePageView(generic.UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = 'registration/edit_profile.html'
    # fields = ['bio', 'profile_image', 'github', 'instagram', 'linkedin', 'twitter']
    success_url = reverse_lazy('home')
