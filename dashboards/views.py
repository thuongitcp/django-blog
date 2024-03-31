import unicodedata
from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

def vi_slug(data):
    vietnamese_map = {
        # Lower
        ord(u'o'): 'o', ord(u'ò'): 'o', ord(u'ó'): 'o', ord(u'ỏ'): 'o', ord(u'õ'): 'o', ord(u'ọ'): 'o',
        ord(u'ơ'): 'o', ord(u'ờ'): 'o', ord(u'ớ'): 'o', ord(u'ở'): 'o', ord(u'ỡ'): 'o', ord(u'ợ'): 'o',
        ord(u'ô'): 'o', ord(u'ồ'): 'o', ord(u'ố'): 'o', ord(u'ổ'): 'o', ord(u'ỗ'): 'o', ord(u'ộ'): 'o',

        ord(u'à'): 'a', ord(u'á'): 'a', ord(u'á'): 'a', ord(u'ả'): 'a', ord(u'ã'): 'a', ord(u'ạ'): 'a',
        ord(u'ă'): 'a', ord(u'ắ'): 'a', ord(u'ằ'): 'a', ord(u'ẳ'): 'a', ord(u'ẵ'): 'a', ord(u'ạ'): 'a',
        ord(u'â'): 'a', ord(u'ầ'): 'a', ord(u'ấ'): 'a', ord(u'ậ'): 'a', ord(u'ẫ'): 'a', ord(u'ẩ'): 'a',

        ord(u'đ'): 'd', ord(u'Đ'): 'd',

        ord(u'è'): 'e', ord(u'é'): 'e', ord(u'ẻ'): 'e', ord(u'ẽ'): 'e', ord(u'ẹ'): 'e',
        ord(u'ê'): 'e', ord(u'ề'): 'e', ord(u'ế'): 'e', ord(u'ể'): 'e', ord(u'ễ'): 'e', ord(u'ệ'): 'e',

        ord(u'ì'): 'i', ord(u'í'): 'i', ord(u'ỉ'): 'i', ord(u'ĩ'): 'i', ord(u'ị'): 'i',
        ord(u'ư'): 'u', ord(u'ừ'): 'u', ord(u'ứ'): 'u', ord(u'ử'): 'ữ', ord(u'ữ'): 'u', ord(u'ự'): 'u',
        ord(u'ý'): 'y', ord(u'ỳ'): 'y', ord(u'ỷ'): 'y', ord(u'ỹ'): 'y', ord(u'ỵ'): 'y',

        # CAPITAL
        ord(u'Ò'): 'O', ord(u'Ó'): 'O', ord(u'Ỏ'): 'O', ord(u'Õ'): 'O', ord(u'Ọ'): 'O',
        ord(u'Ơ'): 'O',
        ord(u'Ờ'): 'O', ord(u'Ớ'): 'O', ord(u'Ở'): 'O', ord(u'Ỡ'): 'O', ord(u'Ợ'): 'O',
        ord(u'Ô'): 'O',
        ord(u'Ồ'): 'O', ord(u'Ố'): 'O', ord(u'Ổ'): 'O', ord(u'Ỗ'): 'O', ord(u'Ộ'): 'O',

        ord(u'À'): 'A', ord(u'Á'): 'A', ord(u'Ả'): 'A', ord(u'Ã'): 'A', ord(u'Ạ'): 'A',
        ord(u'Ă'): 'A',
        ord(u'Ằ'): 'A', ord(u'Ắ'): 'A', ord(u'Ẳ'): 'A', ord(u'Ẵ'): 'A', ord(u'Ặ'): 'A',
        ord(u'Â'): 'A',
        ord(u'Ầ'): 'A', ord(u'Ấ'): 'A', ord(u'Ẩ'): 'A', ord(u'Ẫ'): 'A', ord(u'Ậ'): 'A',

        ord(u'Đ'): 'D',

        ord(u'È'): 'E', ord(u'É'): 'E', ord(u'Ẻ'): 'E', ord(u'Ẽ'): 'E', ord(u'Ẹ'): 'E',
        ord(u'Ê'): 'E',
        ord(u'Ề'): 'E', ord(u'Ế'): 'E',  ord(u'Ể'): 'E', ord(u'Ễ'): 'E', ord(u'Ệ'): 'E',

        ord(u'Ì'): 'I', ord(u'Í'): 'I', ord(u'Ỉ'): 'I', ord(u'Ĩ'): 'I', ord(u'Ị'): 'I',
        ord(u'Ù'): 'U', ord(u'Ú'): 'U', ord(u'Ủ'): 'U', ord(u'Ũ'): 'U', ord(u'Ụ'): 'U',
        ord(u'Ư'): 'U',
        ord(u'Ừ'): 'U', ord(u'Ứ'): 'U', ord(u'Ử'): 'U', ord(u'Ữ'): 'U', ord(u'Ự'): 'U',
        ord(u'Ỳ'): 'Y', ord(u'Ý'): 'Y', ord(u'Ỷ'): 'Y', ord(u'Ỹ'): 'Y', ord(u'Ỵ'): 'Y',
    }
    slug = slugify(data.translate(vietnamese_map))
    return slug

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

def posts(request):
    try:
        posts = Blog.objects.all()
    except:
        return render(request,'404.html')
    
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False) # Temporarily saving the form
            post.author=request.user
            
            post.save()
            title = form.cleaned_data['title']
            post.slug = vi_slug(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('Data form input is Invalid')
            print(form.errors)

    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    try:
        post = Blog.objects.get(id=pk)
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                title = form.cleaned_data['title']
                post.slug = vi_slug(title) + '-' + str(post.id)
                post.save()
                return redirect('posts')
        form = BlogPostForm(instance=post)
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'dashboard/edit_post.html', context) 
    except:
        return render(request,'404.html') 
    


def del_post(request, pk):
    try:
        post = Blog.objects.get(id=pk)
        post.delete()
        return redirect('posts')
    except:
        return render(request, '404.html')