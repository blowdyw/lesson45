
from django.urls import path

from .views import *

urlpatterns = [
    path('in33/', blog, name='blog'),
    path('create/', createBlog),
    path('up/<int:id>/', update_blog_view),
    path('create1/', createBlog1),
    path('in12/', blog3),
    path('delete/<int:id>/', deleteBlog ),
    path('area/', area_show),
    path('cArea/',createArea),
    path('upArea/<int:id>/', updateArea),
    path('dArea/<int:id>/', deleteArea),
]
