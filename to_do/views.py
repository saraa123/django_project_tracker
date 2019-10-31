from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse 
from .models import Item, Feature
from .forms import ItemForm, FeatureForm
from django.contrib.auth.models import User
from django.db.models import Count, Case, When


# Create your views here.
def todo_list(request):

    # Issue objects 
    results = Item.objects.all()

    # feature objects 
    feature_results = Feature.objects.all()

    # Count array for issues that are left to do 
    not_done_issues_count = []

    # Count array for features left to do 
    pending_features_to_do_count = []

    # Count for issues that are done 
    Done_results = Item.objects.aggregate(
        done_results=Count(Case(When(done=True, then='done')))
    )


# pending issues to do count
    Issues_Not_Done_Count = Item.objects.aggregate(
        not_done_results=Count(Case(When(done=False, then='done')))
    )

    for k, v in Issues_Not_Done_Count.items():
            not_done_issues_count.append(v)


# features pending to do count
    features_not_done_count = Feature.objects.aggregate(
        not_done_features=Count(Case(When(done=False, then='done')))
    )

    for k,v in features_not_done_count.items():
            pending_features_to_do_count.append(v)

    
    return render(request, 'todo_list.html', 
                  {"items": results, "name": feature_results, "Done_results": Done_results, 
                  "not_done_issues_count": not_done_issues_count, "pending_features_to_do_count": pending_features_to_do_count})

def new_item(request):
    # Function for adding a new issue

    if request.method=='POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(todo_list)
    else:
            form = ItemForm()

    return render(request, 'add_new_item.html', {'form': form})



def toggle_status(request, id):
    # Function to upvote an issue or feature

    user = request.user

    if user.is_authenticated():
            # if user likes an issue

            if Item.objects.filter(pk=id).exists():
                    item = get_object_or_404(Item, pk=id)
                    if user in item.likes.all():
                            item.likes.remove(user)
                    else:
                            item.likes.add(user)

            # if user likes a feature 

            if Feature.objects.filter(pk=id).exists():
                    feature = get_object_or_404(Feature, pk=id)
                    if user in feature.likes.all():
                            feature.likes.remove(user)
                    else:
                            feature.likes.add(user)

        
    return redirect(todo_list)


