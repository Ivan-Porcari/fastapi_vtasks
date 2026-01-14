from enum import Enum
from pydantic import BaseModel, ValidationError, field_validator, Field, EmailStr, HttpUrl
from typing import Optional 

class StatusType(str, Enum): #creamos la clase con los valores disponibles      
    DONE = 'done'
    PENDING = 'pending'

class MyBaseModel(BaseModel):
    id: int = Field (gt=1, le=100) #si se puede resolver de esta manera mejor que con una función extensa

    @field_validator('id')
    def id_greather_than_zero(cls, v):
        if v <= 0:
            raise ValueError('must be greater than zero')
        return v
    
    @field_validator('id')
    def id_less_than_thousand(cls, v):
        if v >= 1000:
            raise ValueError('must be less than one thousand')
        return v


class Category(MyBaseModel):
    name: str


class User(MyBaseModel):
    name: str = Field (min_length=5) #a fines didactico realizo la practica de ponerle un minimo de 5 caracteres
    surname: str
    email: EmailStr  #utilizamos la validación de Field en este caso con EmailStr
    website: str #A modo de agilizar el testing vamos a comentar la clase HttpUrl


class Task(MyBaseModel): #anidamos las relaciones de task con category y user  
    name: str
    description: Optional[str] = Field ("No description",min_length=5)
    status: StatusType
    category : Category
    user : User

    @field_validator('name')
    def name_alphanumeric_and_whitespaces(cls, v):
        if v.replace(" ", "").isalnum(): 
            return v
        raise ValueError('must be alphanumeric')
    
