from django.urls import path
from . import views

urlpatterns=[
 path('home/', views.home, name="home_path"),
 path('about/', views.about, name="about_path"),
 path('', views.home, name="home_path2"),
]