
# Guía de Inicio Rápido para Reservas de Citas para Universidad

Este documento proporciona instrucciones para configurar y ejecutar el proyecto de Reservas de Citas para Universidad en tu entorno local.

## Requisitos Previos

- Python 3.x instalado en tu sistema.
- PIP (Python Package Installer) para instalar las dependencias.

## Configuración del Entorno Virtual

1. Abre una terminal en la carpeta raíz del proyecto.

2. Crea un entorno virtual (virtual environment) utilizando `venv` o `virtualenv`. Ejemplo usando `venv`:

   ```bash
   python -m venv env
   ```
    **Nota**: Si no funciona `python` probar con `py`.


3. Activa el entorno virtual:

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En macOS y Linux:

  ```
  source venv/bin/activate
  ```

## Instalación de Dependencias

1. Asegúrate de estar en el entorno virtual activado.

2. Ejecuta el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

```
pip install -r requirements.txt
```


## Creación de la Base de Datos

1. Crea la base de datos con el nombre `reservas_citas_universidad`


## Inicialización del Programa

1. Asegúrate de estar en el entorno virtual activado.

2. Ejecuta el archivo `run.py` para iniciar la aplicación:

```
python run.py
```
`o`
```
py run.py
```


La aplicación ahora debería estar en funcionamiento y podrás acceder a ella en tu navegador web en la dirección `http://localhost:5000`.

**Nota:** *Si no estan creadas las tablas.*  Se crean automaticamente al iniciar el programa.

---
