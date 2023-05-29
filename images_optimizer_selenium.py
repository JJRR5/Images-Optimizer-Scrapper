from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import zipfile


def unzip_most_recent_file(download_dir, dest_path):
    # Get all files in download directory
    files = os.listdir(download_dir)

    # Filter only zip files
    zip_files = [file for file in files if file.endswith(".zip")]

    if not zip_files:
        raise Exception("🕵️‍♀️ No zip files found in download directory.")

    # Get full path of zip files
    zip_file_paths = [os.path.join(download_dir, file) for file in zip_files]

    # Get the most recent zip file
    newest_zip_file = max(zip_file_paths, key=os.path.getmtime)

    # Unzip the most recent zip file
    with zipfile.ZipFile(newest_zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    print(f"📦 Unzipped the file {newest_zip_file}!")


def delete_files(file_paths):
    # Delete each file in the file_paths list
    for file_path in file_paths:
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("🗑️  Removed original files!")


# Get all .jpg, .png, .jpeg, and .avif file names in the current directory
current_dir = os.getcwd()
file_names = os.listdir(current_dir)
file_extensions = ['.jpg', '.png', '.jpeg', '.avif']
file_paths = [os.path.join(current_dir, file)
              for file in file_names if os.path.splitext(file)[1] in file_extensions]

if not file_paths:
    print("🕵️‍♀️ No images found in current directory.")
    exit()

print(f"🗂️ Found {len(file_paths)} images")

# Set Chrome driver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# Open the URL
driver.get("https://compressimage.io/")

# Give the page time to load
time.sleep(1)

# Click the settings button
settings_button = driver.find_element(By.ID, "settings_btn")
settings_button.click()
time.sleep(0.5)

# Click the image settings button
image_settings_button = driver.find_element(By.CLASS_NAME, "switch")
try:
    image_settings_button.click()
except Exception as e:
    print(f"⚠️ Error clicking image_settings_button: {e}")

# Find the input element by class attribute and send file paths
upload_input = driver.find_element(By.CLASS_NAME, "form_file_upload_field")
upload_input.send_keys('\n'.join(file_paths))

# Wait for files to be uploaded
print("🚀 Uploading your images... please wait!")
time.sleep(len(file_paths) * 1.1)

# Click the download div
download_zip = driver.find_element(By.CLASS_NAME, "file_download")
try:
    download_zip.click()
    print("💾 Downloading the optimized images...")
except Exception as e:
    print(f"⚠️ Error clicking download_zip: {e}")

# Wait for the download to complete
time.sleep(2)

# Unzip the most recent zip file
download_dir = "/home/vauxoo/Descargas"
unzip_most_recent_file(download_dir, current_dir)

# Delete the original image files
delete_files(file_paths)

# Close the driver at the end
driver.quit()

print(f"✨ Done!, {len(file_paths)} images optimized! ✨")
