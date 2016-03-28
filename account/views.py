from django.shortcuts import render


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.contrib import auth
from forms import RegisterUserForm, LoginUserForm
from models import Username



def login_view(request):
    #return HttpResponse('login')
    if request.method == 'POST':
        print "POST"
        logind = LoginUserForm(request.POST)
        print logind
        print request.POST['username']
        if logind.is_vaild():
            username = request.POST['username']
            password = request.POST['password']
            print username,password
            userdate = auth.authenticate(username=username, password=password)
            #if userdata is not None and userdata.is_active:
            #    auth.login(request, userdata)
            #    return HttpResponseRedirect('/index/')
            #else:
            #    return HttpResponseRedirect('/account/login/')
    else:
        print "GET"
        logind = LoginUserForm()
        print logind
    #return HttpResponse('login')
	return render(request, 'bs1/account/login_view.html',locals())

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")

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
            user = auth.models.User.objects.create_user(username,password)
			#user = auth.models.User.objects.create_user('abc','111')
            user.save()
    else:
        userdata = RegisterUserForm()

    return render(request, 'bs1/account/register.html',locals())



    #return HttpResponse('register')

@login_required
def index(request):
    return HttpResponse('index')


