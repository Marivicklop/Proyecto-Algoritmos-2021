import requests
import random

api = requests.get("https://api-escapamet.vercel.app")


question = random.choice(api.json()[1]["objects"][0]["game"]["questions"])

answer = (question["answer"]).lower()

print(question["question"])

print(answer)

#def show_letters(letters):
#  print(f'''
#   -------------------------------------
#  |                                    |
#  |         {''.join(letters)}         |
#  |                                    |
#  |                                    |
#   -------------------------------------
#  ''')

user_answer = input('--> ').lower()

m = len(answer)

lineas = '_ ' * m
letras = lineas.split()
print(letras)

var texto = answer
console.log(texto.match(/.{1,4}(.$)?/g));








    

