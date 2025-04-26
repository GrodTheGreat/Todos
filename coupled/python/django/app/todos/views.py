from functools import wraps
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User
from .forms import CreateTodoForm, TodoDetailsForm
from .models import Todo


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request: HttpRequest, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect(to="login")

        return view_func(request, *args, **kwargs)

    return wrapped_view


@login_required
def index(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    user = get_object_or_404(klass=User, pk=request.session["user_id"])
    todos = Todo.objects.filter(user=user)

    context = {"todos": todos}
    return render(request=request, template_name="todos/index.html", context=context)


@login_required
def create(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET", "POST"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    user = get_object_or_404(klass=User, pk=request.session["user_id"])
    form = CreateTodoForm(request.POST if request.method == "POST" else None)

    if request.method == "POST" and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        Todo.objects.create(user=user, title=title, description=description)
        return redirect(to="todos-list")

    context = {"form": form}
    return render(request=request, template_name="todos/create.html", context=context)


@login_required
def details(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET", "PATCH", "DELETE"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    user = get_object_or_404(klass=User, pk=request.session["user_id"])
    todo = get_object_or_404(klass=Todo, user=user, pk=pk)
    form = TodoDetailsForm(instance=todo)

    context = {"todo": todo, "form": form}

    return render(request=request, template_name="todos/details.html", context=context)
