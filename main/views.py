from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views (webpages & HTTP requests) here.

def index(response, id):
    # Type the id of a ToDoList in the address bar
    ls = ToDoList.objects.get(id=id)
    
    # For list.html - creation of custom form
    if response.method == "POST":
        #print(response.POST)
        # Updating check buttons upon input
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
            item.save()
        
        # Adding new item to list
        elif response.POST.get("newItem"):
            # Get text from text input field
            txt = response.POST.get("new")
            # Check for valid input since we are using custom, not Django, forms
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid Input")
                
    # Show HTML template
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

# Allow users to create new lists
def create(response):
    # To get user from within code
    # response.user
    
    # Create a blank form that will get passed into HTML
    # Django will know what to do with it
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            # Create new to do list & add that with name given
            # # Save specific list to user
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
        # Redirect to page that has been defined by the new list
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})