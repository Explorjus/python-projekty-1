import requests
from bs4 import BeautifulSoup
import os
import subprocess

link = str(input("Wpisz link do filmu z YouTube: "))
save_path = "/Users/explorjus/Muzyka"

# Upewnij się, że katalog docelowy istnieje
if not os.path.exists(save_path):
    os.makedirs(save_path)

try:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("meta", property="og:title")["content"]
    print(f"Tytuł: {title}")
    
    # Pobierz tylko strumień audio za pomocą yt-dlp
    audio_output_path = os.path.join(save_path, f"{title}.m4a")
    print("Pobieranie audio...")
    subprocess.run([
        "yt-dlp",
        "-f", "bestaudio",  # Pobierz najlepszą jakość audio
        "-o", audio_output_path,
        link
    ])
    
    # Konwertuj pobrany plik audio na MP3 za pomocą ffmpeg
    mp3_output_path = os.path.join(save_path, f"{title}.mp3")
    print("Konwertowanie do MP3...")
    subprocess.run([
        "ffmpeg", "-i", audio_output_path, "-q:a", "0", mp3_output_path
    ])
    
    # Usuń tymczasowy plik audio
    if os.path.exists(audio_output_path):
        os.remove(audio_output_path)
    
    print("Ukończono")
    print(f"Plik MP3 zapisany jako: {mp3_output_path}")
except Exception as e:
    print(f"An error occurred: {e}")