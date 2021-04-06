import requests
import random
import enquiries
from Juegos import Juegos
from Jugador import Jugador
from Lugares import *
import json

# api = requests.get("https://api-escapamet.vercel.app")

def mensajes(n):
  if n == 1:
    print('''
 
   ██╗    ████████╗ ██████╗███╗   ██╗██████╗██╗
   ██║    ████╔══████╔═══██████╗  ████╔════╝██║
   ██║ █╗ ████████╔██║   ████╔██╗ ████║  █████║
   ██║███╗████╔══████║   ████║╚██╗████║   ██╚═╝
   ╚███╔███╔██║  ██╚██████╔██║ ╚████╚██████╔██╗    

''')

def validacion_password():
  password = input('''
 _________________________________________________________________________________________________________________________________
|                                                                                                                                 |
|  Ingrese su contraseña(Debe contener al menos una letra minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico)  |
|_________________________________________________________________________________________________________________________________|

  -->''')


  while True:

    minusc = False
    num = False
    mayusc = False
    space = False
    special = False

    for carac in password:

        if carac.islower():
            minusc = True

        if carac.isdigit():
            num = True

        if carac.isupper():
            mayusc = True

        if carac.isspace():
            space = True

        if not(carac.isalnum()):
            special = True

    if len(password) < 8 or not minusc or not num or not mayusc or not special or space:
      mensajes(1)
      password = input('''
 ______________________________________________ 
|                                              |
|  Contrasena incorrecta, inténtelo de nuevo   |
|______________________________________________|

-->''')


    else:
        print('¡Contrasena ingresada correctamente!')
        return password
        break
        


def name_regist():
  name = input('''
 ___________________________________________________ 
|                                                   |
|  Ingrese su nombre de usuario(máx 10 caracteres)  |
|___________________________________________________|

-->''')
  while name == '' or len(name) > 10:
    mensajes(1)
    name = input('''
 _______________________________________________________________________
|                                                                       |
|  Ingreso incorrecto. Ingrese su nombre de usuario(máx 10 caracteres)  |
|_______________________________________________________________________|   
    
-->''')

  return name
  




# def validar_usuario(name):
#   try:
#     with open("Jugadores_Database.txt") as file:
#       user_database = json.loads(file.readlines())
#       print(user_database)
#       print('\n\npapapapapa')
#       # if name in user_database['User']:
#       #   print('\n\npapapapapa')
#       #   print("\nJugador ya registrado.")
#       #   return main()
#       # else:
#       #   print('a')
#   except FileNotFoundError:
#     print('\n\npapapapapa')
#     print("\nTodavía no hay ningún jugador registrado.\n")
#     return datos_jugador()

def datos_jugador():

  name = name_regist()
  # validar_usuario(name)
  password = validacion_password()


  age = input('''
 ___________________ 
|                   |
|  Ingrese su edad  |
|___________________|

-->''')
  while (not age.isnumeric()):
    mensajes(1)
    name = input('''
 _____________________________________
|                                     |
|  Ingreso inválido. Ingrese su edad  |
|_____________________________________|
    
-->''')

  print('''
 _________________________________ 
|                                 |
|  Ingrese el avatar que quiere   |
|_________________________________| 
''')

  
  
  player = Jugador(name, password, age)
  player.avatar_choice()
  player.show_jugador()


  jugadores_database = {'User': name,'Password': password, 'Age': age}
  with open("Jugadores_Database.txt","a") as file:
    file.write(json.dumps(jugadores_database))  

  return player

