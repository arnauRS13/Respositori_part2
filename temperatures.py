import requests
import json
from datetime import datetime

def obtenir_temperatures(latitud, longitud):
    """
    Obte les temperatures horaries d'una ubicacio utilitzant l'API open-meteo.com.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["hourly"]["temperature_2m"]

def calcular_estadistiques(temperatures):
    """
    Calcula la temperatura maxima minima i mitjana d'una llista de temperatures.
    """
    maxim = max(temperatures)
    minim = min(temperatures)
    mitjana = sum(temperatures) / len(temperatures)
    return maxim, minim, mitjana

def exportar_a_json(maxim, minim, mitjana, nom_fitxer):
    """
    Exporta les estadistiques de temperatura a un fitxer JSON.
    """
    dades = {
        "temperatura_maxima": maxim,
        "temperatura_minima": minim,
        "temperatura_mitjana": mitjana
    }
    with open(nom_fitxer, "w") as f:
        json.dump(dades, f, indent=1) 

if __name__ == "__main__":
    # Coordenades de Barcelona (exemple)
    latitud = 41.3888
    longitud = 2.1590

    temperatures = obtenir_temperatures(latitud, longitud)
    maxim, minim, mitjana = calcular_estadistiques(temperatures)

    # Generar el nom del fitxer amb la data actual
    data_actual = datetime.now().strftime("%Y%m%d")
    nom_fitxer = f"temp_{data_actual}.json"

    exportar_a_json(maxim, minim, mitjana, nom_fitxer)

    print(f"S'han calculat les temperatures i s'han guardat a {nom_fitxer}")