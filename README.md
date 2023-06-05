# FastAPI - README

Este es un breve tutorial para ejecutar un proyecto en FastAPI utilizando un entorno virtual en Python.

## Requisitos previos
Asegúrate de tener instalado lo siguiente en tu sistema:
- Python (preferiblemente la versión 3.6+)
- pip (el gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado para crear entornos virtuales)

## Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/tu_usuario/tu_proyecto.git
```

### 2. Crear un entorno virtual (opcional)

Cambiate al directorio del proyecto:

```
cd tu_proyecto
```

Crea un entorno virtual:

```
python -m venv venv
```

Activa el entorno virtual:

- En Windows:

```
venv\Scripts\activate
```

- En macOS/Linux:

```
source venv/bin/activate
```

### 3. Instalar las dependencias

Una vez que el entorno virtual está activado, instala las dependencias del proyecto utilizando `pip`:

```
pip install -r requirements.txt
```

Esto instalará todas las librerías necesarias para ejecutar el proyecto.

### 4. Configurar la base de datos

Si tu proyecto utiliza una base de datos, asegúrate de configurarla adecuadamente. Puedes editar el archivo de configuración `config.py` o cualquier otro archivo de configuración relevante en tu proyecto.

### 5. Ejecutar el servidor FastAPI

Una vez que las dependencias estén instaladas y la configuración esté lista, puedes ejecutar el servidor FastAPI:

```
uvicorn main:app --reload
```

Esto iniciará el servidor FastAPI en modo de desarrollo, y cualquier cambio que realices en los archivos se reflejará automáticamente sin tener que reiniciar el servidor manualmente.

### 6. Acceder a la API

El servidor FastAPI estará disponible en `http://localhost:8000` por defecto. Puedes acceder a la API utilizando tu navegador o cualquier otra herramienta de prueba de API, como cURL o Postman.

¡Y eso es todo! Ahora deberías poder ejecutar y utilizar tu proyecto FastAPI con un entorno virtual en Python.