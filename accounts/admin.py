from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user"]
    model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
