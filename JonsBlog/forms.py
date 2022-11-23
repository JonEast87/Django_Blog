from django import forms

from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    # # Retrieves key-value pair
    # choices = Category.objects.all().values_list('name', 'name')
    # # Creating empty list for the categories to be stored in
    # choice_list = []
    # # Pushing each Category into our Python List to send back to the client
    # for item in choices:
    #     choice_list.append(item)

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
        fields = ('title', 'title_tag', 'body')


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
