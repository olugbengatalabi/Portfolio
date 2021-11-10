from django.contrib import admin
from .models import Project,Messages
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ['project_title', 'featured','date_created' ]
  list_display_links = ["project_title"]
  list_editable = [ "featured"]
  list_filter = ["featured", 'date_created']

class MessagesAdmin(admin.ModelAdmin):
  list_display = ["read", "name", "date_recieved"]
  list_display_links = ["name"]
  list_editable = ["read"]
  list_filter = ["read", "date_recieved", "name"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Messages, MessagesAdmin)