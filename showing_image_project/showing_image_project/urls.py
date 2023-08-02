
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image/',include('image_gallery.urls')),
     path('',views.intro)
]
