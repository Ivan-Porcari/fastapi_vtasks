from enum import Enum

class StatusType(str, Enum): #creamos la clase con los valores disponibles      
    DONE = 'done'
    PENDING = 'pending'