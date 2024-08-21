from django.shortcuts import render
from .models import Blog
from .models import Vol
# Create your views here.
def vun3(request):
    return render(request, "vun3.html")


def blog(request):
    blogs = Blog.objects.filter().first()
    context = {
        'blogs': blogs

    }
    return render(request, 'blogs.html', context)


def vol(request):
    vols = Vol.objects.filter().first()
    context = {
        'vols': vols

    }
    return render(request, 'blogs.html', context)