from django.core.exceptions import PermissionDenied

from JonsBlog.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView

from .forms import SignupForm, PasswordUpdateForm, EditSettingsForm, EditProfileForm, \
    CreateProfileForm


class CreateProfilePageView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    form_class = CreateProfileForm

    # Backend authentication to ensure user is logged to access page
    login_url = None
    permission_denied = ''
    raise_exception = False
    redirect_field_name = 'next'

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
        context['page_user'] = page_user
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


class UserEditSettingsView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        raise PermissionDenied()


class EditProfilePageView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        raise PermissionDenied()

    success_url = reverse_lazy('home')
