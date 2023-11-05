from django.urls import path, include
from . import views

urlpatterns = [
    path('children/', include("django.contrib.auth.urls")),
    path('children/<int:id>', views.children, name="Children"),
    path('children/apply', views.child_apply, name="apply")
]