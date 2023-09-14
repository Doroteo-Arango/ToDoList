from django.db import models
from django.contrib.auth.models import User


# Create your database models here.
class ToDoList(models.Model):
    # To make lists selective to users, add a foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    # Django doesn't know the type of field that ToDoList is
    # So define the fact that we are using a ForeignKey, in this case a ToDoList object
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text