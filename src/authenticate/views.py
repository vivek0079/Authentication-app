from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model,login,logout

from .forms import UserLoginForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/posts")
    context = {
        "form":form,
        "title": "Login"
    }
    return render(request, "login_form.html", context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request):
    return ("djfhdskjf")