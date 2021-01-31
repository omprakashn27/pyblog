from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    form = Blogs.objects.all()
    context = {'form':form}
    return render(request, 'post/index.html', context)



@login_required(login_url='login')
def addblog(request):
    # form = BlogsForm()
    if request.method == "POST":
        blog = Blogs()
        blog.title = request.POST.get("title","")
        blog.description = request.POST.get("description", "")
        blog.created_by = request.user
        blog.save()
        messages.success(request, "Blog added successfully")
        return redirect('/')

    # context = {'form':form}
    return render(request, 'post/add.html')

def viewBlog(request, id):
    form = Blogs.objects.get(id=id)
    context = {'form':form}
    return render(request, 'post/view.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
        
            user = authenticate(request, username=email, password=password) 
            if user is not None:
                login(request, user)
                redirect('/')
            else:
                messages.warning(request, "Email or password doesnot match")
    return render(request, 'post/login.html')

def registerPage(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect('/')
    else:
        form = CustomUserForm()

        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    context = {'form':form}
    return render(request, 'post/register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')