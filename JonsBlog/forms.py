from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'input',
            }
        )
    )

    title_tag = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': 'Sub title/Snippet',
                'class': 'input',
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'),
        required=True,
        widget=forms.widgets.Select(
            attrs={
                'class': 'select',
            }
        )
    )

    header_image = CloudinaryFileField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                'class': 'file-input',
                'type': 'file',
            }
        )
    )

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': 'Blog entry...',
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'header_image', 'body')


class AddCategory(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input'
            }
        )
    )

    class Meta:
        model = Category
        fields = ('name',)


class UpdateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input',
            }
        )
    )

    title_tag = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input',
            }
        )
    )

    header_image = CloudinaryFileField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                'class': 'file-input',
                'type': 'file',
            }
        )
    )

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea',
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'body')


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': 'Comment entry (max of 240 characters)...'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('body',)
