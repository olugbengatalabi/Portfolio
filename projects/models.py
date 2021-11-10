from django.db import models
from datetime import datetime, time
from django.utils import timezone
# Create your models here.


class Project(models.Model):
  project_title = models.CharField(max_length=150)
  thumbnail_image = models.ImageField(upload_to ="photos/%Y/%m/%d/")
  banner_image = models.ImageField(upload_to ="photos/%Y/%m/%d/")
  featured = models.BooleanField(default= False)
  about = models.TextField(max_length=10000, null=True, blank=True)
  frontend_framework = models.CharField(max_length= 30, blank = True, null = True)
  frontend_framework_icon = models.CharField(max_length= 100, blank = True, null = True)
  html= models.BooleanField(default = True)
  html_icon = models.CharField(max_length = 50, blank = True, null =True)
  css = models.BooleanField(default = True)
  css_icon = models.CharField(max_length = 50, blank = True, null =True)
  vanilla_javascript = models.BooleanField(default = True)
  js_icon = models.CharField(max_length = 50, blank = True, null =True)
  deployed_to = models.CharField(max_length=20, default="DigitalOcean",blank = True, null = True)
  deployed_to_icon = models.CharField(max_length = 200, blank = True, null =True)
  github_link = models.URLField(max_length=1000, blank=True , null = True)
  server = models.CharField(max_length=20, default= 'Ubuntu v18')
  server_icon= models.CharField(max_length = 200, blank = True, null =True)

  static_files_handling =  models.CharField(max_length=50, blank = True, null = True, default = "NGINX")
  staticfiles_handling_icon = models.CharField(max_length = 200, blank = True, null =True)

  database = models.CharField(max_length=30, default = "Postgres")
  database_icon = models.CharField(max_length = 200, blank = True, null =True)
  version_control = models.CharField(max_length=30, default = "Git")
  version_control_icon= models.CharField(max_length = 200, blank = True, null =True)
  authentication_type = models.CharField(max_length=100, blank =True, null =True)
  backend_framework = models.CharField(max_length=30,blank =True, null =True, default ="Django" )
  backend_framework_icon = models.CharField(max_length=200,blank =True, null =True )
  port_routing = models.CharField(max_length=30, default = "Gunicorn",blank =True, null =True)
  port_routing_icon = models.CharField(max_length=200, blank =True, null =True)
  date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
  other_features = models.CharField(max_length=2000,blank =True, null =True )

  def __str__(self) -> str:
      return str(self.project_title) + str(self.id)


class Messages(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  project_title = models.CharField(blank=True, null= True, max_length=500, default="Unspecified")
  message = models.TextField(max_length=3000)
  date_recieved = models.DateTimeField(auto_now=False, auto_now_add=True)
  read = models.BooleanField(default=False)