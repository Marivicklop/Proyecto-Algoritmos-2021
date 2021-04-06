import requests
from Juegos import *
import random


api = requests.get("https://api-escapamet.vercel.app")

class Booleanos(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        print(self.game)
        print((self.rules).capitalize())
        self.question = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
  
        self.answer = self.question["answer"]

    
    def validacion_input(self, player):
        print(self.question["question"])
        user_input = (input('-->')).capitalize()

        while not user_input.isalpha():
            user_input = (input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad también \n--> ')).capitalize()

        if user_input == self.answer:
            print('¡Correcto!')
            player.show_inventario(self.award)

        else:
            print('¡Incorrecto!')
            player.quitar_vidas(n = 0.5)



# booleanos = Booleanos(place = 3, interaction = 0)

# user_input = (input('-->')).capitalize()

# booleanos.validacion_input(user_input)