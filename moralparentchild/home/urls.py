from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('home/childview/<int:id>', views.child_detail, name="childview")
]