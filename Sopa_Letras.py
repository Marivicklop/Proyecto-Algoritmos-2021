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
        self.questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.words = [(self.questions["answer_1"]).lower(), (self.questions["answer_2"]).lower(), (self.questions["answer_3"]).lower()]
        print(self.words)
    
    def sopa(self):
        result = create_panel(height=15, width=15, words_value_list=self.words)
        print('INTENTOS: {}'.format(result.get('attempts')))
        display_panel(result.get('panel'))

    def user_input(self, player):
        game_clueslist = []
        game_clueslist.append(self.questions["clue_1"])
        game_clueslist.append(self.questions["clue_2"])
        game_clueslist.append(self.questions["clue_3"])
        game_clues = random.choice(game_clueslist)
        
        player.get_clues(game_clues)
        self.sopa()
        
        
        while len(self.words) > 0:
            self.sopa()
            user_input = (input('--> ')).lower()
            
            while not user_input.isalpha():
                user_input = (input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad tambien \n--> ')).lower()
            
            while user_input not in self.words:
                n = 1           
                print('Incorrecto')
                player.get_clues(game_clues)
                player.quitar_vidas(n = 1)
                user_input = (input('--> ')).lower()
            
            if user_input in self.words:
                print('¡Correcto!')
                (self.words).remove(user_input)

            


        print('¡Encontraste todas!')
        player.get_vidas()
# sopa_letras = Sopa_Letras(place = 0 , interaction = 0 )

# sopa_letras.sopa()