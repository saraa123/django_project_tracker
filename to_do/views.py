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
    features = Feature.objects.all()

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


    for feature in features:
        like_cost = feature.like_cost
        amount_got = feature.likes.count() * like_cost

        print("feature name", feature.name)
        print("like cost", feature.like_cost)
        print("like amount", feature.likes.count())
        print("amount_got",amount_got)
        print("--------------------")


    
    return render(request, 'todo_list.html', 
                  {"items": results, 
                  "features": features, 
                  "Done_results": Done_results, 
                  "not_done_issues_count": not_done_issues_count, 
                  "pending_features_to_do_count": pending_features_to_do_count,
                  "amount_got": amount_got
                  })


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

    # Query database - find all feedback
    feedback = Feedback.objects.all()

    # Randomly displays feedback
    random_feedback = random.choice(feedback)

    # The feedback form
    form = FeedbackForm(request.POST, request.FILES)

    
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, "Thanks for your feedback!")    
            form.save()
            return redirect(todo_list)
        else:
            form = FeedbackForm()


     # Check if the user is logged in
    if not request.user.is_authenticated:
            form.name='anonymous'
            user=form.name
    else:
        user = User.objects.get(email=request.user.email)
        
    return render(request, 'add_feedback.html', 
                {'form': form,
                "feedback": feedback,
                "random_feedback": random_feedback,
                "user": user})



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
                    like_cost = feature.like_cost

                    if user in feature.likes.all():
                            feature.likes.remove(user)
                            amount_got = like_cost * feature.likes.count()
                            
                    else:
                            feature.likes.add(user)
                            amount_got = like_cost * feature.likes.count()
                    
                    # See if the amount we have towards a feature equals the amount we need
                    if amount_got >= like_cost:
                        if amount_got == like_cost:
                            print("We've hit our target!")
                        elif amount_got > like_cost:
                            print("Over our target!")
            
    return redirect(todo_list)


