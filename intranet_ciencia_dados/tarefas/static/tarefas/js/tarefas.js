const status_select= document.querySelector("#status");
const tarefas = document.querySelector(".tarefas")


status_select.onchange = (event) =>{
    let option = status_select.selectedOptions[0].value
    let tarefas_on = document.querySelectorAll(`[status="${option}"]`);
    let tarefas_off = document.querySelectorAll(`[status]:not([status="${option}"])`);
    tarefas_on.forEach(tarefa => {
        tarefa.disabled = false;
    }); 
    
    tarefas_off.forEach(tarefa =>{
        tarefa.disabled = true;

    })
}
