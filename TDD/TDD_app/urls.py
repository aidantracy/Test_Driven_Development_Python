from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('form_route', views.some_function)
]
