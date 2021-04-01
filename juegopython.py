import requests
import random


#int(float((frase.split()[4]).replace(",", ".")))

api = requests.get("https://api-escapamet.vercel.app")



n = 1

if n == 1:
  question = (api.json()[0]["objects"][1]["game"]["questions"][0]["question"])
  print(question)
  variable = question.split('')[4] 
  answer = input('Ingresa tu código: ')
  if variable in answer:
    variable = question.split('"')[1]
    print(eval(answer))
    if eval(answer) == 50:
      print('nice')
    else:
      print('mal')
  else:
    print('no usaste la variable dada')
else:
  question = (api.json()[0]["objects"][1]["game"]["questions"][0]["question"])
  print(question)
  frase = question.split('"')[1]
