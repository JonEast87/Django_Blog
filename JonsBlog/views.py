from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, UpdateForm, CommentForm
from .models import Post, Category


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


def LikeView(req, pk):
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

        # grabs posts from post_table and assign the returned data to getLikes
        getLikes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = getLikes.total_likes()

        liked = False
        if getLikes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)

        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # saved user information to make it available for later usage
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


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
