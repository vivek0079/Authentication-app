from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Post


def home(request):
    context = {
        "title": "Home",
        "content": "Welcome to Home page",
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "title": "About us",
    }
    return render(request, "about.html",context)

def post_list(request):
    today = timezone.now().date()
    query_list = Post.objects.active()


    paginator = Paginator(query_list, 5) 

    page = request.GET.get('page')
    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)


    context = {
        "query_list": query_list,
    }
    return render(request, "post_list.html",context)

