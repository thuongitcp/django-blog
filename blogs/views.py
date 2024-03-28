from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category
from django.db.models import Q
def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exist
    try:
        category = Category.objects.get(id=category_id)
    except:
        # Redirect the user to homepage or render to 404 page
        return render(request,'404.html')
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    try: 
        single_blog = Blog.objects.get(slug=slug, status='Published')
    except:
        return render(request,'404.html')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)