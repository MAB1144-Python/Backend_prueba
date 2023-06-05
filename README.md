# Backend prueba tecnica - README
## Mgs. Brayan Andru Montenegro Embus

Este es un breve tutorial para ejecutar un proyecto en FastAPI utilizando un entorno virtual en Python.

## Requisitos previos
Asegúrate de tener instalado lo siguiente en tu sistema:
- Python (preferiblemente la versión 3.6+)
- pip (el gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado para crear entornos virtuales)

## Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/MAB1144-Python/Backend_prueba.git
```

### 2. Crear un entorno virtual (opcional)

Cambiate al directorio del proyecto:

```
cd Backend_prueba
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

Cambiate al directorio del proyecto:

```
cd API
```

### 5. Ejecutar el servidor FastAPI

Una vez que las dependencias estén instaladas y la configuración esté lista, puedes ejecutar el servidor FastAPI:

```
uvicorn main:app --reload
```

Esto iniciará el servidor FastAPI en modo de desarrollo, y cualquier cambio que realices en los archivos se reflejará automáticamente sin tener que reiniciar el servidor manualmente.

### 6. Acceder a la API

El servidor FastAPI estará disponible en `http://127.0.0.1:8000` por defecto. Puedes acceder a la API utilizando tu navegador o cualquier otra herramienta de prueba de API, como cURL o Postman.

Puedes utilizar las rutas tambien entrando a `http://127.0.0.1:8000/docs`

si persiste algun problema puede comunicarse conmigo al 3175750088
