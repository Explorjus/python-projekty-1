import folium
from geopy.geocoders import Nominatim
import os
import subprocess
import requests
from dotenv import load_dotenv
import tkinter
import customtkinter

# api z ukrytego pliku .env
load_dotenv("/Users/explorjus/Python_1/.gitignore/.env.py")

api = os.getenv("API_KEY")

# funkcja do sugestii miast
def suggest_cities(user_input, api_key):
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": user_input,
        "types": "geocode",  
        "key": api_key,
        "language": "pl"    
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
        
        geolocator = Nominatim(user_agent="location_finder")
        
        
        location = geolocator.geocode(city)
        
        if location:
            print(f"Miasto: {location.address}")
            print(f"Szerokość geograficzna: {location.latitude}")
            print(f"Długość geograficzna: {location.longitude}")
            
            
            map_ = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
            
            
            folium.Marker(
                [location.latitude, location.longitude],
                popup=f"Lokalizacja: {location.address}",
                tooltip=city
            ).add_to(map_)
            
            
            map_.save("map.html")
            print("Mapa została zapisana jako 'map.html'. Otwórz plik w przeglądarce.")
        else:
            print("Nie znaleziono lokalizacji dla podanej miejscowości.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")




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
        
        if not os.path.exists(file_path):
            print(f"Plik '{file_path}' nie istnieje.")
            return
        
       
        subprocess.run(["open", file_path])
        print(f"Plik '{file_path}' został otwarty w domyślnej przeglądarce.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# ścieka do pliku map.html
file_path = "/Users/explorjus/Python-projekty/map.html"
open_file_in_safari(file_path)

