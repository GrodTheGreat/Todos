from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django import views


class Index(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="todos/index.html")
