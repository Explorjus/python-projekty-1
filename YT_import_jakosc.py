import requests
from bs4 import BeautifulSoup
import os
import subprocess
import json

link = str(input("Enter the link of the video: "))
save_path = "/Users/explorjus/Wideo"

# Upewnij się, że katalog docelowy istnieje
if not os.path.exists(save_path):
    os.makedirs(save_path)

try:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("meta", property="og:title")["content"]
    print(f"Title: {title}")
    
    # Wyświetl dostępne formaty wideo
    print("Fetching available formats...")
    result = subprocess.run([
        "yt-dlp",
        "-F", link
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"An error occurred while fetching formats: {result.stderr}")
        exit(1)
    
    print(result.stdout)
    
    # Poproś użytkownika o wybór formatu
    format_code = str(input("Enter the format code you want to download: "))
    
    print("Downloading in the selected quality...")
    result = subprocess.run([
        "yt-dlp",
        "-f", format_code,  # Pobierz wybrany format
        "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
        link
    ])
    
    if result.returncode == 0:
        print("Finished downloading")
        print("Ready to go")
    else:
        print(f"An error occurred: {result.stderr}")
except Exception as e:
    print(f"An error occurred: {e}")