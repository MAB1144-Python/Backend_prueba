from fastapi import status
from fastapi.routing import APIRouter
from fastapi import Depends
import os
from dotenv import load_dotenv
import pyodbc
import json
import pandas as pd


load_dotenv()

routes_Recaudo_Vehiculos = APIRouter()

@routes_Recaudo_Vehiculos.post(
    path="/Recaudo_Vehiculos",
    status_code=status.HTTP_200_OK,
    tags=["models"],
    summary="""Datos de Conteo de vehiculos.
    """
    )
async def Recaudo_Vehiculos():
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
    select_query = "SELECT * FROM Tabla_Recaudo_Vehiculos"

    # Ejecutar la consulta y obtener los resultados
    df = pd.read_sql_query(select_query, conn)    
    print(df.keys())
    df.fecha_hora = df.fecha_hora.apply(lambda x: x.strftime('%Y-%m-%d, %H:%M:%S'))
    #'estacion', 'sentido', 'fecha_hora', 'categoria', 'valor_tabulado'
    UQ_estacion = df.estacion.unique()

    # Cerrar la conexión
    conn.close()
    return {"UQ_estacion":UQ_estacion,
            "UQ_sentido":"",
            "UQ_categoria":"",
            "datos_Recaudo_Vehiculos": json.loads(df.to_json(orient='records')),}