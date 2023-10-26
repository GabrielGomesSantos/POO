import os

def cls():
    os.system('cls')

class Personagem: 
    def __init__(self, pos_init_x, pos_init_y):
        self.pos_x = pos_init_x
        self.pos_y = pos_init_y
        self.pontos = 0 

    def avancar(self):
        if self.pos_y < 2:
            self.pos_y += 1

    def retroceder(self):
        if self.pos_y > 0:
            self.pos_y -= 1

    def direita(self):
        if self.pos_x < 2:
            self.pos_x += 1

    def esquerda(self):
        if self.pos_x > 0:
            self.pos_x -= 1

    def atual(self):
        return self.pos_x, self.pos_y
    
    def reset(self):
        self.pontos = 0
        self.pos_x = 0
        self.pos_y = 0
           
    
    def status(self):
        if 0 <= self.pos_x < 3 and 0 <= self.pos_y < 3:
            self.pontos += 20
            return self.pontos
        else:
            self.reset

class Mapa: 
    def __init__(self):
        self.mapa = [[' ' for _ in range(3)] for _ in range(3)]
        
    def atualizar_mapa(self, pos_x, pos_y):
        self.mapa = [[' ' for _ in range(3)] for _ in range(3)]
        self.mapa[pos_y][pos_x] = 'P'

    def mostrar(self):
        for linha in self.mapa:
            print("|" + "|".join(linha) + "|")

# Definições
peter = Personagem(0, 0)
mapa = Mapa()

while True:
    cls()
    posicao_x, posicao_y = peter.atual()
    print(f"Pontos: {peter.status()}")
    mapa.atualizar_mapa(posicao_x, posicao_y)
    mapa.mostrar()
    resposta = input("Para qual direção você moverá\nS - Frente\nW - Trás\nD - Direita\nA - Esquerda\nOpção: ")

    if resposta == "s": 
        peter.avancar()

    elif resposta == "w":
        peter.retroceder()

    elif resposta == "d":
        peter.direita()

    elif resposta == "a":
        peter.esquerda()