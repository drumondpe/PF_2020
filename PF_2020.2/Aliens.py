# -*- coding: utf-8 -*-

import pygame
import random #mudar dps
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Alien(pygame.sprite.Sprite):
    #classe que define os aliens 

    def __init__(self, x, y):
        super().__init__()
        LARGURA_alien = 50
        ALTURA_alien = 50
        self.imagem_grande = pygame.image.load('Alien.png').convert_alpha() #carrega a imagem
        self.image = pygame.transform.scale(self.imagem_grande, (LARGURA_alien, ALTURA_alien)) #muda o tamanho da imagem
        self.image.set_colorkey((CORES.preto))

        self.rect = self.image.get_rect()
        #self.rect.x = 100
        #self.rect.y = -ALTURA_alien
        self.rect.center = [x, y]

        self.movimento_contador = 0
        self.movimento_direcao = 1


        #self.speedx = random.randint(-3, 3)
        #self.speedy = random.randint(2, 9)


    def update(self):
        #atualiza a posição do alien  
        self.rect.x += self.movimento_direcao
        self.rect.y += self.movimento_direcao #talvez mudar aqui
        self.movimento_contador += 1
        if abs(self.movimento_contador) > 75: #mexer aqui para movimentação
            self.movimento_direcao *= -1
            self.movimento_contador *= self.movimento_direcao
            self.rect.y += self.movimento_direcao

        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > CONFIG.altura_tela or self.rect.right < 0 or self.rect.left > CONFIG.largura_tela:
            self.rect.x = random.randint(0, CONFIG.largura_tela-20) #LARGURA_alien = 20
            self.rect.y = random.randint(-100, -30) #ALTURA_alien = 30
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)
