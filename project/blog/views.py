from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.contrib import messages

# from django.http import HttpResponse

# # Dummy dictonary posts
# posts = [
#     {
#         'author': 'Qwek',
#         'title': 'Post 1',
#         'content': 'Helloworld!',
#         'date_posted': '25 April 2019'
#     }
# ]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)  # render returns http


# Class based views
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<moddel>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]


# Class based views
class PostDetailView(DetailView):
    model = Post


# Class based views
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        messages.success(self.request, f"Post created!")
        form.instance.author = self.request.user
        return super().form_valid(form)


# Class based views
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        messages.success(self.request, f"Post updated!")
        form.instance.author = self.request.user
        return super().form_valid(form)

    # return 403 if not author != user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Class based views
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    # return 403 if not author != user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})  # render returns http


#  HTTPRESONSE EXAMPLE
#  def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
