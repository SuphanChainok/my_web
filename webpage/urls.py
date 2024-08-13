from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs, name="contact"),
    path('for/', views.forPage, name="for-page"),
    path("card/", views.cardPage, name='card-page'),
    path("color/", views.cardColorPage, name="color-page"),
]
