import folium
from geopy.geocoders import Nominatim
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def show_location_on_map(city):
    try:
        # Inicjalizujemy geolokator
        geolocator = Nominatim(user_agent="location_finder")
        
        # Pobieramy współrzędne miasta
        location = geolocator.geocode(city)
        
        if location:
            print(f"Miasto: {location.address}")
            print(f"Szerokość geograficzna: {location.latitude}")
            print(f"Długość geograficzna: {location.longitude}")
            
            # Tworzymy mapę
            map_ = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
            
            # Zapisujemy mapę do pliku HTML
            map_filename = "map.html"
            map_.save(map_filename)
            
            # Otwieramy plik w domyślnej przeglądarce
            open_file_in_safari(map_filename)
        else:
            messagebox.showerror("Błąd", "Nie znaleziono lokalizacji.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

def open_file_in_safari(file_path):
    try:
        # Sprawdzamy, czy plik istnieje
        if not os.path.exists(file_path):
            print(f"Plik '{file_path}' nie istnieje.")
            return
        
        # Otwieramy plik w domyślnej przeglądarce
        subprocess.run(["open", file_path])
        print(f"Plik '{file_path}' został otwarty w domyślnej przeglądarce.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def on_search():
    city = entry.get()
    if city:
        show_location_on_map(city)
    else:
        messagebox.showwarning("Ostrzeżenie", "Proszę wpisać nazwę miasta.")

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Mapa Lokalizacji")

# Tworzymy etykietę i pole tekstowe
label = tk.Label(root, text="Wpisz nazwę miasta:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Tworzymy przycisk do wyszukiwania
button = tk.Button(root, text="Szukaj", command=on_search)
button.pack(pady=20)

# Uruchamiamy główną pętlę aplikacji
root.mainloop()