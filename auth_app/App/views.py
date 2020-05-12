from django.shortcuts import render
from .forms import UserForm, UserProfileForm, ResetPassword
from django.contrib.auth.models import User
from django import forms
from auth_app.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import UserProfile

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'App/index.html')


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            subject = 'Welcome to DJANGO AUTHENTICATION APP'
            message = 'Hope you are enjoying DJANGO AUTHENTICATION APP'
            recepient = str(user_form['email'].value())
            send_mail(subject,
                      message, EMAIL_HOST_USER, [recepient], fail_silently=False)

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)

    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    return render(request, 'App/registration.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'registered': registered
    })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'App/greeting.html', {'username': username.upper()})

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login to your account")
            return HttpResponse('Invalid login details')

    else:
        return render(request, 'App/login.html')


def reset_password(request):
    if request.method == 'POST':

        reset_form = ResetPassword(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(reset_form.is_valid()):
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        reset_form = ResetPassword()

    return render(request, 'App/reset_pwd.html', {'reset_form': reset_form})
