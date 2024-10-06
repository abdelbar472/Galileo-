from django.urls import path
from . import views
urlpatterns = [
    path("blog/", views.BlogPostListCreate.as_view(), name="blogpost-list-create"),
    #path("blog/<int:pk>/", views.BlogPostDetail.as_view(), name="blogpost-detail"),
]