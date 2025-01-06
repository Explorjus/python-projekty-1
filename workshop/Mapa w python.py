import folium
from geopy.geocoders import Nominatim
import os
import subprocess

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
            
            # Dodajemy znacznik na mapie
            folium.Marker(
                [location.latitude, location.longitude],
                popup=f"Lokalizacja: {location.address}",
                tooltip=city
            ).add_to(map_)
            
            # Zapisujemy mapę jako plik HTML
            map_.save("map.html")
            print("Mapa została zapisana jako 'map.html'. Otwórz plik w przeglądarce.")
        else:
            print("Nie znaleziono lokalizacji dla podanej miejscowości.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Wpisz miasto, które chcesz wyszukać
city = input("Podaj nazwę miejscowości: ")
show_location_on_map(city)


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

# Wpisz pełną ścieżkę do pliku, który chcesz otworzyć
file_path = "/Users/explorjus/Python_1/map.html"
open_file_in_safari(file_path)
