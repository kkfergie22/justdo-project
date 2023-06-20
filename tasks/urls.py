from django.urls import path
from . import views

urlpatterns = [
    path("mark-completed/<int:pk>/", views.mark_completed, name="mark-complete"),  # noqa
    path("", views.list_tasks, name="tasks"),
    path("create/", views.create_task, name="create-task"),
    path("<int:pk>/update/", views.update_task, name="update-task"),
    path("<int:pk>/delete/", views.delete_task, name="delete-task"),
    path("dashboard/", views.dashboard, name="dashboard"),
    ]
