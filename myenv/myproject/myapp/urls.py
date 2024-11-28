"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views

urlpatterns = [
    
    path('',views.Home,name='Home'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('destination',views.destination,name='destination'),
    path('guide',views.guide,name='guide'),
    path('package',views.packageing,name='package'),
    path('service',views.service,name='service'),
    path('signal',views.signal,name='signal'),
    path('testimonial',views.testimonial,name='testimonial'),
    # path('search/', views.search_view, name='search_view'),
    path('ad_home',views.ad_home,name='ad_home'),
    path('ad_package',views.package1,name='ad_package'),
    path('login',views.login1,name='login'),
    path('logout',views.logout,name='logout'),
    
]
