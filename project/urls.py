"""project URL Configuration

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
from project import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('service/',views.service),
    path('contact/',views.contact),
    path('saveenquiry/',views.saveEnquiry, name="saveenquiry"),
    path('pages/blog/',views.blog),
    path('pages/price/',views.price),
    path('pages/team/',views.test),
    path('pages/testimonial/',views.testimonial),
    path('pages/detail/',views.detail),
    path('',views.home),
    path('submitform/',views.submitform , name="submitform"),
    path('userform/',views.userForm),
    path('calculator/',views.calculator),
    path('evenodd/',views.evenodd),
    path('marksheet/',views.marksheet),
    path('newsdetails/<slug>',views.newsDetails)
]
