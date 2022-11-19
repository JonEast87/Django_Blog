from django.urls import path

from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, \
    AddCategoryView, category_view, category_life_view, like_view, AddCommentView

# Using class based url
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name="article-detail"),
    path('add_post/', AddPostView.as_view(),
         name="add-post"),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(),
         name="update-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(),
         name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', category_view, name='category'),
    path('category-list', category_life_view, name='category-list'),
    path('like/<int:pk>', like_view, name='like-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
