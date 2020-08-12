function createTask(case_id) {
    let nameBox = document.getElementById('nameBox')
    let descBox = document.getElementById('descBox')
    let cmb = document.getElementById('cmb')
    let dateBox = document.getElementById('dateBox')
    alert(cmb.value)
    if (nameBox.value !== ""){
        let req = "/crm/createTask?id="+case_id+"&name="+nameBox.value+"&desc="+descBox.value+"&cmd="+cmb.value+"&date="+dateBox.value;
        let xhr = new XMLHttpRequest();
        xhr.open("POST",req,true)
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken') );
        xhr.send()

    }
}