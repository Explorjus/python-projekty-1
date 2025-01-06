import requests
from bs4 import BeautifulSoup
import os
import subprocess
import tkinter
import customtkinter
import threading

def download_video():
    link = entry.get()
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
        process = subprocess.Popen([
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",  # Pobieranie najlepszej jakości wideo i audio
            "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
            link
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        file_size = 0
        last_progress = 0
        for line in process.stdout:
            print(line)  # Dodaj to, aby zobaczyć pełne wyjście
            if "[download]" in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if 'of' in part and 'MiB' in parts[i + 1]:
                        try:
                            file_size = float(parts[i + 1].replace('MiB', '')) * 1024 * 1024
                            print(f"Waga pliku: {file_size / (1024 * 1024):.2f} MB")
                        except ValueError:
                            continue
                    if '%' in part:
                        try:
                            progress = float(part.strip('%'))
                            if progress != last_progress:
                                last_progress = progress
                                bytes_pobrane = (progress / 100) * file_size
                                bytes_left = file_size - bytes_pobrane
                                speed = parts[i + 4] 
                                pPrecentage.configure(text=f"{progress}% {bytes_pobrane/(10**7):.2f}MB/{file_size/ (10**7):.2f} MB at {speed}")
                                progrssBar.set(progress / 100)
                                root.update_idletasks()  # Aktualizacja GUI
                                print(f"Pobrano: {bytes_pobrane / (1024 * 1024):.2f} MB, Pozostało: {bytes_left / (1024 * 1024):.2f} MB")
                        except ValueError:
                            continue
        
        process.wait()
        print("Ukończono")
        print("Gotowe")
    except Exception as e:
        print(f"An error occurred: {e}")

def start_download():
    threading.Thread(target=download_video).start()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Pobieranie z YouTube")

label = customtkinter.CTkLabel(root, text="Wpisz link do filmu z YouTube:")
label.pack(pady=10)

entry = customtkinter.CTkEntry(root, width=400)
entry.pack(pady=10)

pPrecentage = customtkinter.CTkLabel(root, text="0%")
pPrecentage.pack(pady=10)

progrssBar = customtkinter.CTkProgressBar(root, width=400)
progrssBar.set(0)
progrssBar.pack(pady=10, padx=10)

button = customtkinter.CTkButton(root, text="Pobierz", command=start_download)
button.pack(pady=20)

root.mainloop()