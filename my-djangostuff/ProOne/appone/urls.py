from django.urls import path
from appone import views

urlpatterns = [
    path('',views.index,name='index'),
    path('help/',views.helper,name='helper'),
]