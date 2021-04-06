import requests
from Juegos import Juegos
import random
from Jugador import Jugador


api = requests.get("https://api-escapamet.vercel.app")

class Adivinanzas(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        
        self.question = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.message = api.json()[place]["objects"][interaction]["game"]["message_requirement"]
        self.adivinanza = self.question["question"]
        self.answers = self.question["answers"]
           
        


# En este juego el código que planteaes bastante sencillo, lo único que se tiene que hacer
# es revisar si la respuesta del usuario se encuentra dentro de la lista 


    def respuesta(self, player):
        print(self.adivinanza)
        print(self.game)
        print((self.rules).capitalize())
        game_clueslist = []
        game_clueslist.append(self.question["clue_1"])
        game_clueslist.append(self.question["clue_2"]) #TODO
        game_clueslist.append(self.question["clue_3"])
        game_clues = random.choice(game_clueslist)
        player.get_clues(game_clues)
        

        user_input = input('-->')
       
        while not user_input.isalpha():
            user_input = input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad también \n--> ')
        
        while user_input not in self.answers:
            n = 0.5
            print('Incorrecto')
            player.get_clues(game_clues)
            player.quitar_vidas(n = 0.5)
            user_answer = input('-->')
            # if player.life > 0.0:
            
                # user_answer = input('-->')
                # while not user_input.isalpha():
                #     user_input = input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad también \n--> ')


        print('¡Correcto!')
        player.show_inventario(self.award)
        
