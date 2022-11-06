from JonsBlog.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class EditProfileForm(UserChangeForm):
    bio = forms.Textarea(attrs={'class': 'form-control'})
    # profile_image = forms.ImageField(widget=forms.ImageField(attrs={'class': 'form-control'}))
    github = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    instagram = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    linkedin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    twitter = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['bio', 'github', 'instagram', 'linkedin', 'twitter']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})
        # self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['github'].widget.attrs.update({'class': 'form-control'})
        self.fields['instagram'].widget.attrs.update({'class': 'form-control'})
        self.fields['linkedin'].widget.attrs.update({'class': 'form-control'})
        self.fields['twitter'].widget.attrs.update({'class': 'form-control'})


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={
    #     'class': 'form-check'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={
    #     'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
