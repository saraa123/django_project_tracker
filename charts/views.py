from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.db.models import Count, Case, When

from to_do.views import Item, Feature

import random
import datetime
import time

# REST framework
from rest_framework.views import APIView 
from rest_framework.response import Response

users = get_user_model()


# Load charts page
def charts_home(request):
    items = Item.objects.all()
    return render(request, "charts.html", {"item": items})


class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
    
        
        done_issues_count = []
        done_features_count = []

        to_do_issues_count = []
        to_do_features_count = []

        # chart labels and data for issues done and pending
        labels = ["Issues Completed", "Issues To Do"]
        default_items = [done_issues_count, to_do_issues_count]

        # Completed issues count
        Issues_Done_Count = Item.objects.aggregate(
            done_results=Count(Case(When(done=True, then='done')))
        )

        for k, v in Issues_Done_Count.items():
            done_issues_count.append(v)

        # Pending issues count 
        Issues_Not_Done_Count = Item.objects.aggregate(
            not_done_results=Count(Case(When(done=False, then='done')))
        )

        for k,v in Issues_Not_Done_Count.items():
            to_do_issues_count.append(v)


        # chart labels and data for features done and pending 
        progressLabels = ["Features Completed", "Features To Do"]
        progressItems = [done_features_count, to_do_features_count]


        # Completed features count
        Features_done_count = Feature.objects.aggregate(
            done_features=Count(Case(When(done=True, then='done')))
        )

        for k, v in Features_done_count.items():
            done_features_count.append(v)

        # Count for features left to do 
        features_not_done_count = Feature.objects.aggregate(
            not_done_features=Count(Case(When(done=False, then='done')))
        )

        for k,v in features_not_done_count.items():
            to_do_features_count.append(v)
        
        
        data = {
            "labels": labels,
            "default": default_items,
            "progress_labels": progressLabels,
            "progress_default": progressItems
        }

        return Response(data)