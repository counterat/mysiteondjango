from django.http import HttpResponse
from .models import * 
from django.shortcuts import render

def index(request):
    all_posts = Post_blog.objects.all

    context = {
        'all_posts': all_posts,  # Передаем список всех постов в контекст шаблона
        'all_works': Works_blog.objects.all
    }
    return render(request, 'index.html', context=context)

def example(request, name=None):
    if name is None:
        return HttpResponse("undefined")
    else:
        return HttpResponse(name)
    return HttpResponse(f'{name}')

# Create your views here.
