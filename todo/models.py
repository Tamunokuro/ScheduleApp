from django.db import models
from django import forms
from django.forms import widgets
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=264)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Todo(models.Model):
    task = models.CharField(max_length=500)
    date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=CASCADE)

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self):
        return self.task
