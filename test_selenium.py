from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

try:
    # Recibir el DNI desde la línea de comandos
    dni_input = sys.argv[1]

    # Configurar Chrome para ejecutarse sin ventana gráfica
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Inicializa el controlador del navegador Chrome en este caso
    driver = webdriver.Chrome(options=chrome_options)

    # Abre la página web
    driver.get('https://eldni.com/pe/buscar-datos-por-dni')

    time.sleep(2)

    # Encuentra el campo del DNI por su ID e ingresa el valor recibido
    dni_field = driver.find_element(By.ID, 'dni')
    dni_field.send_keys(dni_input)

    # Encuentra y clickea el boton de busqueda
    search_button = driver.find_element(By.ID, 'btn-buscar-datos-por-dni')
    search_button.click()

    time.sleep(5)

    # localizamos los datos dentro de la tabla
    dni_value = driver.find_element(By.XPATH, '//table/tbody/tr/td[1]').text
    nombres = driver.find_element(By.XPATH, '//table/tbody/tr/td[2]').text
    apellido_paterno = driver.find_element(By.XPATH, '//table/tbody/tr/td[3]').text
    apellido_materno = driver.find_element(By.XPATH, '//table/tbody/tr/td[4]').text

    # Asignar los datos a variables
    nombre_completo = f"{nombres} {apellido_paterno} {apellido_materno}"

    # Imprimir los valores esto será capturado por el script PHP
    print(f"DNI: {dni_value}")
    print(f"Nombres: {nombres}")
    print(f"Apellido Paterno: {apellido_paterno}")
    print(f"Apellido Materno: {apellido_materno}")
    print(f"Nombre Completo: {nombre_completo}")

    # Cerrar el navegador
    driver.quit()

except Exception as e:
    # Imprimir el error para poder depurarlo desde el script PHP
    print(f"Error: {str(e)}")
