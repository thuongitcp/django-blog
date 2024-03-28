from django.shortcuts import redirect, render

from assignments.models import About
from blog_main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from blogs.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    # Fetch about us
    try:
        about = About.objects.get(id=1)
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)

def register(request):

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else: 
            print(form.errors)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()


    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    # messages.success(request, 'You are logged out')
    return redirect('login')