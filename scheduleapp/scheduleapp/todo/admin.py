from django.contrib import admin
from todo.models import Todo, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'date', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Todo, TodoAdmin)
