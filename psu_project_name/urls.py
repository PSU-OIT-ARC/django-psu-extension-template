from django.urls import path
from . import views

urlpatterns = [
    # A simple test page
    path("", views.index, name="{{ project_name }}_index"),
]
