from django.contrib import admin
from blogs.models import Category, new
# Register your models here.
class education(admin.ModelAdmin):
    list_display=('Title','Detail')
admin.site.register(new,education)

class detail(admin.ModelAdmin):
    list_display=('Title','Category','Detail')
admin.site.register(Category,detail)