from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
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
    if request.user.is_staff or request.user.is_superuser:
        query_list = Post.objects.all()
    

    paginator = Paginator(query_list, 1) 
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)


    context = {
        "title": "All Posts",
        "query_list": query_list,
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "post_list.html",context)

def post_detail(request, title=None):
    instance = get_object_or_404(Post, slug=title)
    title = instance.title
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title": title,
        "instance": instance,        
    }
    return render(request, "post_detail.html",context)