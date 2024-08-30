
from django.urls import path
from .views import *

urlpatterns = [


    path('region/', region_show),
    path('about/', about_show),
    path('cRegion/', createRegion)
]
