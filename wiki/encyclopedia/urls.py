from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>", views.entry_page, name="entry_page"),
    path("search", views.search, name = "search"),
    path("create", views.create, name= "create"),
    path("wiki/<str:page_name>/edit", views.edit, name="edit"),
    path("/random", views.randoms, name="randoms")
]
