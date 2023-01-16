"""pro1 URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('cl_c_admn',views.cl_c_admn),
    # path('admn_v_proj',views.admn_v_proj),
    path('contact',views.con),
    path('reg',views.register),
    path('proj',views.proj),
    path('about',views.about),
    path('services',views.services),
    path('blog',views.blog),
    path('login_pg',views.login_pg),
    path('log',views.logi),
    path('addProject',views.add_project),
    path('addPro',views.addPro),
    path('adminViewPro',views.adminViewPro),
    path('adhd',views.adhd),
    # path('new_update',views.new_up),
    path('updateProject',views.ppup),
    path('delete/<a>',views.Pdelete),

    path('cont', views.cont)
]
