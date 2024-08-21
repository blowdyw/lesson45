
from django.urls import path
from .views import vun3
from .views import  blog
from .views import vol
urlpatterns = [

    path('in3/', vun3, name='vun3'),
    path('in33/',blog ,name = 'blog'),
    path('in33/', vol),
]
