from django.shortcuts import render, redirect, HttpResponse
from .models import Region, Bout
from .forms import CreateRegionForm, UpdateRegionForm
# Create your views here.


def region_show(request):
    regions = Region.objects.all()
    context = {
        'regions': regions

    }
    return render(request, "Region/region.html", context)


def about_show(request):
    bouts = Bout.objects.all()
    context = {
        'bouts': bouts

    }
    return render(request, "about.html", context)


def createRegion(request):
    if request.method == "POST":
        name = request.POST['name']
        about = request.POST['about']
        Region.objects.create(
            name=name,
            about=about
        )
        return redirect('http://127.0.0.1:8000/home2/region/')

    form = CreateRegionForm
    context = {
        'form': form
    }
    return render(request,"Region/region.html", context)



