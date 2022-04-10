"""healthiefy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pyrsistent import inc
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('index.urls'),name="index"),
    
    path('about/',include('about.urls'),name="about"),
    
    path('diagnosis/',include('diagnosis.urls'),name="diagnosis"),
    
    path('docguide/',include('docguide.urls'),name="docguide"),
    
    path('covidalerts/',include('covidalerts.urls'),name="covidalerts"),
    
    #path('predict_res/',views.predict_res,name="predict_res"),
]
