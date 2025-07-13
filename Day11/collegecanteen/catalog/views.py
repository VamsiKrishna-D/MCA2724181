from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodItem
from .forms import FoodItemForm

def food_list(request):
    items = FoodItem.objects.all()
    return render(request, 'food_list.html', {'items': items})

def food_detail(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    return render(request, 'food_detail.html', {'item': item})

def food_create(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'food_form.html', {'form': form})

def food_update(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food_detail', pk=pk)
    else:
        form = FoodItemForm(instance=item)
    return render(request, 'food_form.html', {'form': form})

def food_delete(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('food_list')
    return render(request, 'food_confirm_delete.html', {'item': item})
