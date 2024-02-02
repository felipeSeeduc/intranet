const status_select= document.querySelector("#status");
const tarefas = document.querySelector(".tarefas")
show_status()

status_select.onchange = show_status
function show_status () {
    let option = status_select.selectedOptions[0].value
    let tarefas_on = document.querySelectorAll(`[status="${option}"]`);
    let tarefas_off = document.querySelectorAll(`[status]:not([status="${option}"])`);
    tarefas_on.forEach(tarefa => {
        tarefa.style.display = "block";
    }); 
    
    tarefas_off.forEach(tarefa =>{
        tarefa.style.display = "none";

    })
}