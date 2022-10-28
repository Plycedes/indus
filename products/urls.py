from django.urls import path
from . import views
from . import new 

urlpatterns = [
    path('', views.index),
    path('new/', new.index)
]