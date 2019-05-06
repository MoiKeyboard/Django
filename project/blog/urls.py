from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    # Class based views
    path("", PostListView.as_view(), name="blog-home"),
    # Non-classed based views
    # path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
