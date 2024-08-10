from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test_ops-home'),
]