def start():
  input('''       °      °           °            °     °        °               ° 
             °            ____________________________________________________________________ °    °    
     °                  /____________________________________________________________________/|           °
        °     °        |                                                                    | |    °
    °         °        |██████████████╗██████╗█████╗██████╗ █████╗███╗   ██████████████████╗| |          °
          °            |██╔════██╔════██╔════██╔══████╔══████╔══██████╗ ██████╔════╚══██╔══╝| |              °
     °           °     |█████╗ █████████║    █████████████╔█████████╔████╔███████╗    ██║   | |       °
 °                     |██╔══╝ ╚════████║    ██╔══████╔═══╝██╔══████║╚██╔╝████╔══╝    ██║   | |          °
         °   °         |██████████████╚████████║  ████║    ██║  ████║ ╚═╝ █████████╗  ██║   | |    °
           °           |╚══════╚══════╝╚═════╚═╝  ╚═╚═╝    ╚═╝  ╚═╚═╝     ╚═╚══════╝  ╚═╝   | |        °
    °             °    |                       _________________________                    | |      °                       
         °             |______________________|Dale a enter para empezar|___________________|/             °
      °                                                                                        °
              °       ________________________________________________________________________    °
    °               /________________________________________________________________________/|     
                   |                                                                        | |      
                   |██╗   █████╗   ██████╗   ███████████████╗███████████████╗ █████╗██████╗ | |     °      
     °             |██║   ██████╗  ██████║   ████╔════██╔══████╔════████╔══████╔══████╔══██╗| |          
             °     |██║   ████╔██╗ ██████║   ███████╗ ██████╔███████████║  ███████████║  ██║| |  °         
 °                 |██║   ████║╚██╗████╚██╗ ██╔██╔══╝ ██╔══██╚════██████║  ████╔══████║  ██║| |    °   °    
     °     °       |╚██████╔██║ ╚██████║╚████╔╝█████████║  █████████████████╔██║  ████████╔╝| |___________    °      
        ___________| ╚═════╝╚═╝  ╚═══╚═╝ ╚═══╝ ╚══════╚═╝  ╚═╚══════╚═╚═════╝╚═╝  ╚═╚═════╝ |/__________ /|           
  °    |                                                                                                | |  °   
       |███╗   ████████████████████████╗ ██████╗██████╗ ██████╗██╗    ██████████╗█████╗███╗   ██╗█████╗ | |       ° 
 °     |████╗ ██████╔════╚══██╔══██╔══████╔═══████╔══████╔═══████║    ██╚══██╔══██╔══██████╗  ████╔══██╗| |          °
       |██╔████╔███████╗    ██║  ██████╔██║   ████████╔██║   ████║    ██║  ██║  █████████╔██╗ █████████║| |    °
°      |██║╚██╔╝████╔══╝    ██║  ██╔══████║   ████╔═══╝██║   ████║    ██║  ██║  ██╔══████║╚██╗████╔══██║| |        °
   °   |██║ ╚═╝ █████████╗  ██║  ██║  ██╚██████╔██║    ╚██████╔█████████║  ██║  ██║  ████║ ╚██████║  ██║| |     °
 °     |╚═╝     ╚═╚══════╝  ╚═╝  ╚═╝  ╚═╝╚═════╝╚═╝     ╚═════╝╚══════╚═╝  ╚═╝  ╚═╝  ╚═╚═╝  ╚═══╚═╝  ╚═╝| |        °
    °  |________________________________________________________________________________________________|/       °                                                                                        
     °                                                                                                        °
         °   °      °                °        °            °     °           °      °         °     °     °                                                                       
                  °       °           °                °               °          °        °    °     °       ° 
 °
''')

def decisiones():
  options = ['Ir a otra sala', 'Quedarme']
  answer = enquiries.choose('Elige qué quieres hacer:', options)
  if answer == 'Ir a otra sala':
    return True
  elif answer == 'Quedarme':
    return False

def comienzo(player):
  sala = 1
  lugares = Lugares(sala)
  lugares.show_sala()
  decision = decisiones()
  if decision == True:
    numero_salas(sala, player)


  else:
    interaction = movimientos(player)
    lugares.movimiento(interaction, player)
    return comienzo(player)

def lab01(player):
  sala = 0
  lugares = Lugares(sala)
  lugares.show_sala()
  decision = decisiones()
  if decision == True:
    numero_salas(sala, player)


  else:
    interaction = movimientos(player)
    lugares.movimiento(interaction, player)
    return lab01(player)

