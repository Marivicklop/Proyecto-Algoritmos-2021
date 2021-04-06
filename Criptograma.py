import requests
from Juegos import *
from caesarcipher import CaesarCipher
from string import ascii_lowercase as abecedario
from prettytable import PrettyTable

api = requests.get("https://api-escapamet.vercel.app")


class Criptograma(Juegos):
    def __init__(self, place, interaction):
        super().__init__(place, interaction)
        print(self.game)
        print((self.rules).capitalize())
        questions = random.choice(api.json()[place]["objects"][interaction]["game"]["questions"])
        self.desplazamiento = questions["desplazamiento"]
        self.message = (questions["question"]).lower()


# en este juego tenemos el caso de que el mensaje dado en la api tiene un acento, se reemplaza primeramente con la función de 
# reemplazar_acentos
    
    
    def reemplazar_acentos(self):
        if 'á' in self.message:
            self.message = (self.message).replace('á', 'a')
            return self.message

# luego aquí utilizando la librería de CaesarCypher, se revuelven los caracteres de la frase dependiendo de 
# la pregunta que haya escogido el random choice        

    def cifrar_message(self):
        criptograma.reemplazar_acentos()
        cifrar = CaesarCipher(self.message, offset = self.desplazamiento)
        self.frase = cifrar.encoded
        print(f'''
         
\t                               +----------------------------+
\t                               |{self.frase}|
\t                               +----------------------------+



''')
# Se cifra el abecedario segun el desplazamiento

    def cifrar_abecedario(self):
        abecedario_cifrado = CaesarCipher(abecedario, offset = self.desplazamiento)
        abecedario_cifrado = abecedario_cifrado.encoded
        return abecedario_cifrado

# Se utiliza la librería PrettyTable para presentar de manera agradable el abecedario

    def show_abecedario(self):
        tabla = PrettyTable()
        tabla2 = PrettyTable()
        abecedario_cifrado = Criptograma.cifrar_abecedario()
        lista_abecedario = list(abecedario)
        lista_abecedario = ' | '.join(lista_abecedario)
        tabla.add_column("Abecedario", [lista_abecedario])

        lista_abecedario_cifrado = list(abecedario_cifrado)
        lista_abecedario_cifrado = ' | '.join(lista_abecedario_cifrado)
        tabla2.add_column("Abecedario Cifrado", [lista_abecedario_cifrado])

        print(tabla2)
        print(tabla)

    def comprobacion(self, player):
        user_input = (input("-->")).lower()
        while not user_input.isalpha():
            user_input = (input("-->")).lower()
                
        while user_input != self.message:
            player.quitar_vidas(n = 1)
            print('Incorrecto')
            user_input = (input("-->")).lower()

            
        print('¡Correcto!')
        player.show_inventario(self.award)
            
        
            

# criptograma = Criptograma(place = 1 , interaction = 2)

# criptograma.cifrar_message()

# criptograma.show_abecedario()

# user_input = (input('\n-->')).lower()

# criptograma.comprobacion(user_input)

