from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django import views

from .models import Todo
from .forms import CreateTodoForm, DeleteTodoForm, EditTodoForm


class TodoIndexView(views.View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest) -> HttpResponse:
        todos = Todo.objects.all()
        context = {"todos": todos}

        return render(
            request=request,
            template_name="todos/todo-list.html",
            context=context,
        )


class TodoDetailsView(views.View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        todo = get_object_or_404(Todo, pk=pk)
        context = {"todo": todo}

        return render(
            request=request,
            template_name="todos/todo-detail.html",
            context=context,
        )


class CreateTodoView(views.View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest) -> HttpResponse:
        form = CreateTodoForm()
        context = {"form": form}

        return render(
            request=request,
            template_name="todos/create-todo.html",
            context=context,
        )

    # noinspection PyMethodMayBeStatic
    def post(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="todo-list")

        context = {"form": form}
        return render(
            request=request,
            template_name="todos/create-todo.html",
            context=context,
        )


class DeleteTodoView(views.View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        todo = get_object_or_404(Todo, pk=pk)
        context = {"todo": todo}

        return render(
            request=request,
            template_name="todos/delete-todo.html",
            context=context,
        )

    # noinspection PyMethodMayBeStatic
    def post(
        self,
        request: HttpRequest,
        pk: int,
    ) -> HttpResponse | HttpResponseRedirect:
        form = DeleteTodoForm(request.POST)
        if form.is_valid():
            todo = get_object_or_404(Todo, pk=pk)
            todo.delete()

            return redirect(to="todo-list")

        context = {"form": form}

        return render(
            request=request,
            template_name="todos/delete-todo.html",
            context=context,
        )


class EditTodoView(views.View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        todo = get_object_or_404(Todo, pk=pk)
        form = EditTodoForm(instance=todo)
        context = {"form": form, "id": pk}

        return render(
            request=request,
            template_name="todos/update-todo.html",
            context=context,
        )

    # noinspection PyMethodMayBeStatic
    def post(
        self,
        request: HttpRequest,
        pk: int,
    ) -> HttpResponse | HttpResponseRedirect:
        todo = get_object_or_404(Todo, pk=pk)
        form = EditTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()

            return redirect(to="todo-list")

        context = {"form": form}

        return render(
            request=request,
            template_name="todos/update-todo.html",
            context=context,
        )
