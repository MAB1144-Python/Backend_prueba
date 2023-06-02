from fastapi import FastAPI
import os
import peewee
from peewee import *
from contextvars import ContextVar
from fastapi import Depends
import mysql.connector
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

app = FastAPI()


@app.get('/')
def home():

    # Connect to a MySQL database on network.
    #Base de datos
    Server = '23.102.103.53'
    Colección = 'BrayanMontenegro'
    Usuario = 'bmontenegroprueba'
    Contraseña = 'bmontenegroprueba'
    #mysql_db = MySQLDatabase(Colección, user=Usuario, password=Contraseña,host=Server, port=0)
    #mysql_db.connect()
    conexion = mysql.connector.connect(
        host = Server,
        port = 8080,
        user = Usuario,
        password = Contraseña,
    )
    cursor = conexion.cursor()
    #mysql_db._state = PeeweeConnectionState()
    #print()
    return {"message": "Hello World"}