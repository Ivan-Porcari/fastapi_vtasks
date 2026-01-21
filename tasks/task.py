from fastapi import APIRouter, Body, status, HTTPException
from .models import Task

task_router = APIRouter() #creamos la instancia del router 
task_list = []

@task_router.get('/', status_code=status.HTTP_200_OK)
def get(): 
    return {"tasks" : task_list} #devolvemos la lista completa de listas

@task_router.post('/', status_code=status.HTTP_201_CREATED)     
def add(task: Task): #importamos directamente la clase Task

    if task in task_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = f'Task {task.name} have already exist')
    
    task_list.append(task)
    return {"tasks" : task_list}

@task_router.put('/',status_code=status.HTTP_200_OK) #el tipo de CRUD se especifica en la instancia
def update(index:int, task: Task = Body(
    openapi_examples= { #muy util a la hora de definir varios ejemplos de prueba
            "example1" : {
            "summary" : "first_example",
            "value" : {
                "id" : "1234",
                "name" : "prueba desde body",
                "description" : "prueba desde body",
                "tag" : ["tag3", "tag4", "tag5"]
            }
        },
            "example2" : {
            "summary" : "second_example",
            "value" : {
                "id" : "12345",
                "name" : "prueba desde body v2",
                "description" : "prueba desde body v2",
                "tag" : ["tag3", "tag4", "tag5 v2"]
            }
        }        
    }
    # examples = [
    #     {
    #         "id" : 74,
    #         "name" : "Studying",
    #         "description" : "A lot",
    #         "tag" : ["tag1,tag2"],
    #     },
    #     {
    #         "id" : 745,
    #         "name" : "Studying v2",
    #         "description" : "A lot v2",
    #         "tag" : ["tag1,tag2, tag3"],
    #     }
    # ]
)): 
        # task_list[index] = { #este esquema es util si hay que aplicar validaciones
    #     "task" : task.name,
    #     "status" : task.status,
    #     "description" : task.description 
    # }

    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = 'Task ID does not exist')

    task_list[index] = task
    return {"tasks" : task_list}

@task_router.delete('/', status_code=status.HTTP_200_OK)
def delete(index:int):

    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = 'Task ID does not exist')
    
    del task_list[index] 
    return {"tasks" : task_list}

