from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

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
    return render(request, "charts.html")


def pie_chart(request):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_count = User.objects.all().count()
        issue_count = Item.objects.all().count()
        feature_count = Feature.objects.all().count()
        labels = ["Users", "Issues", "Features", "green", "purple", "orange"]
        default_items = [user_count, issue_count, feature_count, 5, 5, 5]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
