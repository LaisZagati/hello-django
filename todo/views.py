from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm # Import the form

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items 
    }
    return render(request, 'todo/todo_list.html', context)
  

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid(): # Validate the form data
            form.save()  # Save the form data to the database
            return redirect('get_todo_list') # Redirect to the homepage or list view
    
    form = ItemForm() # Create an empty form for GET requests
    context = {
        'form': form     
    }
    
    return render(request, 'todo/add_item.html', context)
  
  
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid(): # Validate the form data
            form.save()  # Save the form data to the database
            return redirect('get_todo_list') # Redirect to the homepage or list view
    form = ItemForm(instance=item) # Create an empty form for GET requests
    context = {
        'form': form     
    }
    return render(request, 'todo/edit_item.html' , context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not Item.done
    item.save()
    return redirect('get_todo_list')
    

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
