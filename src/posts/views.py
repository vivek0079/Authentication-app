from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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
    if request.user.is_staff or request.user.is_superuser:
        query_list = Post.objects.all()
    
    query = request.GET.get("q")
    if query:
        query_list = query_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

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

