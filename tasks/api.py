from fastapi import FastAPI, APIRouter, Query, Path
from tasks.task import task_router #path absoluto 
#from .task import task_router con el . delante de la importación le decimos que es relativo dentro del proyect path

app = FastAPI() #creación de la instancia 

router = APIRouter()

@router.get('/hello') #decorador / route / access
def hello_world(): #función 
    return {"hello": "World"}

@app.get("/e_page")
def page(page:int = Query(1, ge = 1, le = 20, title ="Esta es la pagina que quieres ver"), size : int = Query(5, ge = 5, le = 20, title = "Cuantos registros por pagina")): #valor por defecto es 1
    #size = cantidad de registros por pagina, estos argumentos viajan por la query string
    return { "page" : page, "size" : size}

@app.get("/e_phone") # +34 111 12-34-56 ejemplo de expresión regular para normalizar entradas
def phone(phone: str = Query(pattern=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$" )):
 return {"phone": phone}

@app.get("/ep_phon/{phone}") # Con path hacemos lo mismo pero lo indicamos por URL 
def phone(phone: str = Path(pattern=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$" )):
 return {"phone": phone}


app.include_router(router) #indicamos las rutas que queremos incluir dentro de app
app.include_router(task_router, prefix='/tasks') #prefijo para aclarar la raíz de las rutas