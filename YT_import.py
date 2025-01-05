import requests
from bs4 import BeautifulSoup
import os
import subprocess

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
    
    print("Downloading in the best quality...")
    subprocess.run([
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",  # Pobieranie najlepszej jakości wideo i audio
        "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
        link
    ])
    print("Finished downloading")
    print("Ready to go")
except Exception as e:
    print(f"An error occurred: {e}")
