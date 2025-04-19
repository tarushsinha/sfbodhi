from django.urls import path
from . import views

urlpatterns = [
    path('rishta/', views.rishta_view, name='rishta'),
]