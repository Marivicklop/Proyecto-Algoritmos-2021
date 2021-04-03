import requests
from Juegos import *



api = requests.get("https://api-escapamet.vercel.app")

class Ahorcado(Juegos):


    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        print((self.game).title()) 
        print((self.rules).capitalize())
        words = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        
        self.question = words["question"]
        print(self.question)
        
        self.word = (words["answer"]).lower()
        print(self.word)
        
        self.letters = set(self.word)



    def ahorcado_validacion(self):
        self.user_letters = set() 
        

        while len(self.letters) > 0:

            user_input = (input("-->")).lower()

            if user_input in self.letters:


                if user_input not in self.user_letters:
                    self.user_letters.add(user_input)
                    self.letters.remove(user_input)
                



            else:
                
                if user_input in self.user_letters:
                    print('Ya utilizaste esa letra')
                else:
                    print('mal')

            


        






ahorcado = Ahorcado(place = 1 , interaction = 0 )



ahorcado.ahorcado_validacion()
