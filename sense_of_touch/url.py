from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact,name="contact"),
    path("Gallery",views.gallery, name="gallery"),
    path("About",views.about,name="about")
]