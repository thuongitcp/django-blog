from django import forms

from blogs.models import Category, Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ='__all__'


choices = Category.objects.all().values_list('category_name', 'category_name')
choice_list = []

for item in choices:
    choice_list.append(item)
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'owner_user', 'type': 'hidden'}),
        #     'blog_body': forms.Textarea(attrs={'class': 'form-control'}),
        #     # 'status': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'is_featured': forms.Boo(attrs={'class': 'form-control'}),

        # }