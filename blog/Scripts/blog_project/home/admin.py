from django.contrib import admin
from .models import modelblogs
# Register your models here.
class blog(admin.ModelAdmin):
    list_display = ['id', 'title']
admin.site.register(modelblogs , blog)