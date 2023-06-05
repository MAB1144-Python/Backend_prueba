from fastapi import FastAPI
import os
import pyodbc
import pandas as pd
from contextvars import ContextVar
from fastapi import Depends
from pydantic import BaseSettings
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
from fastapi.routing import APIRouter
from route.route_Conteo_Vehiculos import routes_Conteo_Vehiculos
from route.route_Recaudo_Vehiculos import routes_Recaudo_Vehiculos
from route.route_Registro import routes_Registro
from route.route_Login import routes_login


app = FastAPI()
app.include_router(routes_Conteo_Vehiculos, prefix = "/datos")
app.include_router(routes_Recaudo_Vehiculos, prefix = "/datos")
app.include_router(routes_Registro, prefix = "/user")
app.include_router(routes_login, prefix = "/user")
# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
    "http://localhost:8000",
    # Agrega aquí los orígenes permitidos
]

# Agregar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

