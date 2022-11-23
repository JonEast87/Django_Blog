from JonsBlog.models import Profile
from django import forms
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'input'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input is-info'})
        self.fields['password1'].widget.attrs.update({'class': 'input is-info'})
        self.fields['password2'].widget.attrs.update({'class': 'input is-info'})


class CreateProfileForm(forms.ModelForm):
    bio = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': 'Bio entry, max of 255 characters...'
            }
        )
    )

    profile_image = CloudinaryFileField(
        required=True,
        widget=forms.widgets.FileInput(
            attrs={
                'class': 'file-input',
                'type': 'file',
            }
        )
    )

    github = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    instagram = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    linkedin = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    twitter = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'github', 'instagram', 'linkedin', 'twitter')


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea',
            }
        )
    )

    github = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    instagram = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    linkedin = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    twitter = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'github', 'instagram', 'linkedin', 'twitter')


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'input',
                'type': 'email'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'type': 'password'
            }
        )
    )

    new_password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'type': 'password'
            }
        )
    )

    new_password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'type': 'password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
