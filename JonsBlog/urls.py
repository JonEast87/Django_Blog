from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView

# Using class based url
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name="article-detail"),
    path('add_post/', AddPostView.as_view(),
         name="add-post"),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(),
         name="update-post"),
]
