from JonsBlog.models import Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    #
    # username = forms.CharField(
    #     required=True,
    #     widget=forms.widgets.TextInput(
    #         attrs={
    #             'class': 'input is-info',
    #             'type': 'text',
    #         }
    #     )
    # )
    #
    # password = forms.CharField(
    #     required=True,
    #     widget=forms.widgets.TextInput(
    #         attrs={
    #             'class': 'input is-info',
    #             'type': 'password',
    #         }
    #     )
    # )

    class Meta:
        model = User
        # fields = ('username', 'password')

    def __int__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input is-info'})
        self.fields['password'].widget.attrs.update({'class': 'input is-info'})


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input is-info'}))

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'input is-info'}))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'input is-info'}))

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
                'class': 'textarea is-info',
                'placeholder': 'Bio entry, max of 255 characters...'
            }
        )
    )

    profile_image = forms.ImageField(
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
                'class': 'input is-info'
            }
        )
    )

    instagram = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
            }
        )
    )

    linkedin = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
            }
        )
    )

    twitter = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
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
                'class': 'textarea is-success',
            }
        )
    )

    github = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

    instagram = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

    linkedin = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

    twitter = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-success'
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
                'class': 'input is-success',
                'type': 'email'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input is-success'
            }
        )
    )

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
