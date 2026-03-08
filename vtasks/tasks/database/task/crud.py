#una buena práctica sería que si tenemos cruds de varias instancias ir modulando los mismos en archivos diferentes
#otra buena práctica para ordenar es como importamos los paquetes, 1er orden fastapi, 2do orden terceros, 3ro imports propios de la app

from sqlalchemy.orm import Session

from tasks.database import models
from tasks.database.pagination import paginate, PageParams
from tasks.schemes import Task

def getById(id: int,db: Session):
    
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

def update(id: int, task: Task, db: Session):
    taskdb = getById(id, db)
    
    if taskdb is None:  # evita AttributeError
        return None
        
    taskdb.name = task.name
    taskdb.description = task.description
    taskdb.status = task.status
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

def delete(id: int, db: Session):
    taskdb = getById(id, db)
    
    if taskdb is None:  # evita AttributeError
        return None
        
    db.delete(taskdb)
    db.commit()

def pagination(page:int, size: int, db: Session):
    pageParams = PageParams()
    # pageParams.page = page
    # pageParams.size = size
    return paginate(pageParams , db.query(models.Task), Task)

