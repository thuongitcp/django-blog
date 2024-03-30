from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogpost_count = Blog.objects.filter(status='Published').count()

    context = {
        'category_count': category_count,
        'blogpost_count': blogpost_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):

    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'dashboard/edit_category.html', context)

def del_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories')
    # context = {
    #     'category': category,
    #     'form': form,
    # }
    # return render(request, 'dashboard/del_category.html', context)