from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item, Feature
from .forms import ItemForm, FeatureForm

# Create your views here.
def todo_list(request):
    results = Item.objects.all()
    feature_results = Feature.objects.all()
    return render(request, 'todo_list.html', {"items": results, "name": feature_results})

def new_item(request):
    if request.method=='POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(todo_list)
    else:
            form = ItemForm()

    return render(request, 'add_new_item.html', {'form': form})

def edit_an_item(request, id):
        item = get_object_or_404(Item, pk=id)
        form = ItemForm(instance=item)

        if request.method == 'POST':
                form = ItemForm(request.POST, instance=item)

                if form.is_valid():
                        form.save()
                        return redirect(todo_list)
        else:
                form = ItemForm(instance=item)


        
        return render(request, 'edit_issue.html', {'form': form})


def toggle_status(request, id):
        item = get_object_or_404(Item, pk=id)
        item.done = not item.done
        item.save()
        return redirect(todo_list)
