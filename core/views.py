from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# Create your views here.
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core/recruiter_dashboard')
            else:
                context = {
                    'form' : form,
                }
                return render(request, 'core/login.html', context)
    context = {
        'form' : form,
    }
    return render(request, 'core/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')