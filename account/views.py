from django.shortcuts import render


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
#from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from forms import RegisterUserForm, LoginUserForm
from models import Username
from django.contrib.auth.models import User

#import django.contrib.auth.views.login 

def login_view(request):
    #return HttpResponse('login')
    if request.method == 'POST':
        print "POST"
        logind = LoginUserForm(request.POST)
        #print logind
        #print request.POST['username']
        if logind.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print username,password
            userdata = authenticate(username=username, password=password)
            if userdata is not None and userdata.is_active:
                login(request, userdata)
                #return HttpResponseRedirect('/account/index/')
                return HttpResponseRedirect(request.POST.get('next'))
                #return HttpResponseRedirect('/account/index/?next=/images/')
            else:
                return HttpResponseRedirect('/account/login/')

    else:
        
        print "GET"
        logind = LoginUserForm()
    #return HttpResponse('login')
    return render(request, 'bs1/account/login_view.html',locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/account/login/")

def register(request):
    if request.method == 'POST':
        userdata = RegisterUserForm(request.POST)
        if userdata.is_valid():
            print request
            print request.POST['username']
            #data = Username(username = request.POST['username'],
            #                password = request.POST['password'],
            #                usertype = request.POST['usertype']
			#				)
            #data.save()
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username,password=password)
			#user = auth.models.User.objects.create_user('abc','111')
            user.save()
        print type(userdata)
    else:
        userdata = RegisterUserForm()

    return render(request, 'bs1/account/register.html',locals())



    #return HttpResponse('register')

@login_required()
def index(request):
    try:
        user = request.user.username
    except  User.DoesNotExist:
        #//handle the case when the user does not exist.
        user = "index"
    return HttpResponse(user)


