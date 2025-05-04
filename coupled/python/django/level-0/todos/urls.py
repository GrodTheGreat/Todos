from django.urls import path

from todos.views import (
    TodoIndexView,
    CreateTodoView,
    EditTodoView,
    DeleteTodoView,
    TodoDetailsView,
)

urlpatterns = [
    path(route="", view=TodoIndexView.as_view(), name="todo-list"),
    path(route="add", view=CreateTodoView.as_view(), name="create-todo"),
    path(route="<int:pk>/", view=TodoDetailsView.as_view(), name="todo-detail"),
    path(
        route="<int:pk>/edit", view=EditTodoView.as_view(), name="update-todo"
    ),
    path(
        route="<int:pk>/delete",
        view=DeleteTodoView.as_view(),
        name="delete-todo",
    ),
]
