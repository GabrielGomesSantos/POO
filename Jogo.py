import os
import random as r

def cls():
    os.system('cls')

class Personagem:
    def __init__(self, pos_init_x, pos_init_y):
        self.pos_x = pos_init_x
        self.pos_y = pos_init_y
        self.pontos = 0
        self.rounds = 0

    def avancar(self):
        if self.pos_y < 2:
            self.pos_y += 1
            self.rounds += 1
            self.pontos += 20
            self.detectionColide()

        else:
            self.reset()
            print("Game Over!!")

    def retroceder(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.rounds += 1
            self.pontos += 20
            self.detectionColide()

        else:
            self.reset()
            print("Game Over!!")

    def direita(self):
        if self.pos_x < 2:
            self.pos_x += 1
            self.rounds += 1
            self.pontos += 20
            self.detectionColide()

        else:
            self.reset()
            print("Game Over!!")

    def esquerda(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.rounds += 1
            self.pontos += 20
            self.detectionColide()

        else:
            self.reset()
            print("Game Over!!")

    def atual(self):
        return self.pos_x, self.pos_y

    def reset(self):
        self.pontos = 0
        self.pos_x = 0
        self.pos_y = 0
        self.rounds = 0

    def status(self):
        return self.pontos

    def detectionColide(self):
        if (self.pos_x == pedra1.posicao_obstaculo_x and self.pos_y == pedra1.posicao_obstaculo_y):
            self.reset()
            print("Você colidiu com um obstáculo! Pontos resetados.")

class Mapa:
    def __init__(self):
        self.mapa = [[" " for _ in range(3)] for _ in range(3)]

    def atualizar_mapa(self, pos_x, pos_y, pos_obt_x, pos_obt_y):
        self.mapa = [[" " for _ in range(3)] for _ in range(3)]
        self.mapa[pos_y][pos_x] = "P"
        self.mapa[pos_obt_y][pos_obt_x] = "X"

    def mostrar(self):
        for linha in self.mapa:
            print("|" + "|".join(linha) + "|")

class Obstaculo:
    def __init__(self):
        self.posicao_obstaculo_x = r.randint(0, 2)
        self.posicao_obstaculo_y = r.randint(0, 2)

    def obst(self):
        return self.posicao_obstaculo_y, self.posicao_obstaculo_x

# Definições
peter = Personagem(0, 0)
mapa = Mapa()
pedra1 = Obstaculo()


while peter.rounds <= 10:
    cls()
    posicao_personagem_x, posicao_personagem_y = peter.atual()
    posicao_obstaculo_x, posicao_obstaculo_y = pedra1.obst()
    mapa.atualizar_mapa(
        posicao_personagem_x, posicao_personagem_y, posicao_obstaculo_y, posicao_obstaculo_x
    )

    print(f"Rounds: {peter.rounds} \nPontos: {peter.status()}")
    mapa.mostrar()
    resposta = input("Use W, A, S, D para se mover\n")

    if resposta == "s":
        peter.avancar()
    elif resposta == "w":
        peter.retroceder()
    elif resposta == "d":
        peter.direita()
    elif resposta == "a":
        peter.esquerda()
