import requests
from Juegos import *
import random

api = requests.get("https://api-escapamet.vercel.app")

class Mezclados(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.words = questions["words"]
        print(self.words)


    def mezclar(self, player):
        print(self.game)
        print((self.rules).capitalize())
        user_answer = input('-->').lower()
        while not user_input.isalpha():
            user_input = (input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad también \n--> '))

        for word in self.words:
            word = list(word)
            new_word = random.shuffle(word)
            print("".join(word))

        while new_word != user_input:
            n = 1
            player.quitar_vidas(n)
            print('Incorrecto')
            user_answer = input('-->').lower()
            
        print('Correcto')
        player.show_inventario(self.award)
# mezclados = Mezclados(place = 4, interaction = 1)