# Inventory Management System

Este proyecto es un sistema de inventarios desarrollado en Python con FastAPI. Utiliza SQLAlchemy para la interacción con la
base de datos y Starlette para la configuración del entorno. El sistema permite la gestion de productos, categorias, y usuarios, ademas de los simples CRUD's de cada uno de estos, tambien posee funciones de busqueda, filtrado de productos y historial de cambios hechos en los productos. Por ultimo tambien tiene funciones para poder exportar todos los productos y productos con bajo stock a 3 tipos de formato, CSV, JSON y PDF.


## Requisitos

- Python 3.8+
- PostgreSQL 12+

## Instalación

1. Clonar el repositorio:
    
    ```bash
   git clone https://github.com/darioplazaleon/inventory-management.git
   cd inventory-management
    ```
2. Crear un entorno virtual e instalar las dependencias:
    
    ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
    ```
3. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:
    
    ```dotenv
   DATABASE_URL=postgresql://user:password@localhost/dbname
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
    ```

## Uso

1. Inicia la aplicacion:
   ```bash
    uvicorn app.main:app --reload
    ```
2. La aplicacion estara disponible en `http://localhost:8000/docs`. 

## Estructura del proyecto

- `app/`: Contiene el código fuente de la aplicación.
  - `core/`: Configuración de la aplicación. Incluida el manejo de JWT.
  - `db/`: Configuración de la base de datos. Conexion y creación de sesiones.
  - `models/`: Define los modelos de la base de datos.
  - `routers/`: Define las rutas de la aplicación.
  - `schemas/`: Define los esquemas de los modelos.
  - `utils/`: Varias funciones utilitarias para la aplicación.
- `.env`: Archivo de configuración de variables de entorno.
- `requirements.txt`: Lista de dependencias del proyecto.

## Funciones Principales

- **Productos**: CRUD de productos, busqueda y filtrado de productos, historial de cambios.
- **Categorias**: CRUD de categorias.
- **Usuarios**: Registro y cambio de ROLES.
- **Exportar**: Exportar todos los productos y productos con bajo stock a 3 tipos de formato, CSV, JSON y PDF.
- **Autenticación**: Autenticación de usuarios mediante JWT.
- **Autorización**: Protección de rutas mediante roles de usuario.
- **Documentación**: Documentación de la API con Swagger UI.

