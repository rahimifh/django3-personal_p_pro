from django.shortcuts import render, get_object_or_404
from .models import Blog

#Create your views here.

def blog (request):

    pro = Blog.objects.order_by('-date')[:5]
    return render(request, 'Blog/blog.html', {'pro':pro})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'Blog/detail.html', {'blog':blog})
