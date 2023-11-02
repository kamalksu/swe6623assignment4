from django.urls import path
from . import views


urlpatterns = [
    path('parents/', views.parents, name="parents"),
    path('parents/apply', views.parent_apply, name="apply")
]