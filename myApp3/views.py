from django.shortcuts import render, redirect, HttpResponse
from .models import Blog, Area
from .forms import CreateBlogForm, UpdateBlog, CreateAreaForm, UpdateArea




# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs

    }
    return render(request, 'blogs.html', context)




def createBlog(request):

    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(
            title=title,
            body=body
        )
        return redirect('http://127.0.0.1:8000/home3/in33/')

    form = CreateBlogForm()
    context = {
        "form": form
    }
    return render(request, "blog_form.html", context)


def createBlog1(request):

    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(
            title=title,
            body=body
        )
        return redirect('http://127.0.0.1:8000/home3/in12')

    form = CreateBlogForm()
    context = {
        "form": form
    }
    return render(request, "blog_form.html", context)



def blog3(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs

    }
    return render(request, 'create.html', context)





def update_blog_view(request, id):
    blog = Blog.objects.get(id=id)


    if request.method == "POST":
        blog = UpdateBlog(request.POST, instance=blog)
        if blog.is_valid():
            blog.save()
            return redirect('http://127.0.0.1:8000/home3/in33/')
        return HttpResponse('error')
    UpdateBlogForm = UpdateBlog(instance= blog)

    context = {

        'UpdateBlogForm': UpdateBlogForm

    }
    return render(request, "update_blog.html", context)


def deleteBlog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/home3/in33/')


def area_show(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }
    return render(request, "Area/area.html", context)




def createArea(request):

    if request.method == "POST":
        name = request.POST['name']
        about = request.POST['about']
        Area.objects.create(
            name=name,
            about=about
        )
        return redirect('http://127.0.0.1:8000/home3/area/')

    form = CreateAreaForm
    context = {
        "form": form
    }
    return render(request, "Area/area_form.html", context)




def updateArea(request, id):
    area = Area.objects.get(id=id)


    if request.method == "POST":
        area = UpdateArea(request.POST, instance=area)
        if area.is_valid():
            area.save()
            return redirect('http://127.0.0.1:8000/home3/area/')
        return HttpResponse('error')
    UpdateAreaForm = UpdateArea(instance=area)

    context = {

        'UpdateAreaForm': UpdateAreaForm

    }
    return render(request, "Area/update_area.html", context)



def deleteArea(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('http://127.0.0.1:8000/home3/area/')