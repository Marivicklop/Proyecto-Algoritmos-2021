import requests
import random
from Juegos import *

api = requests.get("https://api-escapamet.vercel.app")
# int(float((frase.split()[4]).replace(",", ".")))
class Python(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        self.questions = api.json()[place]["objects"][interaction]["game"]["questions"]
        self.rand_option = random.choice(self.questions)
        self.rand_question = self.rand_option["question"]





    def validar_respuesta(self, player):
        print(self.game)
        print((self.rules).capitalize())
        variable = "frase"

        if self.rand_question == self.questions[0]["question"]:
            print(self.rand_question)
            game_clueslist = []
            game_clueslist.append(self.rand_option["clue_1"])
            game_clueslist.append(self.rand_option["clue_2"])
            game_clueslist.append(self.rand_option["clue_3"])
            game_clues = random.choice(game_clueslist)
            player.get_clues(game_clues) 
           
            answer = input('Ingresa tu código: \n-->')
            

            while not variable in answer:
                answer = input('No usaste la variable dada. Ingresa tu código: \n-->')
            
            frase = "tengo en mi cuenta 50,00 $"

            print(eval(answer))

            while True:
                if not eval(answer) == 50:
                    print('Incorrecto')
                    player.get_clues(game_clues)
                
                else:

                    print('¡Correcto!')
                    player.show_inventario(self.award)
                    break
           
        else:
            print(self.rand_question)
            
            game_clues = (self.rand_option["clue_1"])

            player.get_clues(game_clues) 
            
            answer = input('Ingresa tu código: \n-->')
            

            while not variable in answer:

                answer = input('No usaste la variable dada. Ingresa tu código: \n-->')

            frase = "oidutse ne al ortem aireinegni ed sametsis"
            print(eval(answer))

            while not eval(answer) == "sistemas de ingenieria metro la en estudio":
                print('Incorrecto')
                player.quitar_vidas(n = 0.5)
                player.get_clues(game_clues)
                answer = input('Ingresa tu código: \n-->')
            print('¡Correcto!')
            player.show_inventario(self.award)