from fastapi import FastAPI
import os
import pyodbc
import pandas as pd
from contextvars import ContextVar
from fastapi import Depends
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get('/Conteo_Vehiculos')
def home():
    conn = pyodbc.connect('Driver={SQL Server};'+
                        'Server=23.102.103.53;'+
                        'Database=BrayanMontenegro;'+
                        'UID=bmontenegroprueba;'+
                        'PWD=bmontenegroprueba;'
                        )

    # Creación de la tabla
    #estacion VARCHAR(50),sentido VARCHAR(50),fecha_hora TIME,cantegoria VARCHAR(50),cantidad INT
    cursor = conn.cursor()
    # Consulta para obtener todos los datos de la tabla
    select_query = "SELECT * FROM Tabla_Conteo_Vehiculos"

    # Ejecutar la consulta y obtener los resultados
    df = pd.read_sql_query(select_query, conn)

    # Cerrar la conexión
    conn.close()
    return {"message": df.to_json(orient='records')}