# Script de Extracción de Datos de Wikipedia

## Descripción General

Este script automatiza la extracción de datos de Wikipedia utilizando Python y Selenium. El script realiza las siguientes tareas:
1. Inicia sesión en Wikipedia con las credenciales proporcionadas.
2. Extrae información sobre los estados mexicanos y sus datos de población.
3. Extrae información sobre los estados de EE.UU. y su etimología.
4. Guarda los datos extraídos en archivos Excel.

## Requisitos

- Python 3.6+
- Selenium
- WebDriver Manager
- pandas

## Configuración

1. Clonar el repositorio:
```sh
https://github.com/ErikRobles/webscrapingWiki.git
cd wikipedia-scraper
```
2. Crear y activar un entorno virtual:
```sh
python3 -m venv myenv
source myenv/bin/activate
```
3. Instalar las dependencias:
```sh
pip install -r requirements.txt
pip install webdriver-manager
```

4. Configurar variables de entorno para las credenciales de Wikipedia:
```sh
WIKIPEDIA_USERNAME=tu_usuario
WIKIPEDIA_PASSWORD=tu_contraseña
```
#### Ejecución del Script
Para ejecutar el script en Chrome:

```sh
python main.py
```
Para ejecutar el script en Firefox:

```sh
python main.py firefox
```
**Estructura del Proyecto**
* main.py: El script principal que ejecuta todo el proceso de extracción de datos.
* utils/: Contiene funciones de utilidad y configuración para WebDriver.
* data_extraction/: Contiene los módulos para extraer datos de Wikipedia.

**Solución de Problemas**

Si encuentras algún problema, asegúrate de que todas las dependencias estén instaladas correctamente y que las versiones de tu WebDriver sean compatibles con las versiones de tu navegador.

#### Licencia
Este proyecto está licenciado bajo la Licencia MIT.

Estructura del Proyecto
```arduino
wikipedia-scraper/
├── data_extraction/
│   ├── __init__.py
│   ├── extract_us_states.py
│   ├── login_wikipedia.py
│   ├── table_extraction.py
│   └── toponimia_extraction.py
├── utils/
│   ├── __init__.py
│   └── webdriver_setup.py
├── main.py
├── requirements.txt
├── README.md
└── .env
```

Version en Inglés

# Wikipedia Data Extraction Script

## Overview

This script automates the extraction of data from Wikipedia using Python and Selenium. The script performs the following tasks:
1. Logs into Wikipedia with provided credentials.
2. Extracts information about Mexican states and their population data.
3. Extracts information about US states and their etymology.
4. Saves the extracted data into Excel files.

## Requirements

- Python 3.6+
- Selenium
- WebDriver Manager
- pandas

## Setup

1. Clone the repository:
```sh
https://github.com/ErikRobles/webscrapingWiki.git
cd wikipedia-scraper
```
2. Create and activate a virtual environment:
```sh
python3 -m venv myenv
source myenv/bin/activate
```
3. Install the dependencies:
```sh
pip install -r requirements.txt
pip install webdriver-manager
```
4. Set up environment variables for Wikipedia credentials:
```sh
WIKIPEDIA_USERNAME=your_username
WIKIPEDIA_PASSWORD=your_password
```
### Running the Script
To run the script in Chrome:
```sh
python main.py
```
To run the script in Firefox:
```sh
python main.py firefox
```
#### Project Structure
* main.py: The main script that runs the entire data extraction process.
* utils/: Contains utility functions and setup for WebDriver.
* data_extraction/: Contains the modules for extracting data from Wikipedia.

#### Troubleshooting

If you encounter any issues, please ensure that all dependencies are installed correctly and that your WebDriver versions are compatible with your browser versions.

#### License
This project is licensed under the MIT License.

#### Project Structure
```arduino
wikipedia-scraper/
├── data_extraction/
│   ├── __init__.py
│   ├── extract_us_states.py
│   ├── login_wikipedia.py
│   ├── table_extraction.py
│   └── toponimia_extraction.py
├── utils/
│   ├── __init__.py
│   └── webdriver_setup.py
├── main.py
├── requirements.txt
├── README.md
└── .env
```

