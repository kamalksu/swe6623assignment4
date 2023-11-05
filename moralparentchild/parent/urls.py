from django.urls import path
from . import views


urlpatterns = [
    path('parents/<int:id>', views.parents, name="parents"),
    path('parents/apply', views.parent_apply, name="apply")
]