from django.shortcuts import render


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.contrib import auth
from forms import RegisterUserForm
from models import Username

def login_view(request):
    return HttpResponse('login')

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")

def register(request):
    if request.method == 'POST':
        user = RegisterUserForm(request.POST)
        if user.is_valid():
            print request
            data = Username(username = request.POST['username'],
                            password = request.POST['password'],
                            usertype = request.POST['usertype'])
            data.save()
    else:
        data = RegisterUserForm()

    return render(request, 'bs1/account/register.html',locals())



    return HttpResponse('register')

@login_required
def index(request):
    return HttpResponse('index')


