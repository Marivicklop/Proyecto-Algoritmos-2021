import requests
import random
import enquiries
from Juegos import Juegos
from Adivinanzas import Adivinanzas
from Jugador import Jugador

api = requests.get("https://api-escapamet.vercel.app")

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
        
def avatar_choice():
  options = ['Scharifker', 'Eugenio Mendoza', 'Pelusa', 'Gandhi', 'Isa', 'Departamento de Física']
  answer = enquiries.choose('---------', options)
  print(f'Escogiste a {answer}')
  return answer

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
  validar_usuario(name)

  datos_jugador(name)


def validar_usuario(name):
  try:
    with open("Jugadores_Database.txt") as dbj:
        datos = dbj.readlines()
        print(datos)
        if name in datos:
          print("\nJugador ya registrado.")
          return main()
        else:
          return datos_jugador(name)
  except FileNotFoundError:
    print("\nTodavía no hay ningún jugador registrado.\n")
    return name_regist()

def datos_jugador(name):


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

  avatar = avatar_choice()


  player = Jugador(name, password, age, avatar)
  player.show_jugador()
  with open("Jugadores_Database.txt","a") as dbj:
    dbj.write(player.name)
    dbj.write(player.password)
    dbj.write(player.age)
    dbj.write(player.avatar)
  return main()



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




def main():


  start()

  options = ['Registrarte', 'Entrar', 'Records', 'Salir']
  answer = enquiries.choose('Elige qué quieres hacer:', options)
  if answer == 'Registrarte':
    name = name_regist()

  elif answer == 'Entrar':
    pass
  elif answer == 'Records':
    pass
  else:
    exit(0)

# # # # # # # juego3
# # # # # #   # adivinanza = Adivinanzas(place = 0, interaction = 2)

# # # # # #   # user_answer = input('--> ')

# # # # # #   # adivinanza.respuesta(user_answer)


main()
