import random
import os

def run():
    IMAGENES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    DB = [
        "C",
        "PYTHON",
        "JS",
        "JAVA",
        "PHP"
    ]
    
    palabras = random.choice(DB) #marco una palabra aletoria
    espacios = ["_"]* len(palabras) #le marco cuantos _ va a tener cada palabra
    intentos = 6
    
    while True:
        os.system("cls")
        for caracter in espacios:
            print(caracter,end=" ")
        print(IMAGENES[intentos])
        letra = input("Elige una letra: ").upper()
        
        encontro = False
        for idx , caracter in enumerate(palabras):
            if caracter == letra:
                espacios[idx] = letra
                encontro = True
        
        if not encontro:
            intentos -=1
        if "_" not in espacios:
            os.system("cls")
            print("Ganaste")
            break
        if intentos == 0:
            os.system("cls")
            print("Perdiste")
            break
         
    
if __name__ == "__main__":
    run()