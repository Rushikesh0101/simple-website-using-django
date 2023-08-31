from django.urls import path, include
from .import views
from webapp import views

urlpatterns = [
    path('',views.home),
    path('main', views.main),
    path('about', views.about),
    path('contact', views.contact),
]