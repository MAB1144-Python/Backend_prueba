from fastapi import status
from fastapi.routing import APIRouter
from fastapi import Depends
import os
from dotenv import load_dotenv
import pyodbc
import json
import pandas as pd


load_dotenv()

routes_Conteo_Vehiculos = APIRouter()

@routes_Conteo_Vehiculos.post(
    path="/Conteo_Vehiculos",
    status_code=status.HTTP_200_OK,
    tags=["models"],
    summary="""Datos de Conteo de vehiculos.
    """
    )
async def Conteo_Vehiculos():
    print("entro")
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
    df.fecha_hora = df.fecha_hora.apply(lambda x: x.strftime('%Y-%m-%d, %H:%M:%S'))
    print(df.fecha_hora)

    # Cerrar la conexión
    conn.close()
    return {"datos_Conteo_Vehiculos": json.loads(df.to_json(orient='records'))}