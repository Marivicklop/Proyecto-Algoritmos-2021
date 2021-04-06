import requests
from Juegos import *



api = requests.get("https://api-escapamet.vercel.app")

class Ahorcado(Juegos):


    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        words = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.question = words["question"]
        self.word = (words["answer"]).lower()
        self.letters = set(self.word)



    def ahorcado_validacion(self, player):
        print((self.game).title()) 
        print((self.rules).capitalize())
        self.user_letters = set() 
        print(self.question)
        print(self.word)
# aquí se evalua que una vez se haya mostrado las pistas, el input del usuario pasa por un set, el cual es necesario para tener
# un registro de la letras que el usuario va metiendo. estas a su vez se borran del set, y todo esto dentro de un while loop que verifique que hasta 
# que el len de la lista sea 0, se seguirán pidiendo inputs al usuario         
        user_input = (input("-->")).lower()
        
        
        while not user_input.isalpha():
            user_input = (input('Estás buscando romperme el código, son las 2:30 am, no busques romper mi sanidad tambien \n--> ')).lower()
        
        
        while len(self.letters) > 0:

            

            if user_input in self.letters:


                if user_input not in self.user_letters:
                    self.user_letters.add(user_input)
                    self.letters.remove(user_input)
                



            else:
                
                if user_input in self.user_letters:
                    print('Ya utilizaste esa letra')
                    

                else:
                    print('Incorrecto')
                    player.quitar_vidas(n=0.25)


        player.show_inventario(self.award)


        






# ahorcado = Ahorcado(place = 1 , interaction = 0 )



# ahorcado.ahorcado_validacion()
