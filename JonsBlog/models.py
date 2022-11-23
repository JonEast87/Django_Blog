from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = CloudinaryField(null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, default="Jon's Blog")
    header_image = CloudinaryField(null=True, blank=True)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    publication_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="general")
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])


class Comment(models.Model):
    profile = models.ForeignKey(Profile, related_name='user_comment', on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = models.TextField(max_length=240)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
