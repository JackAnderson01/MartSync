from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email', 'created', 'updated']
    list_filter=['created', 'updated']
    search_fields=['id','name','email']

admin.site.register(User, UserAdmin)