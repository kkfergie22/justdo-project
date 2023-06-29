from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from django.http import JsonResponse
from .forms import TaskForm
from django.utils import timezone
import requests
import datetime
from decouple import config


@login_required
def list_tasks(request):
    """Renders the task list"""
    tasks = Task.objects.all()
    form = TaskForm()
    xp = request.user.userprofile.xp
    context = {"tasks": tasks, "form": form, "xp": xp}
    return render(request, "tasks/task_list.html", context)


@login_required
def create_task(request):
    """Creates a new task"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.user = request.user
            task.save()
            print(task.user)
            messages.success(request, "Task created successfully.")
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {'form': form})


@login_required
def update_task(request, pk):
    """Updates an exisiting task"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_list.html', {'form': form})


@login_required
def delete_task(request, pk):
    """Renders the delete task form"""
    form = TaskForm()
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('tasks')


@login_required
def dashboard(request):
    """Renders the dashboard"""
    city = "Accra"
    # Weather API
    api_key = config("WEATHER_API_KEY")
    base_url = "https://api.openweathermap.org/data/3.0/onecall?lat=5.55&lon=-0.20&units=metric&exclude=hourly,minutely&appid={}"  # noqa
    city_weather = requests.get(base_url.format(api_key)).json()

    # Get the current weather
    current_weather = city_weather['current']
    current_day = datetime.datetime.fromtimestamp(current_weather['dt']).\
        strftime('%A')
    current_weather_context = {
        "city": city,
        "day": current_day,
        "temperature": round(current_weather['temp']),
        "main": current_weather['weather'][0]['main'],
        "description": current_weather['weather'][0]['description'],
        "icon": current_weather['weather'][0]['icon']
    }

    # Get the daily weather
    daily_weather = city_weather.get('daily', [])[1:]
    daily_forecast = []
    for day in daily_weather:
        date = day.get('dt')
        date_obj = datetime.datetime.fromtimestamp(date)
        day_of_week = date_obj.strftime('%A')
        icon = day.get('weather', [{}])[0].get('icon')
        temperature = round(day.get('temp', {}).get('day'))

        daily_forecast.append({
            'day': day_of_week,
            'icon': icon,
            'temperature': temperature
        })

    completed_tasks = request.session.get('completed_tasks', [])
    completed_tasks = [str(task_id) for task_id in completed_tasks]

    user_profile = request.user.userprofile
    xp = user_profile.xp

    task = Task.objects.all()
    completed = 0
    in_progress = 0
    not_started = 0
    due_today = 0

    for t in task:
        if t.due_date == timezone.now().date():
            due_today += 1
        if t.status == "C":
            completed += 1
        if t.status == "IP":
            in_progress += 1
        if t.status == "P":
            not_started += 1

    context = {
        "tasks": task,
        "completed_tasks": completed_tasks,
        "completed": completed,
        "in_progress": in_progress,
        "not_started": not_started,
        "due_today": due_today,
        "xp": xp,
        "current_weather": current_weather_context,
        "daily_weather": daily_forecast,
        }
    return render(request, "tasks/dashboard.html", context)


@login_required
def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.mark_completed()
    return JsonResponse({'status': 'success'})
