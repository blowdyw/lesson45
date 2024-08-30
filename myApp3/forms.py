from django import forms
from .models import Blog, Area




class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']




class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']






class CreateAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'about']



class UpdateArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'about']
