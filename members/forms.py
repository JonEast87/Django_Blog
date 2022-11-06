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


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'github', 'instagram', 'linkedin', 'twitter')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control', }),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'github', 'instagram', 'linkedin', 'twitter')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control', }),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

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
