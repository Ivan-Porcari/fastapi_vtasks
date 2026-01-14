from fastapi import APIRouter, Body
from .models import Task

task_router = APIRouter() #creamos la instancia del router 
task_list = []

@task_router.get('/task')
def get(): 
    return {"tasks" : task_list} #devolvemos la lista completa de listas

@task_router.post('/')     
def add(task: Task): #importamos directamente la clase Task
    task_list.append(task)
    return {"tasks" : task_list}

@task_router.put('/') #el tipo de CRUD se especifica en la instancia
def update(index:int, task: Task): 
        # task_list[index] = { #este esquema es util si hay que aplicar validaciones
    #     "task" : task.name,
    #     "status" : task.status,
    #     "description" : task.description 
    # }
    task_list[index] = task
    return {"tasks" : task_list}

@task_router.delete('/')
def delete(index:int):
    del task_list[index] 
    return {"tasks" : task_list}

