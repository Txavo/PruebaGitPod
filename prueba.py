import random

palabras = ["árbol", "ordenador", "teclado", "ratón", "monitor"]

class Ahorcado:
    def __init__(self):
        self.palabra_secreta = random.choice(palabras)
        self.letras_acertadas = ["_" for _ in self.palabra_secreta]
        self.fallos = 0
        self.MAX_FALLOS = 6

    def jugar(self):
        while True:
            letra = input("Introduce una letra: ")
            if letra in self.palabra_secreta:
                for i in range(len(self.palabra_secreta)):
                    if self.palabra_secreta[i] == letra:
                        self.letras_acertadas[i] = letra
            else:
                self.fallos += 1
            
            print(f"Letras acertadas: {''.join(self.letras_acertadas)}")
            if self.fallos >= self.MAX_FALLOS:
                print(f"Has perdido. La palabra secreta era {self.palabra_secreta}.")
                break
            elif all(letra in self.letras_acertadas for letra in self.palabra_secreta):
                print("¡Felicidades, has adivinado la palabra secreta!")
                break

ahorcado = Ahorcado()
ahorcado.jugar()
