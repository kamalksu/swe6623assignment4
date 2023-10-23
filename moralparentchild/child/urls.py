from django.urls import path
from . import views

urlpatterns = [
    path('children/', views.children, name="Children")
]