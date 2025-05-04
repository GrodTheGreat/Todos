from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import views
from django.urls import reverse

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

    def post(self, request: HttpRequest) -> HttpResponse:
        todo_form = forms.CreateTodoForm(request.POST)

        if todo_form.is_valid():
            todo_form.save()

            return HttpResponseRedirect(redirect_to=reverse(viewname="index"))

        context = {"form": todo_form}

        return render(
            request=request,
            template_name="todos/create.html",
            context=context,
        )
