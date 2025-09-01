from fastapi import APIRouter
from enum import Enum


task_router = APIRouter()
task_list = []

class StatusType(str, Enum):
    DONE = 'done'
    PENDING = 'pending'
    

@task_router.get('/task')
def get():
    return {"tasks" : task_list}

@task_router.post('/{task}')
def add(task:str):
    task_list.append({
        'task' : task,
        'status' : StatusType.PENDING, #status por defecto como pendiente porque no tiene lógica agregar una tarea que se haya realizado segun el negocio
        })
    return {"tasks" : task_list}

@task_router.put('/')
def update(index:int, task:str, status: StatusType):
    task_list[index] = {
        "task" : task,
        "status" : status
    }
    return {"tasks" : task_list}

@task_router.delete('/')
def delete(index:int):
    del task_list[index] 
    return {"tasks" : task_list}

