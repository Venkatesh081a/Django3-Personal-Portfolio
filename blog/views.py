from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog


def all_blogs(request):
    blog_db = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blog_db})


def detail(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogId': blog_object})
