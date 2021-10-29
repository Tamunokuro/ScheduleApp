from django import forms
from django.forms import fields
from todo.models import Todo, Category


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {'date': forms.TextInput(
            attrs={"placeholder": "YYYY-MM-DD",
                   }
        )
        }
