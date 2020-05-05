from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse 
from django.contrib import auth, messages
from .models import Item, Feature, Feedback
from .forms import ItemForm, FeatureForm, FeedbackForm
from django.contrib.auth.models import User
from django.db.models import Count, Case, When

from  products.models import Product

import random

def feature_request_price():
    """ Function to return the price of the 'new feature request' ticket """
    
    # Query the database - look for the new feature request ticket
    products = Product.objects.filter(name='Request a new feature')
    
    for ticket in products:
        ticket_price = ticket.price

    return (ticket_price)

def pending_issue_count(request):
    """ Function to count pending issues """

    # List that will be used to count the issues that are left to do
    not_done_issues_count = []

    # Count how many issues are still pending
    Issues_Not_Done_Count = Item.objects.aggregate(
        not_done_results=Count(Case(When(done=False, then='done')))
    )

    # Append the number of issues not done to the not_done_issues_count list
    for k, v in Issues_Not_Done_Count.items():
            not_done_issues_count.append(v)

    return (not_done_issues_count)

def issues_done_count(request):
    """ Count how many issues are marked as 'done' """

    issues_done = []

    Done_results = Item.objects.aggregate(
        done_results=Count(Case(When(done=True, then='done')))
    )

    for k, v in Done_results.items():
        issues_done.append(v)

    return (issues_done)


def features_done_count(request):
    """ Count how many features are marked as 'done' """

    features_done = []

    Done_features = Feature.objects.aggregate(
        done_features=Count(Case(When(done=True, then='done')))
    )

    for k, v in Done_features.items():
        features_done.append(v)

    return (features_done)


def feature_request_count(request):
    """ Function to count feature requests """

    # List that will be used to count the number of features requested
    pending_features_to_do_count = []

    # Calls the feature_request_price function - returns
    # the price of the feature request ticket.
    feature_price = feature_request_price()

    features = Feature.objects.all()

    for feature in features:

        feature.money_received = feature_price+(feature.like_cost*feature.likes.count())

        if feature.money_received < feature.amount_needed and not feature.done:
            pending_features_to_do_count.append(feature.name)

    
    return (pending_features_to_do_count)

def in_progress_feature(request):
    """ Function for features in progress and count.
    'Features in progress' are those features that have met their monetary target.
    """

    # Feature objects
    features = Feature.objects.all()

    features_in_progress = []

    # Calls the feature_request_price function - returns
    # the price of the feature request ticket.
    feature_price = feature_request_price()

    # Checks how much money each feature has received. If the money has reached
    # the required amount then it will be added to the features_in_progress list
    for feature in features:
        feature.money_received = feature_price+(feature.like_cost*feature.likes.count())

        # Check if the money received equals the amount needed for that feature
        if feature.money_received == feature.amount_needed:
            
            # Ignores features that are marked as 'done'.
            if feature.done == False:
                features_in_progress.append(feature.name)

        # Check if the money receieved is greater than the amount needed 
        elif feature.money_received > feature.amount_needed:
            features_in_progress.append(feature.name)
    
    return (features_in_progress)


def todo_list(request):
    """ Home page """ 

    # Issue objects 
    results = Item.objects.all()

    # Feature objects 
    features = Feature.objects.all()

    # Calls the feature_request_price function - returns
    # the price of the feature request ticket.
    feature_price = feature_request_price()

    # Determines how money_received will be calculated
    for feature in features:
        feature.money_received = feature_price+(feature.like_cost*feature.likes.count())
    
    # Call functions: pending_issue_count and pending_feature_count
    not_done_issues_count = pending_issue_count(request)
    pending_features_to_do_count = len(feature_request_count(request))

    # Calling function - count features in progress 
    features_in_progress = in_progress_feature(request)
    features_in_progress_count = len(features_in_progress)


    return render(request, 'todo_list.html', 
                  {"items": results, 
                  "features": features, 
                  "not_done_issues_count": not_done_issues_count, 
                  "pending_features_to_do_count": pending_features_to_do_count,
                  "features_in_progress": features_in_progress,
                  "features_in_progress_count": features_in_progress_count
                  })

def closed_issues_and_features(request):
    """ Load page displaying issues and features marked as 'done' """

    # Issue objects
    results = Item.objects.all()

    # Feature objects
    features = Feature.objects.all()

    # Call function - count for how many issues are done 
    issues_done = issues_done_count(request)

    # Count for how many features are done
    features_done = features_done_count(request)

    # Call functions: pending_issue_count and pending_feature_count
    not_done_issues_count = pending_issue_count(request)
    pending_features_to_do_count = len(feature_request_count(request))

    # Call in_progress_feature. Count how many features are in progress
    features_in_progress = in_progress_feature(request)
    features_in_progress_count = len(features_in_progress)

    return render(request, "closed_issues_and_features.html",
                {
                    "items": results,
                    "features": features,
                    "not_done_issues_count": not_done_issues_count,
                    "pending_features_to_do_count": pending_features_to_do_count,
                    "features_in_progress_count": features_in_progress_count,
                    "issues_done": issues_done,
                    "features_done": features_done

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

    user = request.user 

    # Query database - find all feedback
    feedback = Feedback.objects.all()

    # Randomly displays feedback with a limit of 4
    random_feedback = random.sample(list(feedback), 4)

    # First check if the user is logged in
    if user.is_authenticated:

        # If they are, proceed to then check if a POST method has been sent
        if request.method == 'POST':
            feedback_form = FeedbackForm(request.POST, request.FILES)

            # Check if the form is valid and save it
            if feedback_form.is_valid():
                form = feedback_form.save(commit=False)
                form.name = user 
                form.save()
                messages.success(request, "Thanks for your feedback!")
                return redirect(add_feedback)
            
            # Display the blank form if it isn't valid upon POST 
            else:
                feedback_form = FeedbackForm()

        # Display the blank form if no POST method has been sent 
        else:
            feedback_form = FeedbackForm()

    # If they aren't logged in they won't be able to send feedback
    else:
        feedback_form = FeedbackForm()

    return render(request, 'add_feedback.html', 
                {'form': feedback_form,
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
    
            
    return redirect(todo_list)

