import requests
import random

api = api = requests.get("https://api-escapamet.vercel.app")

class Juegos:
    def __init__(self, place, interaction):
        self.game = api.json()[place]["objects"][interaction]["game"]["name"]
        self.rules = api.json()[place]["objects"][interaction]["game"]["rules"]
        self.award = api.json()[place]["objects"][interaction]["game"]["award"]
        self.requirement = api.json()[place]["objects"][interaction]["game"]["requirement"]

    def dificultad(self):
        options = ['Fácil', 'Medio', 'Difícil']
        answer = enquiries.choose('Elige qué quieres hacer:', options)
        if answer == 'Fácil':
            self.clues = 5
            self.life = 5.0
            return self.clues 
            return self.life
        elif answer == 'Medio':
            self.clues = 3
            self.life = 3.0
            return self.clues
            return self.life
        else:
            self.clues = 2
            self.life = 1.0
            return self.clues
            return self.life

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