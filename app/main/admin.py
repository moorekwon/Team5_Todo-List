from django.contrib import admin

# Register your models here.
from main.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
