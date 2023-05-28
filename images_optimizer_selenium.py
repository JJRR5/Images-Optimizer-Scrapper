from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import zipfile

def unzip_most_recent_file(download_dir, dest_path):
    # Obtener todos los archivos en el directorio de descargas
    files = os.listdir(download_dir)

    # Filtrar solo los archivos zip
    zip_files = [file for file in files if file.endswith(".zip")]

    if not zip_files:
        raise Exception("No zip files found in download directory")

    # Obtener la ruta completa de los archivos zip
    zip_file_paths = [os.path.join(download_dir, file) for file in zip_files]

    # Obtener el archivo zip más reciente
    newest_zip_file = max(zip_file_paths, key=os.path.getmtime)

    # Descomprimir el archivo zip más reciente
    with zipfile.ZipFile(newest_zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)

def delete_files(file_paths):
    # Elimina cada archivo en la lista de file_paths
    for file_path in file_paths:
        if os.path.isfile(file_path):
            os.remove(file_path)

# Recuperamos los nombres de todos los archivos .jpg, .png, y .jpeg en el directorio actual
current_dir = os.getcwd()
file_names = os.listdir(current_dir)
file_extensions = ['.jpg', '.png', '.jpeg']
file_paths = [os.path.join(current_dir, file) for file in file_names if os.path.splitext(file)[1] in file_extensions]

# Aquí se especifica la ruta del driver de Chrome
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# Aquí se abre la URL
driver.get("https://compressimage.io/") 

# Se necesita tiempo para que la página cargue completamente. 
time.sleep(1) 

# Hacemos clic en el botón de configuración
settings_button = driver.find_element(By.ID, "settings_btn")
settings_button.click()
time.sleep(0.5) 

# Hacemos clic en el botón de configuración de imagen
image_settings_button = driver.find_element(By.CLASS_NAME, "switch")
try:
    image_settings_button.click()
except Exception as e:
    print(f"Error clicking image_settings_button: {e}")

# Aquí se encuentra el elemento input por su atributo class y se envían las rutas de los archivos
upload_input = driver.find_element(By.CLASS_NAME, "form_file_upload_field")
upload_input.send_keys('\n'.join(file_paths))

# Esperamos a que se carguen los archivos
time.sleep(len(file_paths) * 1.1) 

# Finalmente, hacemos clic en el div de descarga
download_zip = driver.find_element(By.CLASS_NAME, "file_download")
try:
    download_zip.click()
except Exception as e:
    print(f"Error clicking download_zip: {e}")

# Esperamos a que se descargue el archivo
time.sleep(2)

# Descomprimimos el archivo .zip más reciente
download_dir = "/home/vauxoo/Descargas"
unzip_most_recent_file(download_dir, current_dir)

# Eliminamos los archivos de imagen originales
delete_files(file_paths)

# Es buena práctica cerrar el driver al final
driver.quit()
