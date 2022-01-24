from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>', views.read),
    path('delete/', views.delete),
    path('update/<id>', views.update),
]
