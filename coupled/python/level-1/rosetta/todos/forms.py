from django import forms

from .models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ["is_complete"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "required": True,
                    "class": "form-input__text",
                    "placeholder": "Todo",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-input__text",
                    "placeholder": "(Optional)",
                }
            ),
        }
