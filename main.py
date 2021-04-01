import requests
import random

api = requests.get("https://api-escapamet.vercel.app")

def datos_jugador():
  name = input('Ingrese su nombre de usuario(máx 10 caracteres)\n-->')
  while name == '' or len(name) > 10:
    name = input('Ingreso incorrecto. Ingrese su nombre de usuario(máx 10 caracteres)\n-->')




def main():
  datos_jugador()
main()
