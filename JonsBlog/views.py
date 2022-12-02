from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, UpdateForm, CommentForm, AddCategory
from .models import Post, Category


# Utilizing Python classes to make the views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_date', '-publication_time']

    # retrieves the data needed to generate a dictionary for the categories dropdown on home.html
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        # grabs posts from post_table and assign the returned data to get_likes
        # get_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        # total_likes = get_likes.total_likes()

        context["cat_menu"] = cat_menu
        # context["total_likes"] = total_likes
        return context


def like_view(req, pk):
    # This creates a form and submits the post id to find the matching post id
    # if found it saves it to the table, if not it returns a 404 error
    post = get_object_or_404(Post, id=req.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=req.user.id).exists():
        post.likes.remove(req.user)
        liked = False
    else:
        post.likes.add(req.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


# using function for this since retrieving the request is simpler for the function than a class
def category_view(req, cats):
    # db query for categories to store
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(req, 'categories.html', {'cats': cats.replace('-', ' '),
                                           'category_posts': category_posts})


def category_life_view(req):
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

        # grabs posts from post_table and assign the returned data to get_likes
        get_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_likes.total_likes()

        liked = False
        if get_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'add_post.html'

    # Test to check if user is_superuser, if not then display a 403,
    # this will remain in place until I can decide on if I want anyone posting
    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'add_comment.html'

    # Backend authentication to ensure user is logged to access page
    login_url = None
    permission_denied = ''
    raise_exception = False
    redirect_field_name = 'next'

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = AddCategory
    template_name = 'add_category.html'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        raise PermissionDenied()


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        raise PermissionDenied()

    success_url = reverse_lazy('home')
