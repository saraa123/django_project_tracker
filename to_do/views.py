from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse 
from django.contrib import auth, messages
from .models import Item, Feature, Feedback
from .forms import ItemForm, FeatureForm, FeedbackForm
from django.contrib.auth.models import User
from django.db.models import Count, Case, When

import random


def todo_list(request):
    """ Home page """ 

    # Issue objects 
    results = Item.objects.all()

    # Feature objects 
    feature_results = Feature.objects.all()

    # List that will be used to count the issues that are left to do 
    not_done_issues_count = []

    # List that will be used to count the features that are left to do
    pending_features_to_do_count = []

    # Count how many issues are marked as 'done' 
    Done_results = Item.objects.aggregate(
        done_results=Count(Case(When(done=True, then='done')))
    )


    # Count how many issues are still pending
    Issues_Not_Done_Count = Item.objects.aggregate(
        not_done_results=Count(Case(When(done=False, then='done')))
    )

    # Append the number of issues not done to the not_done_issues_count list
    for k, v in Issues_Not_Done_Count.items():
            not_done_issues_count.append(v)


    # Features pending to do count
    features_not_done_count = Feature.objects.aggregate(
        not_done_features=Count(Case(When(done=False, then='done')))
    )

    # Append number of features still pending to the pending_features_to_do_count list
    for k,v in features_not_done_count.items():
            pending_features_to_do_count.append(v)

    feedback = Feedback.objects.all()

    random_feedback = random.choice(feedback)

    return render(request, 'todo_list.html', 
                  {"items": results, 
                  "name": feature_results, 
                  "Done_results": Done_results, 
                  "not_done_issues_count": not_done_issues_count, 
                  "pending_features_to_do_count": pending_features_to_do_count,
                  "feedback": feedback,
                  "random_feedback": random_feedback})


def new_item(request):
    """ Function for adding a new issue """

    if request.method=='POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(todo_list)
    else:
            form = ItemForm()

    return render(request, 'add_new_item.html', {'form': form})


def add_feedback(request):
    """ Function for adding feedback """

    feedback = Feedback.objects.all()

    random_feedback = random.choice(feedback)


    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Thanks for your feedback!")    
            form.save()
            return redirect(todo_list)
    else:
            form = FeedbackForm()


    return render(request, 'add_feedback.html', 
                {'form': form,
                "feedback": feedback,
                "random_feedback": random_feedback})



def toggle_status(request, id):
    """ Function to upvote an issue or feature """ 

    user = request.user

    # Check if the user is logged in
    if user.is_authenticated():

            # If user likes an issue
            if Item.objects.filter(pk=id).exists():
                    item = get_object_or_404(Item, pk=id)
                    if user in item.likes.all():
                            item.likes.remove(user)
                    else:
                            item.likes.add(user)

            # If user likes a feature 
            if Feature.objects.filter(pk=id).exists():
                    feature = get_object_or_404(Feature, pk=id)
                    if user in feature.likes.all():
                            feature.likes.remove(user)
                    else:
                            feature.likes.add(user)

        
    return redirect(todo_list)


