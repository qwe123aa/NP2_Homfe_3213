from django.contrib import admin

from 홈피.models import recipe, CustomUser, CustomUserManager

admin.site.register(recipe)
admin.site.register(CustomUser)