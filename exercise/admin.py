from django.contrib import admin

# these lines added:

from django.contrib import admin
from .models import User, Workout


class WorkoutInline(admin.TabularInline):
    model = Workout
    extra = 3


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [WorkoutInline]


admin.site.register(User, UserAdmin)