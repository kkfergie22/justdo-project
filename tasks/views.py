from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task
from django.views.generic.list import ListView


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "due_date", "status", "priority"]
    success_url = reverse_lazy("tasks")

    def form_validation(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task created successfully.")
        return super(CreateTask, self).form_validation(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "due_date", "status", "priority"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task updated successfully.")
        return super(UpdateTask, self).form_validation(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task Deleted successfully.")
        return super(DeleteTask, self).form_validation(form)
