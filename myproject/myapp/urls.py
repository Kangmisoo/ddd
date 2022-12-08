"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views 
urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('user/', views.datalist, name='list'),
    path('user/add', views.add),
    path('user/add/addrecord', views.addrecord),
    path('user/delete/<int:id>', views.delete),
    path('user/update/<int:id>', views.update),
    path('user/update/updaterecord/<int:id>', views.updaterecord),
]
