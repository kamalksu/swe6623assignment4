from django.urls import path, include
from . import views

urlpatterns = [
    path('volunteers/', include("django.contrib.auth.urls")),
    path('volunteers/', views.volunteers, name='Volunteers')
]