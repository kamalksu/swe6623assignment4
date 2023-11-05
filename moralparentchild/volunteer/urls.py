from django.urls import path, include
from . import views


urlpatterns = [
    #path('volunteers/', include("django.contrib.auth.urls")),
    path('volunteers/', views.volunteers, name='Volunteers'),
    path('volunteers/apply', views.volunteer_apply, name="apply"),
    path('volunteers/child_approval/<int:id>', views.child_detail, name="child_detail"),
    path('volunteers/parent_approval/<int:id>', views.parent_detail, name="parent_detail")
]