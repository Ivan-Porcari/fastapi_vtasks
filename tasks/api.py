from fastapi import FastAPI, APIRouter
from task import task_router #con el . delante de la importación le decimos que es relativo dentro del proyect path


app = FastAPI() #creación de la instancia 

router = APIRouter()

@router.get('/hello') #decorador / route / access
def hello_world(): #función 
    return {"hello": "World"}


app.include_router(router)
app.include_router(task_router, prefix='/tasks') #prefijo para aclarar la raíz de las rutas