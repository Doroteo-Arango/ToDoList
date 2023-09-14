from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.

# Allow ToDoList to be viewed from admin site
# If you create a new application or new db model, you must register it as follows
admin.site.register(ToDoList)
admin.site.register(Item)