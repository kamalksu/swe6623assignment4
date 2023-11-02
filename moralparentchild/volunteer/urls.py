from django.urls import path, include
from . import views

urlpatterns = [
    path('volunteers/', include("django.contrib.auth.urls")),
    path('volunteers/', views.volunteers, name='Volunteers'),
    path('volunteers/apply', views.volunteer_apply, name="apply")
]