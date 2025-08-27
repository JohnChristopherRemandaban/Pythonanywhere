from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'user', 'created_date', 'due_date')
    list_filter = ('status', 'category', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
