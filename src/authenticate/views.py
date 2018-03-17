from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

from .forms import UserLoginForm, UserRegisterForm
from .tokens import account_activation_token

User = get_user_model()
 
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
        "login_form":form,
        "title": "Login"
    }
    return render(request, "login_form.html", context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':user.pk,
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        if next:
            return redirect(next)
        return HttpResponse('Please confirm your email address to complete the registration')

    context = {
        "title": "Register",
        "register_form": form,
    }
    return render(request, "register_form.html", context)

def activate(request, uid, token):
    try:
        uid = uid
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        context = {
            "username":user.username,
        }
        return render(request, "success_message.html", context)
    else:
        return HttpResponse('Activation link is invalid!')