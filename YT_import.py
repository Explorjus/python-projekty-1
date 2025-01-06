import requests
from bs4 import BeautifulSoup
import os
import subprocess
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1980x1080")
app.title("YT Import")

title = customtkinter.CTkLabel(app, text="Wprowadz link do filmu z YouTube", font=("Arial", 20))
title.pack(pady=10, padx=10)

link = customtkinter.CTkEntry(app, width=350, height=50)
link.pack()
app.mainloop()

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
