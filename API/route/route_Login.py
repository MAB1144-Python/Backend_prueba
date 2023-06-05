from fastapi import status
from fastapi.routing import APIRouter
from fastapi import Depends
import os
from dotenv import load_dotenv
import pyodbc
import json
import pandas as pd
import datetime


load_dotenv()

routes_login = APIRouter()

@routes_login.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    tags=["models"],
    summary="""Datos de Conteo de vehiculos.
    """
    )
async def login(username: str,password: str):
    print("entro", username)
    
    conn = pyodbc.connect('Driver={SQL Server};'+
                        'Server=23.102.103.53;'+
                        'Database=BrayanMontenegro;'+
                        'UID=bmontenegroprueba;'+
                        'PWD=bmontenegroprueba;'
                        )

    # Creación de la tabla
    #estacion VARCHAR(50),sentido VARCHAR(50),fecha_hora TIME,cantegoria VARCHAR(50),cantidad INT

    if(True):# try:
        # Consulta para obtener todos los datos de la tabla
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Tabla_Usuarios  WHERE username = ? AND password = ?",
                   [username, password])
        count = cursor.fetchone()[0]
        cursor.close()
        print(count)
        
        #df = pd.read_sql_query(select_query, conn, params=params)  

        #print(df)
        # Confirmar los cambios
        conn.commit()

        # Cerrar la conexión
        conn.close()
        return {"username":json.loads(pd.Series(username).to_json(orient='values')),
                "token": json.loads(pd.Series("a1b2c3d4e5f6").to_json(orient='values'))         
        }
    """except:
        return {"username":json.loads(pd.Series("Error de login").to_json(orient='values')),
                "token": json.loads(pd.Series("").to_json(orient='values'))     
        }"""