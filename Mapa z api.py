import folium
from geopy.geocoders import Nominatim
import os
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv("/Users/explorjus/Python_1/.gitignore/.env.py")

api = os.getenv("API_KEY")


# Funkcja sugerująca miasta z Google Places API
def suggest_cities(user_input, api_key):
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": user_input,
        "types": "geocode",  # Wyszukiwanie geograficzne
        "key": api_key,
        "language": "pl"    # Język wyników (polski)
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        predictions = response.json().get("predictions", [])
        return [prediction["description"] for prediction in predictions]
    else:
        print(f"Błąd API: {response.status_code}")
        return []

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

# Twój klucz API Google Places  # Wprowadź tutaj swój klucz API

# Pobieranie nazwy miasta z sugestiami
while True:
    user_input = input("Podaj nazwę miejscowości (lub jej fragment): ")
    suggestions = suggest_cities(user_input, api)
    
    if suggestions:
        print("Propozycje miast:")
        for idx, suggestion in enumerate(suggestions, start=1):
            print(f"{idx}. {suggestion}")
        
        try:
            choice = int(input("Wybierz miasto z listy (podaj numer) lub wpisz ponownie: "))
            if 1 <= choice <= len(suggestions):
                city = suggestions[choice - 1]
                print(f"Wybrano miasto: {city}")
                break
        except ValueError:
            print("Niepoprawny wybór. Spróbuj ponownie.")
    else:
        print("Brak sugestii. Spróbuj wpisać ponownie.")

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

