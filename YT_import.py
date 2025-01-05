import requests
from bs4 import BeautifulSoup
import os
import subprocess

link = str(input("Wpisz link do filu z youtube: "))
save_path = "/Users/explorjus/Wideo"

# Upewnij się, że katalog docelowy istnieje
if not os.path.exists(save_path):
    os.makedirs(save_path)

try:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("meta", property="og:title")["content"]
    print(f"Tytuł: {title}")
    
    print("Pobieranie...")
    subprocess.run([
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",  # Pobieranie najlepszej jakości wideo i audio
        "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
        link
    ])
    print("Ukończono")
    print("Gotowe")
except Exception as e:
    print(f"An error occurred: {e}")
