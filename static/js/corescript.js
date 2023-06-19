function getCookie(name) {
  const cookieValue = document.cookie
    .split(';')
    .map((cookie) => cookie.split('='))
    .find((cookie) => cookie[0].trim() === name);

  if (cookieValue) {
    return decodeURIComponent(cookieValue[1]);
  }

  return null;
}

// Attach event listener to checkboxes
const checkboxes = document.querySelectorAll('.task-checkbox');
checkboxes.forEach((checkbox) => {
  checkbox.addEventListener('change', function () {
    const taskId = this.dataset.taskId;
    const isChecked = this.checked;

    // Make AJAX request to update task status
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/tasks/update_status/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Task status updated successfully
        console.log('Task status updated');
      }
    };

    xhr.send(
      JSON.stringify({
        task_id: taskId,
        is_checked: isChecked,
      })
    );
  });
});
