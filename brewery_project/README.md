# Brewery Project

## Descripción

Este proyecto es una aplicación Django que consulta la API de Open Brewery DB para obtener una lista de cervecerías y muestra los datos en una tabla HTML utilizando Bootstrap para el diseño.

## Instalación

1. Clonar el repositorio y navegar a la carpeta del proyecto.
2. Crear un entorno virtual e instalar las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Aplicar migraciones y ejecutar el servidor de desarrollo:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

4. Navegar a `http://127.0.0.1:8000/` en tu navegador para ver la lista de cervecerías.

## API Utilizada

La aplicación utiliza la API de Open Brewery DB para obtener datos sobre cervecerías. La URL de la API es: https://api.openbrewerydb.org/v1/breweries
