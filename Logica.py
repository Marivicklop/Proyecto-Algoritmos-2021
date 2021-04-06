import requests
from Juegos import Juegos
import random


api = requests.get("https://api-escapamet.vercel.app")

class Logica(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        random_numbers = [0, 1]
        self.n = random.choice(random_numbers)           
        self.questions = (api.json()[place]["objects"][interaction]["game"]["questions"][self.n])
        



    def validar_respuesta(self, player):
        print((self.game).capitalize())
        print((self.rules).capitalize())
        print(self.questions)
        user_input = input('--> ')
        while not user_input.isdigit() or user_input == '' or user_input.isspace():
            user_input = input('--> ')

        if self.n == 0:
            if user_input == '67':
                print('¡Correcto!')
                player.show_inventario(self.award)

            
            else:
                print('Incorrecto')
                player.quitar_vidas(n = 1)
        else: 
            if user_input == '41':
                print('¡Correcto!')
                player.show_inventario(self.award)


            else:
                print('Incorrecto')
                player.quitar_vidas(n = 1)





        

