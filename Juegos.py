import requests
import random

api = api = requests.get("https://api-escapamet.vercel.app")

class Juegos:
    def __init__(self, place, interaction):
        self.game = api.json()[place]["objects"][interaction]["game"]["name"]
        self.rules = api.json()[place]["objects"][interaction]["game"]["rules"]
        self.award = api.json()[place]["objects"][interaction]["game"]["award"]
        self.requirement = api.json()[place]["objects"][interaction]["game"]["requirement"]
    

# class Sopa_Letras(Juegos):
#     pass

# class Python(Juegos):
#     pass

# class Adivinanzas(Juegos):
#     pass

# class Ahorcado(Juegos):
#     pass

# class Derivadas(Juegos):
#     pass

# class Criptograma(Juegos):
#     pass

# class Logica(Juegos):
#     pass

# class Quizizz(Juegos):
#     pass

# class Memoria(Juegos):
#     pass

# class Booleanos(Juegos):
#     pass

# class Libre(Juegos):
#     pass

# class Mezclados(Juegos):
#     pass

# class EscogeNumero(Juegos):
#     pass