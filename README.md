# ETL Process for Largest Banks
This project implements an ETL (Extract, Transform, Load) process to compile a list of the top 10 largest banks in the world ranked by market capitalization. The code extracts data from a Wikipedia page, transforms the market capitalization values into different currencies (USD, GBP, EUR, INR) using exchange rates from a CSV file, and saves the processed data both as a CSV file and in an SQLite database. The progress of each step is logged for tracking purposes.
## Features
- **Data Extraction**: Scrapes bank data from a specified Wikipedia page.
- **Data Transformation**: Converts market capitalization values to various currencies.
- **Data Loading**: Saves the transformed data to CSV and SQLite database.
- **Logging**: Tracks progress throughout the ETL process for transparency.
## Technologies Used
- Python
- BeautifulSoup
- Pandas
- SQLite
- Requests
- NumPy
### Acknowledgments
This project was inspired by the "Data Engineering" course by IBM on Coursera. The concepts and techniques used in this script were learned through this course.

# Proceso ETL para los Bancos Más Grandes
Este proyecto implementa un proceso ETL (Extracción, Transformación, Carga) para compilar una lista de los 10 bancos más grandes del mundo clasificados por capitalización de mercado. El código extrae datos de una página de Wikipedia, transforma los valores de capitalización de mercado a diferentes monedas (USD, GBP, EUR, INR) utilizando tasas de cambio de un archivo CSV, y guarda los datos procesados tanto en un archivo CSV como en una base de datos SQLite. El progreso de cada paso se registra para fines de seguimiento.
## Características
- **Extracción de Datos**: Obtiene datos de bancos de una página de Wikipedia específica.
- **Transformación de Datos**: Convierte los valores de capitalización de mercado a varias monedas.
- **Carga de Datos**: Guarda los datos transformados en CSV y en una base de datos SQLite.
- **Registro**: Realiza un seguimiento del progreso durante todo el proceso ETL para mayor transparencia.
## Tecnologías Utilizadas
- Python
- BeautifulSoup
- Pandas
- SQLite
- Requests
- NumPy
 ### Agradecimientos
Este proyecto fue inspirado por el curso "Data Engineering" de IBM en Coursera. Los conceptos y técnicas utilizados en este script fueron aprendidos a través de este curso.
