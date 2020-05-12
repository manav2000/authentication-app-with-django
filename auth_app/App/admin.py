from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'nationality')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
