from django.urls import path

from . import views


urlpatterns = [
    path("", views.intro),
    path("image_gallery/",views.show_image_gallery)
]