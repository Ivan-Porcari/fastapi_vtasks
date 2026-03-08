from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/tasks" #el conectar va a emplear segun el modelo utilizado
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #utilizamos a sesion para hacer la conexión y realizar operaciones sobre la db

Base = declarative_base() #la utilizamos para crear modelos y tablas en base a ellos    

def get_database_session():
    try:
        db = SessionLocal()
        print("INIT DB")
        yield db #a diferencia del return cuando devolvemos este resultado lo que esté por debajo no se ejecuta
        #return db
    finally: #el finally siempre se va a ejecutar pero ahí muere la función cuando la función que envía la petición a la DB retorne su respuesta
        print("END DB")
        db.close()
