function deleteTask(task_id) {
  let req = "/crm/deleteTask?task_id="+task_id;
  let xhr = new XMLHttpRequest();
  xhr.open("POST",req,true)
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken') );
  xhr.send()

}