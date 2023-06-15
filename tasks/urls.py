from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="tasks"),
    path("create/", views.CreateTask.as_view(), name="create-task"),
    path("update/<int:pk>/", views.UpdateTask.as_view(), name="update-task"),
    path("delete/<int:pk>/", views.DeleteTask.as_view(), name="delete-task"),
]
