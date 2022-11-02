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

    # retrieves the data needed to generate a dictionary for the categories dropdown on home.html
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# using function for this since retrieving the request is simpler for the function than a class
def CategoryView(req, cats):
    # db query for categories to store
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(req, 'categories.html', {'cats': cats.replace('-', ' '),
                                           'category_posts': category_posts})
def CategoryListView(req):
    # db query for categories to store
    category_menu_list = Category.objects.all()
    return render(req, 'category_list.html', {'category_menu_list': category_menu_list})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    # retrieves the data needed to generate a dictionary for the categories dropdown on home.html
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


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
