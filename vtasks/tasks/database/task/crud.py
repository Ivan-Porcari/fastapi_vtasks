#una buena práctica sería que si tenemos cruds de varias instancias ir modulando los mismos en archivos diferentes
#otra buena práctica para ordenar es como importamos los paquetes, 1er orden fastapi, 2do orden terceros, 3ro imports propios de la app

from sqlalchemy.orm import Session

from tasks.database import models
from tasks.schemes import Task

def getById(db: Session, id: int):
    
    # task = db.query(models.Task).filter(models.Task.id == id).first()
    task = db.query(models.Task).get(id)
    return task

def getAll(db: Session):
    
    # task = db.query(models.Task).filter(models.Task.id == id).first()
    tasks = db.query(models.Task).all()
    return tasks

def create(task: Task, db: Session):
    taskdb = models.Task(name = task.name, description = task.description, status = task.status)
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

