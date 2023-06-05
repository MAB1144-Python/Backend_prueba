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

routes_Conteo_Vehiculos = APIRouter()

@routes_Conteo_Vehiculos.post(
    path="/Conteo_Vehiculos",
    status_code=status.HTTP_200_OK,
    tags=["models"],
    summary="""Datos de Conteo de vehiculos.
    """
    )
async def Conteo_Vehiculos(sel_estacion: str,sel_sentido: str,sel_categoria: str,fecha_hora_ini: str,fecha_hora_fin: str):
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

    params = []
    if(sel_estacion != '' and len(params) == 0):
        select_query = select_query+'  WHERE estacion = ? '
        params.append(sel_estacion)
    elif(sel_sentido !='' and len(params) == 0):
        select_query = select_query+'  WHERE sentido = ? '
        params.append(sel_sentido)
    elif(sel_categoria !='' and len(params) == 0):
        select_query = select_query+'  WHERE categoria = ? '
        params.append(sel_categoria)



    if(sel_sentido !='' and len(params) != 0):
        select_query = select_query+'  AND sentido = ? '
        params.append(sel_sentido)
    if(sel_categoria !='' and len(params) != 0):
        select_query = select_query+'  AND categoria = ? '
        params.append(sel_categoria)

    try:    
        if(fecha_hora_ini != '' and len(params) == 0):
            fc = fecha_hora_ini.split("-")
            fecha = datetime.datetime(int(fc[0]), int(fc[1]), int(fc[2]), int(fc[3]),0,0)
            select_query = select_query+'  WHERE fecha_hora >= ? '
            params.append(fecha)
        elif(fecha_hora_ini != '' and len(params) != 0):
            fc = fecha_hora_ini.split("-")
            fecha = datetime.datetime(int(fc[0]), int(fc[1]), int(fc[2]), int(fc[3]),0,0)
            select_query = select_query+'  AND fecha_hora >= ? '
            params.append(fecha)  
    except:
        print('---')          
   
    try:
        if(fecha_hora_fin != '' and len(params) == 0):
            fc = fecha_hora_fin.split("-")
            fecha = datetime.datetime(int(fc[0]), int(fc[1]), int(fc[2]), int(fc[3]),0,0)
            select_query = select_query+'  WHERE fecha_hora <= ? '
            params.append(fecha)
        elif(fecha_hora_fin != '' and len(params) != 0):
            fc = fecha_hora_fin.split("-")
            fecha = datetime.datetime(int(fc[0]), int(fc[1]), int(fc[2]), int(fc[3]),0,0)
            select_query = select_query+'  AND fecha_hora <= ? '
            params.append(fecha) 
    except:
        print('---')          

    # Ejecutar la consulta y obtener los resultados
    print(select_query)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    if len(params) == 0:
        df = pd.read_sql_query(select_query, conn)  
    else:
        df = pd.read_sql_query(select_query, conn, params=params)  

    print(df)
    conteo_total = df.cantidad.sum()
    df.fecha_hora = df.fecha_hora.apply(lambda x: x.strftime('%Y-%m-%d, %H:%M:%S'))
    #'estacion', 'sentido', 'fecha_hora', 'categoria', 'valor_tabulado'
    query = f"SELECT COUNT(*) FROM Tabla_Conteo_Vehiculos"
    # Ejecutar la consulta SQL
    cursor = conn.cursor()
    cursor.execute(query)
    # Obtener el resultado de la consulta
    total_registros = cursor.fetchone()[0]
    # Consulta SQL para obtener el valor máximo de la columna
    query = f"SELECT MAX(fecha_hora) FROM Tabla_Conteo_Vehiculos"
    # Ejecutar la consulta SQL
    cursor = conn.cursor()
    cursor.execute(query)
    # Obtener el resultado de la consulta
    max_fecha = cursor.fetchone()[0]
    # Consulta SQL para obtener el valor minimo de la columna
    query = f"SELECT MIN(fecha_hora) FROM Tabla_Conteo_Vehiculos"
    # Ejecutar la consulta SQL
    cursor = conn.cursor()
    cursor.execute(query)
    # Obtener el resultado de la consulta
    min_fecha = cursor.fetchone()[0]
    print(max_fecha, min_fecha)

    # Ejecutar la consulta SQL
    cursor = conn.cursor()
    UQ_estacion = list(df.estacion.unique())
    UQ_sentido = df.sentido.unique()
    UQ_categoria = list(df.categoria.unique())
    # Cerrar la conexión
    conn.close()

    try:
        return {"n_registros":json.loads(pd.Series(total_registros).to_json(orient='values')),
                "fecha_max":json.loads(pd.Series([max_fecha.strftime('%Y'),max_fecha.strftime('%m'),max_fecha.strftime('%d'),max_fecha.strftime('%H')]).to_json(orient='values')),
                "fecha_min":json.loads(pd.Series([min_fecha.strftime('%Y'),min_fecha.strftime('%m'),min_fecha.strftime('%d'),min_fecha.strftime('%H')]).to_json(orient='values')),
                "UQ_estacion":json.loads(pd.Series(UQ_estacion).to_json(orient='values')),
                "UQ_sentido": json.loads(pd.Series(UQ_sentido).to_json(orient='values')),
                "UQ_categoria": json.loads(pd.Series(UQ_categoria).to_json(orient='values')),
                "Conteo_total": json.loads(pd.Series(conteo_total).to_json(orient='values')),
                "datos_conteo": json.loads(df.to_json(orient='records')),
        }
    except:
        return {"n_registros":json.loads(pd.Series(0).to_json(orient='values')),
                "fecha_max":json.loads(pd.Series(["0","0","0","0"]).to_json(orient='values')),
                "fecha_min":json.loads(pd.Series(["0","0","0","0"]).to_json(orient='values')),
                "UQ_estacion":json.loads(pd.Series(["0","0","0","0"]).to_json(orient='values')),
                "UQ_sentido": json.loads(pd.Series(["0","0","0","0"]).to_json(orient='values')),
                "UQ_categoria": json.loads(pd.Series(["0","0","0","0"]).to_json(orient='values')),
                "Conteo_total": json.loads(pd.Series(conteo_total).to_json(orient='values')),
                "datos_conteo": json.loads(df.to_json(orient='records')),       
        }