from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.db.models import Count, Case, When

from to_do.views import Item, Feature, in_progress_feature, feature_request_count

import random
import datetime
import time

""" REST framework """
from rest_framework.views import APIView 
from rest_framework.response import Response

""" Global variable to return the user """
users = get_user_model()

def charts_home(request):
    """ Load charts page """
    items = Item.objects.all()
    return render(request, "charts.html", {"item": items})


class ChartData(APIView):
    """ Chart data and labels for issues and features """

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        """ Issues chart containing all functions and counts """
        
        # Issues done count
        done_issues_count = []

        # Issues pending count 
        to_do_issues_count = []

        # Completed issues count
        Issues_Done_Count = Item.objects.aggregate(
            done_results=Count(Case(When(done=True, then='done')))
        )

        # Will append the issues that are done to the done_issues_count list
        for k, v in Issues_Done_Count.items():
            done_issues_count.append(v)

        # Pending issues count
        Issues_Not_Done_Count = Item.objects.aggregate(
            not_done_results=Count(Case(When(done=False, then='done')))
        )

        # Appends issues not done to the to_do_issues_count list
        for k, v in Issues_Not_Done_Count.items():
            to_do_issues_count.append(v)

        # Chart labels and data for issues done and pending
        labels = ["Issues Completed", "Issues To Do"]
        default_items = [done_issues_count, to_do_issues_count]

        """ Features chart containing all functions and counts """

        # Features done count
        done_features_count = []

        # Count for number of features in progress
        features_in_progress = in_progress_feature(request)
        features_in_progress_count = len(features_in_progress)

        # Count for number of features requested 
        feature_requests = len(feature_request_count(request))
    
        # Completed features count
        Features_done_count = Feature.objects.aggregate(
            done_features=Count(Case(When(done=True, then='done')))
        )

        # Appends features that are done to the done_features_count list
        for k, v in Features_done_count.items():
            done_features_count.append(v)
        
        # Chart labels and data for features done, requests, and in progress 
        progressLabels = ["Requests", "Completed", "In progress"]
        progressItems = [feature_requests, done_features_count, features_in_progress_count]

        
        # Data to be returned and used for the charts
        data = {
            "labels": labels,
            "default": default_items,
            "progress_labels": progressLabels,
            "progress_default": progressItems
        }

        return Response(data)
