from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('/about', views.about, name='about'),
     path('/mentor', views.mentor, name='mentor'),
     path('/result', views.result, name='result'),
     path('/about', views.about, name='about'),
     path('/internship', views.internship, name='internship'),
]