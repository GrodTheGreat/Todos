import bcrypt
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm
from .models import User


def index(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    return render(request=request, template_name="accounts/index.html")


def login(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET", "POST"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    form = LoginForm(request.POST if request.method == "POST" else None)

    if request.method == "POST" and form.is_valid():
        email: str = form.cleaned_data["email"]
        password: str = form.cleaned_data["password"]
        user = User.objects.filter(email=email).first()
        if user is None or not bcrypt.checkpw(
            password=password.encode(), hashed_password=user.password_hash.encode()
        ):
            form.add_error(
                field=None,
                error="Email and Password combination does not match any known users",
            )
        else:
            request.session["user_id"] = user.id
            return redirect(to="todos-list")

    context = {"form": form}
    return render(request=request, template_name="accounts/login.html", context=context)


def logout(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET", "POST"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    if request.method == "POST":
        request.session.pop("user_id")
        return redirect(to="home")

    return render(request=request, template_name="accounts/logout.html")


def register(request: HttpRequest) -> HttpResponse | HttpResponseNotAllowed:
    PERMITTED_METHODS = ["GET", "POST"]
    if request.method not in PERMITTED_METHODS:
        return HttpResponseNotAllowed(permitted_methods=PERMITTED_METHODS)

    form = RegisterForm(data=request.POST if request.method == "POST" else None)

    if request.method == "POST" and form.is_valid():
        email: str = form.cleaned_data["email"]
        password: str = form.cleaned_data["password"]
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(email=email, password_hash=hashed_password)

        return redirect(to="login")

    context = {"form": form}
    return render(
        request=request, template_name="accounts/register.html", context=context
    )