def saman(player):
  sala = 2
  lugares = Lugares(sala)
  lugares.show_sala()
  decision = decisiones()
  if decision == True:
    numero_salas(sala, player)


  else:
    interaction = movimientos(player)
    lugares.movimiento(interaction, player)
    return saman(player)

  
def laboratorios(player):
  sala = 3
  lugares = Lugares(sala)
  lugares.show_sala()
  decision = decisiones()
  if decision == True:
    numero_salas(sala, player)
  else:
    options = ['Sí', 'No']
    answer = enquiries.choose('Estás list@ para jugar:', options)
    if answer == 'No':
      numero_salas(sala, player)
    else:
      interaction = 0
      lugares.movimiento(interaction, player)
      return laboratorios(player)


    

def centro_de_servidores(player):
  sala = 4
  lugares = Lugares(sala)
  lugares.show_sala()
  decision = decisiones()
  if decision == True:
    numero_salas(sala, player)


  else:
    interaction = movimientos(player)
    lugares.movimiento(interaction, player)
    return centro_de_servidores(player)


def numero_salas(sala, player):
  if sala == 0: #Laboratorio Sl001
    options = ['Centro de servidores', 'Laboratorios']
    answer = enquiries.choose('¿A dónde quieres ir?', options)
    if answer == 'Centro de servidores':
      return centro_de_servidores(player)
    else: 
      return laboratorios(player)

  elif sala == 1: #Biblioteca
    options = ['Samán', 'Laboratorios']
    answer = enquiries.choose('¿A dónde quieres ir?', options) 
    if answer == 'Samán':
      return saman(player)
    else: 
      return laboratorios(player)

  elif sala == 2: #saman
    options = ['Biblioteca, ups solo puedes ir a la biblioteca desde el samán']
    answer = enquiries.choose('¿A dónde quieres ir?', options)
    if answer == 'Biblioteca, ups solo puedes ir a la biblioteca desde el samán':
      return comienzo(player)

  elif sala == 3: #pasillo
    options = ['Laboratorio SL001', 'Biblioteca']
    answer = enquiries.choose('¿A dónde quieres ir?', options)  
    if answer == 'Laboratorio SL001':
      return lab01(player)
    else: 
      return comienzo(player)
  
  elif sala == 4: #cuarto de servidores
    options = ['Laboratorio SL001, ups solo puedes ir al Laboratorio desde el cuarto de servidores']
    answer = enquiries.choose('¿A dónde quieres ir?', options) 
    if answer == 'Laboratorio SL001, ups solo puedes ir al Laboratorio desde el cuarto de servidores':
      return lab01(player)


def movimientos(player):
  options = ['Centro', 'Izquierda', 'Derecha']
  answer = enquiries.choose('¿Con qué objeto deseas interactuar?', options)
  if answer == 'Centro':
    interaction = 0
    return interaction
  elif answer == 'Izquierda':
    interaction = 1
    return interaction
  else:
    interaction = 2
    return interaction


def empezar_juego(player, life):
  while True:
    comienzo(player)


    
def main():


  start()

  options = ['Registrarte', 'Entrar', 'Records', 'Salir']
  answer = enquiries.choose('Elige qué quieres hacer:', options)
  if answer == 'Registrarte':
    player = datos_jugador()
    life = player.dificultad()
    player.show_clues_life()
    empezar_juego(player, life)
    
  elif answer == 'Entrar':
    name = 'marib'
    password = 'a'
    age = '11'
    player = Jugador(name, password, age)
    life = player.dificultad()
    player.show_clues_life()
    empezar_juego(player, life)

  elif answer == 'Records':
    pass
  else:
    exit(0)

# # # # # # # juego3
# # # # # #   # adivinanza = Adivinanzas(place = 0, interaction = 2)

# # # # # #   # user_answer = input('--> ')

# # # # # #   # adivinanza.respuesta(user_answer)


main()
