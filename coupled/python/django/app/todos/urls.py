from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="todos-list"),
    path(route="create", view=views.create, name="create-todo"),
    path(route="<int:pk>", view=views.details, name="todo-details"),
]
