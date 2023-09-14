from django import forms

class CreateNewList(forms.Form):
    # Same fields as in ToDoList db
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)