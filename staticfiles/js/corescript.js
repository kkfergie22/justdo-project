window.addEventListener('DOMContentLoaded', () => {
  const completedTasks = JSON.parse(localStorage.getItem('completedTasks')) || [];
  const taskCheckboxes = document.querySelectorAll('.task-checkbox');

  taskCheckboxes.forEach((checkbox) => {
    const taskId = checkbox.value;
    if (completedTasks.includes(taskId)) {
      checkbox.checked = true;
      checkbox.disabled = true;
      const taskItem = checkbox.closest('.task-item');
      taskItem.classList.add('is_completed');
    }
  });
});
