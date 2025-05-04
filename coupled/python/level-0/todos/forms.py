# 3rd party imports
from django import forms

# Custom imports
from .models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]


class DeleteTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = []


class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
