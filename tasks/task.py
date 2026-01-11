from fastapi import APIRouter, Body
from .models import StatusType

task_router = APIRouter() #creamos la instancia del router 
task_list = []

@task_router.get('/task')
def get(): 
    return {"tasks" : task_list} #devolvemos la lista completa de listas

@task_router.post('/') #quitamos el argumento para poder utilizar la clase Body    
def add(task:str = Body()): #al utilizar Body protegemos el path y la información viaja en el cuerpo de la petición
    task_list.append({
        'task' : task,
        'status' : StatusType.PENDING, #status por defecto como pendiente porque no tiene lógica agregar una tarea que se haya realizado segun el negocio
        })
    return {"tasks" : task_list}

@task_router.put('/') #el tipo de CRUD se especifica en la instancia
def update(index:int, task:str = Body(), status: StatusType = Body()): #este nombre se puede cambiar hace referencia a la función solamente
    task_list[index] = {
        "task" : task,
        "status" : status 
    }
    return {"tasks" : task_list}

@task_router.delete('/')
def delete(index:int):
    del task_list[index] 
    return {"tasks" : task_list}

