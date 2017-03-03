from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


def login(request):
    '''登陆页面'''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return render(request,'index.html')
        else:
            return render(request, 'login.html', {'login_err': '密码或用户名错误'})
    else:
        return render(request,'login.html')

def logout(request):
    '''退出'''
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def index(request):
    '''主页面'''
    if request.user.is_superuser:
        return render(request,'index.html')