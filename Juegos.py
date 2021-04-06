import requests
import random
from Jugador import * 

api = api = requests.get("https://api-escapamet.vercel.app")

class Juegos:
    def __init__(self, place, interaction):
        self.game = api.json()[place]["objects"][interaction]["game"]["name"]
        self.rules = api.json()[place]["objects"][interaction]["game"]["rules"]
        self.award = api.json()[place]["objects"][interaction]["game"]["award"]
        self.requirement = api.json()[place]["objects"][interaction]["game"]["requirement"]

    
#aquí esta la clase juego
