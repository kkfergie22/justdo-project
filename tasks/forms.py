from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task title'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Task status'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Task priority'
            }),
        }
