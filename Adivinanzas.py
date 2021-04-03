import requests
from Juegos import Juegos
import random

api = requests.get("https://api-escapamet.vercel.app")

class Adivinanzas(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        print(self.game)
        print((self.rules).capitalize())
        question = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.message = api.json()[place]["objects"][interaction]["game"]["message_requirement"]
        self.adivinanza = question["question"]
        self.answers = question["answers"]
        print(self.adivinanza)
        print(self.answers)

    def respuesta(self, user_answer):
        if user_answer in self.answers:
            print('bien')
        else:
            print('mal')


adivinanza = Adivinanzas(place = 0, interaction = 2)

user_answer = input('--> ')
adivinanza.respuesta(user_answer)