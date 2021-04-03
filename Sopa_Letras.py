import requests
from Juegos import *
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel


api = requests.get("https://api-escapamet.vercel.app")

class Sopa_Letras(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        print(self.game)
        print((self.rules).capitalize())
        questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.words = [questions["answer_1"], questions["answer_2"], questions["answer_3"]]
        print(self.words)
    def sopa(self):
        result = create_panel(height=15, width=15, words_value_list=self.words)
        print('INTENTOS: {}'.format(result.get('attempts')))
        display_panel(result.get('panel'))


sopa_letras = Sopa_Letras(place = 0 , interaction = 0 )

sopa_letras.sopa()