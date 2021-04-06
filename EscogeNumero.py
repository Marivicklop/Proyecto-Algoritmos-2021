import requests
from Juegos import *
import random
from Jugador import Jugador
api = requests.get("https://api-escapamet.vercel.app")

class EscogeNumero(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)

        questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        question = questions["question"]
        question = question.replace('-', ' ')
        self.question = question.split()

    def contador(self, contador, m):
        print((self.game).capitalize())
        print((self.rules).capitalize())
        if contador == True:
            if m < 3:
                m += 1
            else:
                m = 0
                player.quitar_vidas(n = 0.25)

    def numero_random(self, player):
        m = 0
        max_n = int(self.question[-1])
        min_n = int(self.question[-2])
        guessin_n = random.randint(min_n, (max_n+1))
        print(guessin_n)
        
        user_input = input('--> ')
        while not user_input.isdigit() or user_input == '' or user_input.isspace():
            user_input = input('--> ')
            
# mequieromorir, en este código primero se hace un contador para las vidas que no sé si me funciona porque el códiog
# no corre :c la API no lo logra       

        if int(user_input) == guessin_n:
            print('¡Correcto!')
            player.show_inventario(self.award)
            
#aquí ya que se etsa pidiendo que se le indique al usuario si esta muy arriiba o muy abajo 
#se establece un parametro de cercanía en este caso yo utilice un intervalo de 3 entre los números
#  

        else:
            while user_input != guessin_n:

                cerca_arriba = guessin_n + 3
                cerca_abajo = guessin_n - 3
                user_input = int(user_input)
                
                if user_input in range(cerca_abajo, guessin_n+1):
                    print('tas un poco abajo')
                    user_input = int(input("--> "))
                    contador = True
                    self.contador(contador, m)
                elif user_input in range(guessin_n, cerca_arriba + 1):
                    print('tas un poco arriba')
                    user_input = int(input("--> "))
                    contador = True
                    self.contador(contador, m)
                elif user_input > cerca_arriba:
                    print('tas muy arriba')
                    user_input = int(input("--> "))
                    contador = True
                    self.contador(contador, m)
                elif user_input < cerca_abajo:
                    print('tas muy abajo')
                    user_input = int(input("--> "))
                    contador = True
                    self.contador(contador, m)

            print('¡Correcto!')
            player.show_inventario(self.award)

                
            

# escogenumero = EscogeNumero(place = 4, interaction = 2)



# escogenumero.numero_random()