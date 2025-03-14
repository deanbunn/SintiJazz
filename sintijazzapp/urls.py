from django.urls import path
from . import views

app_name="sintijazzapp"
urlpatterns = [
    path("", views.index)
]
