from django.urls import path
from . import views

urlpatterns = [
  path("index", views.index, name = "index"),
  path("preview/<int:id>", views.preview, name = "preview"),
]