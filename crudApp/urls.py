from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.todoView, name="home"),
    path("edit/<int:id>", views.updateTodoView, name="edit_todo"),
    path("delete/<int:id>", views.deleteTodoView, name="delete_todo"),
    path("completed/<int:id>", views.is_completedView, name="is_complete"),
]
