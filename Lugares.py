import requests
import random
from Jugador import Jugador
from Juegos import Juegos
from Adivinanzas import Adivinanzas
from Ahorcado import Ahorcado
from Logica import Logica
from Booleanos import Booleanos
from Criptograma import Criptograma
from Derivadas import Derivadas
from EscogeNumero import EscogeNumero
from Libre import Libre 
from Memoria import Memoria
from Mezclados import Mezclados
from Python import Python
from Quizizz import Quizizz
from Sopa_Letras import Sopa_Letras

api = requests.get("https://api-escapamet.vercel.app")

class Lugares:
    def __init__(self, sala):
        self.sala = sala


#             get room retorna el grafico
#             objetos
#             salas


# funcion desplazamiento de izquierda derecha entre el mapa el cuarto

# parametros get room, pedir mov del user

#cuando vas al saman se tendr[ia la comprobaci[on de un booleno para cchequear si los obketos ene l inventario son los necesarios para no perder vidas]]

# funcion interactuar los objetos de la habitacion

# parametros games y objetos

# parametro en la clase juego de booleano para chequear si el juego esta completo junto un parametro que te deniegie la enrada al juego en casp de ser check True

    def show_sala(self):

        if self.sala == 0:
            print('''
                                                                                            
           ██      █████ ██████  ██████ ██████  █████ ████████ ██████ ██████ ██ ██████      █████████      ██████  ██████  ██ 
           ██     ██   ████   ████    ████   ████   ██   ██   ██    ████   ██████    ██     ██     ██     ██  ██████  ███████ 
           ██     █████████████ ██    ████████ ███████   ██   ██    ████████ ████    ██     █████████     ██ ██ ████ ██ ██ ██ 
           ██     ██   ████   ████    ████   ████   ██   ██   ██    ████   ██████    ██          ████     ████  ██████  ██ ██ 
           █████████   ████████  ██████ ██   ████   ██   ██    ██████ ██   ████ ██████      ██████████████ ██████  ██████  ██ 
 _________________________________________________________________________________________________________________________________________
|                                                                                                                                         |
|                                                                                                                                         |
|                                           ________________________________________                                                      | 
|                                          |  ____________________________________  |                                                     |
|                                          | |                                    | |                                                     | 
|                                          | |                                    | |             ______________      _______             |
|                                          | |                                    | |            |.------------.|    |[====o]|            | 
|___.___     ~         _____________       | |                                    | |            ||            ||    |[_.--_]|            |
|\ \o\  \   ,, ???    |        '\ \ \      | |                                    | |            ||            ||    |[_____]|            |
| \ \o\  \ /<   ?     |        ' ____|_    | |                                    | |            ||            ||    |      :|            |
|--\//,- \_.  /_____  |        '||::::::   | |                                    | |            ||____________||    |      :|            |
|    o- /   \_/    '\ |        '||_____|   | |                                    | |        .==.|""  ......    |.==.|      :|            |
|    | \ '   o       '________|_____|      | |                                    | |        |::| '-.________.-' |::||      :|            |
|    |  |-   #     <  ___/____|___\___     | |____________________________________| |        |''|  /__________\-.|''||______:|            |
|    `_/'------------|    _    '  <<<:|    |________________________________________|      /  `""`_.............._\ `______ |\            |
|        /________\| |_________'___o_o|                                                   |     /:::::::::::'':::\`;'-.-.  `\  \          |
|    \_______________________________/|                                                   |    /::=========.:.-::"\ \ \--\   \  \         |
|____|                                |___________________________________________________|    \`""""""""""""""""`/  \ \__    \  \________|
|    |                                |                                                   |     `""""""""""""""""`    '========'  \       |
|    |                                |                                                   |                                        \      |
|    |                                |                                                   |_________________________________________\     | 
|____|________________________________|___________________________________________________|_________________________________________|_____|  
      
                                                                                                
            ''')

        elif self.sala == 1:
            print('''
            
                                ██████ ████████ ██     ██ ██████ ███████████████ ██████ █████  
                                ██   ██████   ████     ████    ██   ██   ██     ██     ██   ██ 
                                ██████ ████████ ██     ████    ██   ██   █████  ██     ███████ 
                                ██   ██████   ████     ████    ██   ██   ██     ██     ██   ██ 
                                ██████ ████████ █████████ ██████    ██   ███████ ████████   ██ 
                                                               
 __________________________________________________________________________________________________________________________________                                                           
|                                                                                                                                  |
|                                                     ______________________________                                               |
|      _______________________________               ||----------------------------||\                                             |
|     | _____________________________ |              ||.--.    .-._                || |                                            |
|     ||=============================||              |||==|____| |H|___            || |                                            |
|     ||-----------------------------||              |||  |====| | |xxx|_          || |                                            |
|     ||=============================||              |||==|    | | |   | \         || |                                            |
|     ||-----------------------------||              |||  |    | | |   |\ \   .--. || |                                            |
|     ||_____________________________||              |||  |    | | |   |_\ \_( oo )|| |                                            |
|     |_______________________________|              |||==|====| |H|xxx|  \ \ |''| || |                                            |
|                                                    ||`--^----'-^-^---'   `-' ""  || |                                            |
|                  .----.                            ||----------------------------|| |                                            |
|                  |    |                            ||----------------------------|| |                                            |
|                  |____|                            ||          .-.__.-----. .---.|| |                                            |
|   _.-------------._()_.-------------._             || __   .---| |XX|<(*)>|_|^^^||| |                                            |
|  / |             | )( |             | \            || ''|__|:x:|=|  |     |=| Q ||| |            _____________________________   |
|__| |             | () |             | |____________||   |==|   | |  |Illum| | R ||| |___________|        °°°°°°°°°°         | \__|
|  _\|_____________| )( |_____________|/_            || ''|  |:x:|=|  |inati| | Y ||| |           |___________________________| |  |
|.=. /             /(__)\             \ .=.          ||   |  |   | |  |     | | Z ||| |           |        °°°°°°°°°°         | |  |
||U|/_____________/______\_____________\|U|\         || ''|==|:x:|=|XX|<(*)>|=|^^^||| |           |___________________________| |  |
|| |====================================| ||         || --'--^---^-^--^-----^-^---^|| |           |        °°°°°°°°°°         | |  |
|| |                                    | ||         ||----------------------------|| |           |___________________________|_|  |
||_|LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLlc|_||_________||____________________________||_|___________||_||______________________||||__|
                                                                                                        
   
            ''')

        elif self.sala == 2:
            print('''
            

                 ██████ ██      █████ ███████ █████      ██████ ███████ ██████████████ ██████ ██████  █████ ██████  ██████  
                 ██   ████     ██   ██   ███ ██   ██     ██   ████     ██        ██   ██    ████   ████   ████   ████    ██ 
                 ██████ ██     ███████  ███  ███████     ██████ █████  ██        ██   ██    ████████ █████████   ████    ██ 
                 ██     ██     ██   ██ ███   ██   ██     ██   ████     ██        ██   ██    ████   ████   ████   ████    ██ 
                 ██     █████████   ███████████   ██     ██   █████████ ██████   ██    ██████ ██   ████   ████████  ██████  
                                                                                                           
                                                                                                           
 ___________________________________________________________________________________________________________________________                                                                                                           
|                                                                           .-                                               |    
|                                                    -.                   -.  -.        .- -.                                |
|                                                 .-    .-  -.          -.      -. -. .-     -.                              |
|                                              .-  .             -. .   .          ;%   -.  ;;   .-                            |
|            ____________                    .-         ,           ,                :;%  %;      -.                       ___|   
|         __/            \__                      :         ;                   :;%;'     .,      -.                _____/   |
|  ______/                  \____          .-  ,.        %;     %;            ;        %;'    ,;    -.             _/         |
| /                              \___             ;       ;%;  %%;        ,     %;    ;%;    ,%'    -.           /           |
|                                    \__        %;      _%;%;      ,  ;       %;  ;%;   ,%;'          .    _ ___/            |
|                                       \ -.    ;%;  __/ %;        ;%;        % ;%;  ,%;'             .   /                  |
|                                          -.    `%;./    ;%;     %;'        `;%%;.%;'             --.___/                   |
|                                         .-      `:;%.    ;%%. %@;-.       %; ;@%;%'             -                          |    
|                                          -.        `:%;.  :;bd%;   -.      %;@%;'             -                            |            
|                                             -. -. -   `@%:.  :;%.       -. ;@@%;'              -                           |
|                                                    -.   `@%.  `;@%.     -. ;@@%;        -.                                 |
|                                                      -. `@%%. `@%%    ;@@%;        -.                                      |
|                                                            ;@%. :@%%  %@@%;   -.                                           |
|                                                            %@bd%%%bd%%:;                                                   |    
|                                                                #@%%%%%:;;                                                  |
|________________________________________________________________%@@%%%::;___________________________________________________|
|                                                                %@@@%(o);  . '                                              |
|    .-                                                            %@@@o%;:(.,'                                              |
|                                  .-               .-           `.. %@@@o%::;       .-             .-            .-         |
|                       .-                        /// |.---------- )@@@o%::;--------//|                                      |
|          -.                                    ///  /           %@@(o)::;        // |_            -          -.            |
|                      - .                      ///  /           .%@@@@%::;       //   /|                                    |
|                                              /||  /           ;%@@@@%::;.      //   /||            .-                      | 
|     .-                           .-         /_|| /            ;%@@@@%%:;;;.   ||___/ ||                          -.        |
|                                            ||||/         ...;%@@@@@%%:;;;;,.. ||  ||               .-                      |
|          .-                                ||||'----------------------------- ||  ||                                       |
|                     .-      -.                                                                                   -.        |
|                                                                                                                            |    
|____________________________________________________________________________________________________________________________|            
''')

        elif self.sala == 3:
            print('''
            
                                    ██████  █████ ███████████     ██      ██████  
                                    ██   ████   ████     ████     ██     ██    ██ 
                                    ██████ ██████████████████     ██     ██    ██ 
                                    ██     ██   ██     ██████     ██     ██    ██ 
                                    ██     ██   █████████████████████████ ██████  

                    88888888888888888888888888888888888888888888888888888888888888888888888
                    88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
                    88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
                    88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
                    88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
                    88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
                    88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
                    88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
                    88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
                    88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
                    88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
                    88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
                    88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
                    88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
                    88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
                    88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
                    88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
                    88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
                    88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
                    88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
                    88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
                    88 8888888888888888888888888888888888888888888888888888888888888 888888
                                              
                                              

            ''')
        elif self.sala == 4:
            print('''
            
                    ████████████████████ ██    ██████████  ██████ ██████ ██████████████ 
                    ██     ██     ██   ████    ██████   ████    ████   ████     ██      
                    ████████████  ██████ ██    ██████   ████    ████████ █████  ███████ 
                         ████     ██   ██ ██  ██ ████   ████    ████   ████          ██ 
                    ████████████████   ██  ████  ████████  ██████ ██   ████████████████ 
                                                                                        
                                                                    

            ''')

    
    #se creó un método de movimiento el cual permite al usuario navegar por las diferentes salas
    #de forma que todo esté relacionado y a su vez se utilizó el método de show para mostrar los gráficos
    # de las salas, btw yo hice el banquito y las hojitas del saman
    # en este método se pasa el objeto player de forma que este mismo se pase por las diferentes subclases de Juegos    
    def movimiento(self, interaction, player):
        if self.sala == 0:
            place = 0
            if interaction == 0:
                sopa_letras = Sopa_Letras(place, interaction)
                sopa_letras.user_input(player)
            elif interaction == 1:
                python = Python(place, interaction)
                if (player.check_inventary(python.requirement)) == True:
                    python.validar_respuesta(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{python.requirement}')
            else:
                contrasenia = True
                if contrasenia == True:
                    adivinanzas.respuesta(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas contraseña')

        elif self.sala == 1:
            place = 1
            if interaction == 0:

                Ahorcado(place, interaction).ahorcado_validacion(player)
        

            elif interaction == 1:
                if (player.check_inventary(Derivadas(place, interaction).requirement)) == True:
                    Derivadas(place, interaction).memoria_rip(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{Derivadas(place, interaction).requirement}')
            else:
                criptograma = Criptograma(place, interaction)
                if (player.check_inventary(criptograma.requirement)) == True:
                    criptograma.show_abecedario()
                    criptograma.comprobacion(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{criptograma.requirement}')
        elif self.sala == 2:
            place = 2
            if interaction == 0:
                logica = Logica(place, interaction)
                if (player.check_inventary(logica.requirement)) == True:
                    user_input = input('-->')
                    logica.validar_respuesta(user_input, player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{logica.requirement}')
            elif interaction == 1:
                Quizizz(place, interaction).preguntas(player)
            else:
                Memoria(place, interaction).memoria_rip(player)

        elif self.sala == 3:
            place = 3
            if interaction == 0:
                if (player.check_inventary(Booleanos(place, interaction).requirement)) == True:
                    Booleanos(place, interaction).validacion_input(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{Booleanos(place, interaction).requirement}')
        else:
            place = 4
            if interaction == 0:

                if (player.check_inventary(Libre(place, interaction).requirement)) == True:
                    Libre(place, interaction).comprobar_respuesta(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{Libre(place, interaction).requirement}')

            elif interaction == 1:
                if (Mezclados.check_inventary(Mezclados(place, interaction).requirement)) == True:
                    Mezclados(place, interaction).mezclar(player)
                else:
                    print(f'No tienes los objetos necesarios, necesitas{Mezclados(place, interaction).requirement}')

            else:
                if (Mezclados.check_inventary(EscogeNumero(place, interaction).requirement)) == True:

                    EscogeNumero(place, interaction).numero_random(player)

                else:
                    print(f'No tienes los objetos necesarios, necesitas{(EscogeNumero(place, interaction).requirement)}')



                          