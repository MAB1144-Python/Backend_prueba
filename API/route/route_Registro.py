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

routes_Registro = APIRouter()

@routes_Registro.post(
    path="/Registro",
    status_code=status.HTTP_200_OK,
    tags=["models"],
    summary="""Registro de usuarios.
    """
    )
async def Registro(username: str,first_name: str,last_name: str,cellphone: str,email: str,password: str,born_date: str):
    print("entro", username)
    
    conn = pyodbc.connect('Driver={SQL Server};'+
                        'Server=23.102.103.53;'+
                        'Database=BrayanMontenegro;'+
                        'UID=bmontenegroprueba;'+
                        'PWD=bmontenegroprueba;'
                        )

    # Creación de la tabla
    #estacion VARCHAR(50),sentido VARCHAR(50),fecha_hora TIME,cantegoria VARCHAR(50),cantidad INT
    cursor = conn.cursor()
    params = [username,first_name,last_name,cellphone,email,password,born_date]

    try:
        # Consulta para obtener todos los datos de la tabla
        select_query = "INSERT INTO Tabla_Usuarios (username, first_name, last_name, cellphone, email, password, born_date) VALUES (?, ?, ?, ?, ?, ?, ?)"
        
        df = pd.read_sql_query(select_query, conn, params=params)  

        print(df)
        # Confirmar los cambios
        conn.commit()

        # Cerrar la conexión
        conn.close()
        return {"usuario":json.loads(pd.Series("Registro exitoso").to_json(orient='values'))   
        }
    except:
        return {"usuario":json.loads(pd.Series("Error de registro").to_json(orient='values'))
        }