from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.Index.as_view(), name="index"),
    path(route="create", view=views.Create.as_view(), name="create"),
]
