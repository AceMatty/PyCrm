function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function EditCase(ind) {
    let nameBox = document.getElementById('nameBox'+ind)
    let descBox = document.getElementById('descBox'+ind)
    let req = "/crm/editCase?id="+ind+"&name="+nameBox.value+"&desc="+descBox.value
    let xhr = new XMLHttpRequest();
    xhr.open("POST",req,true)
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken') );
    xhr.send()
}