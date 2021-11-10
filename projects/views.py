from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
  queryset= Project.objects.filter(featured = True)
  if request.method == "POST":
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    if "project" in request.POST:
      project = request.POST["project"]
    print(name + " " +  email + " " + project + " " + message)
    if name and email != "" and name and email is not None:
      Messages.objects.create(name = name, email = email, project_title = project, message = message)
  context = {
    "projects": queryset
  }
  return render(request, "index.html", context)

def preview(request, id):
  project = Project.objects.get(id = id)
  context = {
    "project": project
  }

  return render(request, "preview.html", context)