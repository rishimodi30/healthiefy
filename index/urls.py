from django.urls import path
from django.urls import path
from django.urls.conf import include
from pyrsistent import inc
from . import views

urlpatterns=[
path('',views.index,name='index')

]