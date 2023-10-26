import os

def cls():
    os.system('cls')

class Personagem:
    def __init__(self, pos_init_x, pos_init_y):
        self.pos_x = pos_init_x
        self.pos_y = pos_init_y

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

class Mapa:
    def __init__(self):
        self.mapa = [[' ' for _ in range(3)] for _ in range(3)]

    def atualizar_mapa(self, pos_x, pos_y):
        # Limpa o mapa anterior
        self.mapa = [[' ' for _ in range(3)] for _ in range(3)]
        # Coloca o personagem no mapa
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
    mapa.atualizar_mapa(posicao_x, posicao_y)
    mapa.mostrar()
    resposta = input("Para qual direção você moverá\n1 - Frente\n2 - Trás\n3 - Direita\n4 - Esquerda\n5 - Sair\nOpção: ")

    match resposta:
    
        case "1":
            peter.avancar()
        case "2":
            peter.retroceder()
        case "3":
            peter.direita()
        case "4":
            peter.esquerda()
        case "5":
            break
