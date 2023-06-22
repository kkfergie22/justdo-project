from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, date


class TaskManager(models.Manager):
    def create_task(self, user, title, due_date, status,
                    priority):
        """
        Create a new task.

        Args:
            user (User): The user associated with the task.
            title (str): The title of the task.
            due_date (datetime): The due date of the task.
            status (str): The status of the task.
            priority (str): The priority of the task.

        Returns:
            Task: The created task.
        """

        try:
            user = User.objects.get(pk=user.pk)

        except ValueError as e:
            raise ValueError("Invalid user or category") from e

        created_on = timezone.now()
        last_updated_on = timezone.now()
        task = self.create(user=user, title=title,
                           due_date=due_date, status=status,
                           priority=priority, created_on=created_on,
                           last_updated_on=last_updated_on)
        return task

    def delete_task(self, task_id):
        """
        Delete a task.

        Args:
            task_id (int): The ID of the task to delete.
        """
        try:
            task = self.get(pk=task_id)
            task.delete()
        except ValueError as e:
            raise ValueError("Task not found.") from e

    def edit_task(self, task_id, title, due_date, status,
                  priority):
        """
        Edit an existing task.

        Args:
            task_id (int): The ID of the task to edit.
            title (str): The new title of the task.
            description (str): The new description of the task.
            due_date (date): The new due date of the task.
            status (str): The new status of the task.
            priority (str): The new priority of the task.

        Returns:
            Task: The edited task.
        """
        try:
            task = self.get(pk=task_id)
        except ValueError as e:
            raise ValueError("Task not found") from e

        task.title = title
        task.due_date = due_date
        task.status = status
        task.priority = priority
        task.last_updated_on = timezone.now()
        task.save()
        return task


class Task(models.Model):
    NOT_STARTED = 'P'
    COMPLETED = 'C'
    IN_PROGRESS = 'IP'

    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (COMPLETED, 'Completed'),
        (IN_PROGRESS, 'In Progress'),
    ]

    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES,
                              default=NOT_STARTED)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES,
                                default=LOW)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    objects = TaskManager()

    class Meta:
        ordering = ["due_date", "priority", "status", "-last_updated_on",
                    "-created_on"]
        verbose_name_plural = "Tasks"

    def __str__(self):
        """Return a string representation of the task"""
        return self.title

    def mark_completed(self):
        """
        Mark the task as completed and update user XP.
        """

        self.status = self.COMPLETED
        self.save()

        # Update user's XP
        base_xp = 20
        completion_time = self.due_date - date.today()
        one_day = timedelta(days=1)
        if completion_time < one_day:
            bonus_xp = 20
        elif completion_time < 2 * one_day:
            bonus_xp = 15
        else:
            bonus_xp = 5

        profile = self.user.userprofile
        profile.xp = base_xp + bonus_xp
        profile.save()

    def is_overdue(self):
        """
        Check if the task is overdue.

        Returns:
            bool: True if the task is overdue, False otherwise.
        """
        now = timezone.now().date()
        return self.due_date < now

    @property
    def created_by(self):
        """
        Get the user who created the task.

        Returns:
            User: The User object who created the task.
        """
        return self.user

    @property
    def days_until_due(self):
        """
        Get the number of days until the task is due.

        Returns:
            int: The number of days until the task is due.
        """
        now = timezone.now().date()
        time_until_due = self.due_date - now
        return time_until_due.days if time_until_due.days >= 0 else 0

    @property
    def is_high_priority(self):
        """
        Check if the task has high priority.

        Returns:
            bool: True if the task has high priority, False otherwise.
        """
        return self.priority == self.HIGH
