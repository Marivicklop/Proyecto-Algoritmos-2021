import enquiries

class Jugador:

  def __init__(self, name, password, age):
    self.name = name
    self.password = password
    self.age = age
    self.inventario = []
#Mi clase jugador integra la mayoría de los métodos con los cuales se maneja el jugador por el juego
# Defino los atributos necesarios para las clases, a continuación se definen los diferentes metodos que están relacionados con la clase jugador y a su vez con la clase juegos

  def show_inventario(self, award):
    (self.inventario).append(award)
    print(self.inventario)


  def show_jugador(self):

     print(f'''
Nombre: {self.name}
Edad: {self.age}
Avatar: {self.avatar}
''')

  def dificultad(self):
      options = ['Fácil', 'Medio', 'Difícil']
      answer = enquiries.choose('Elige qué quieres hacer:', options)
      if answer == 'Fácil':
          self.life = 5.0
          self.clues = 5
          
      elif answer == 'Medio':
          self.life = 3.0
          self.clues = 3.0
          
      else:
          self.clues = 2
          self.life = 1.0
          
#Aquí realicé el método necesario para mostrar las pistas pero se me imprimía siempre la misma pista

  def show_clues_life(self):
    print(f'Tus pistas disponibles son: {self.clues}')
    print(f'Tus vida es: {self.life}')
  
  def avatar_choice(self):
    options = ['Scharifker', 'Eugenio Mendoza', 'Pelusa', 'Gandhi', 'Isa', 'Departamento de Física']
    answer = enquiries.choose('---------', options)
    print(f'Escogiste a {answer}')
    self.avatar = answer
    return self.avatar

  def get_clues(self, game_clues):
    if self.clues > 0:
      options = ['Sí', 'No']
      user_pistas = enquiries.choose('¿Quiéres pista?', options)
      if user_pistas == 'Sí':
        self.clues += -1
        print(game_clues)
        print(f'Tienes {self.clues} pistas')
      else:
        print('Sin pistas entonces...')
    else:    
    
      print('Ya no tienes pistas')
    
  def check_inventary(self, requirements):
    if requirements in self.inventario:
      return True
    else:
      return False
    

      

  def quitar_vidas(self, n):
    if self.life > 0.0:
      self.life -= n
      print(f'Tienes {self.life} vidas')
     

    else:
      print('''
      
      
  ▄████ ▄▄▄      ███▄ ▄███▓█████     ▒█████  ██▒   █▓█████ ██▀███  
 ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀    ▒██▒  ██▓██░   █▓█   ▀▓██ ▒ ██▒
▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███      ▒██░  ██▒▓██  █▒▒███  ▓██ ░▄█ ▒
░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄    ▒██   ██░ ▒██ █░▒▓█  ▄▒██▀▀█▄  
░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒   ░ ████▓▒░  ▒▀█░ ░▒████░██▓ ▒██▒
 ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░   ░ ▒░▒░▒░   ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░     ░ ▒ ▒░   ░ ░░  ░ ░  ░ ░▒ ░ ▒░
░ ░   ░  ░   ▒  ░      ░     ░      ░ ░ ░ ▒      ░░    ░    ░░   ░ 
      ░      ░  ░      ░     ░  ░       ░ ░       ░    ░  ░  ░     
                                                 ░                 

      
                             __
                           _|  |_
                         _|      |_
                        |  _    _  |
                        | |_|  |_| |
                    _  |  _    _  |  _
                    |_|_|_| |__| |_|_|_|
                      |_|_        _|_|
                        |_|      |_|
                
      
''')
      exit(0)



  def get_vidas(self):
    self.life += 1
    print('¡Ganaste una vida extra!')
