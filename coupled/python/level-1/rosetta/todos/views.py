from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django import views

from . import forms


class Index(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="todos/index.html")


class Create(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = forms.CreateTodoForm()
        context = {"form": form}
        return render(
            request=request,
            template_name="todos/create.html",
            context=context,
        )
