import requests
from Juegos import *
import enquiries
import random

api = requests.get("https://api-escapamet.vercel.app")

class Quizizz(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.correct_answer = questions["correct_answer"]
        self.answer_2 = questions["answer_2"]
        self.answer_3 = questions["answer_3"]
        self.answer_4 = questions["answer_4"]
        self.question = questions["question"]  


    def preguntas(self, player):
        print(self.game)
        print((self.rules).capitalize())
        
        options = [self.answer_2, self.answer_3, self.answer_4, self.correct_answer]
        answer = enquiries.choose(f'{self.question}', options)
        while answer != self.correct_answer:
            print('Incorrecto')
            player.quitar_vidas(n = 1)
            answer = enquiries.choose(f'{self.question}', options)
        
        print('Correcto')
        player.show_inventario(self.award)
            
        

# quizizz = Quizizz(place = 2 , interaction = 1)
# quizizz.preguntas()