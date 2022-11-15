from django import forms

from .models import Post, Category, Comment

# Retrieves key-value pair
choices = Category.objects.all().values_list('name', 'name')
# Creating empty list for the categories to be stored in
choice_list = []
# Pushing each Category into our Python List to send back to the client
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'input is-info'
            }
        )
    )

    title_tag = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': 'Sub title/Snippet',
                'class': 'input is-info'
            }
        )
    )

    category = forms.ChoiceField(
        required=True,
        choices=choice_list,
        widget=forms.widgets.Select(
            attrs={
                'class': 'select is-info'
            }
        )
    )

    header_image = forms.ImageField(
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
                'class': 'textarea is-info',
                'placeholder': 'Blog entry...'
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'header_image', 'body')


class UpdateForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
            }
        )
    )

    title_tag = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
            }
        )
    )

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea is-info',
            }
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')


class CommentForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'input is-info'
            }
        )
    )

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'textarea is-info'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('name', 'body')
