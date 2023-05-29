## 🖼️ Images-Optimizer-Scrapper 🕸️

Este es un script automatizado de Python que utiliza Selenium para interactuar con compressimage.io, un sitio web que permite comprimir y convertir imágenes a un formato más eficiente. Este script encuentra todas las imágenes en el directorio de trabajo actual con las extensiones .jpg, .png y .jpeg, las sube al sitio web, las comprime y las convierte al formato .webp, y luego las descarga automáticamente. Una vez que todas las imágenes han sido descargadas en su formato optimizado, el script reemplaza las imágenes originales con estas nuevas imágenes optimizadas.

## 💻 Requisitos

- Python 3.6 o superior
- Selenium
- webdriver_manager

Para instalar las dependencias de Python, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```


## ⚙️ Uso

Asegúrate de tener todas las imágenes que quieres comprimir en el directorio de trabajo actual.

Ejecuta el script de Python.

El script comprimirá automáticamente todas las imágenes utilizando el sitio web compressimage.io, las descargará en un archivo .zip, y las extraerá en el directorio de trabajo actual.

## 📝 Notas

Este script fue diseñado para automatizar el proceso de compresión de imágenes utilizando el sitio web compressimage.io. Por favor, asegúrate de respetar las políticas y condiciones del sitio web al utilizar este script.

## 📚 Referencias

- [Selenium](https://www.selenium.dev/)
- [webdriver_manager](https://pypi.org/project/webdriver_manager/)
- [compressimage.io](https://compressimage.io/)

## 👋 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir lo que te gustaría cambiar.
