from django.contrib import admin
from django.urls import path
from Winfo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('about',About,name='about'),
]
