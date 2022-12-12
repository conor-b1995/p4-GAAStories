from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
