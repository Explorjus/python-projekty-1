from dotenv import load_dotenv
import os

load_dotenv("/Users/explorjus/Python_1/.gitignore/.env.py")

# Pobieranie kluczy z zmiennych środowiskowy
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

# Sprawdzanie, czy zmienne zostały załadowane poprawnie
print(f"API Key: {api_key}")
print(f"Secret Key: {secret_key}")