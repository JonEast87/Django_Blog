from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy


# Utilizing Python classes to make the views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_time']


# using function for this since retrieving the request is simpler for the function than a class
def CategoryView(req, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(req, 'categories.html', {'cats': cats, 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    fields = '__all__'
    model = Category
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
