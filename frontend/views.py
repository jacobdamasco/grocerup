from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# Helper methods
def isEmpty(place):
    numItems = place.count()
    if numItems == 0:
        return True
    else:
        return False


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def dashboard(request):
    items = Item.objects
    fridge = items.filter(place='Fridge')
    freezer = items.filter(place='Freezer')
    pantry = items.filter(place='Pantry')
    
    emptyFridge = isEmpty(fridge)
    emptyFreezer = isEmpty(freezer)
    emptyPantry = isEmpty(pantry)

    context  = {
        'items': items,
        'fridge': fridge,
        'freezer': freezer,
        'pantry': pantry,
        'emptyFridge': emptyFridge,
        'emptyFreezer':emptyFreezer,
        'emptyPantry': emptyPantry,
        }

    return render(request, "dashboard.html", context)

def itemsForm(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')

    context = {'form': form}
    return render(request, "item_form.html", context)

def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')

    context = {'form': form}
    return render(request, "update_item.html", context)

def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/dashboard/')

    context = {'item': item}
    return render(request, "delete_item.html", context)
