from django.contrib import admin

from 홈피.models import recipe, UserLoginHistory

admin.site.register(UserLoginHistory)
admin.site.register(recipe)