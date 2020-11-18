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

    def __init__(self):
        super().__init__()
        LARGURA_alien = 20
        ALTURA_alien = 30
        self.imagem_grande = pygame.image.load('Alien.png').convert_alpha() #carrega a imagem
        self.image = pygame.transform.scale(self.imagem_grande, (LARGURA_alien, ALTURA_alien)) #muda o tamanho da imagem
        self.image.set_colorkey((CORES.preto))

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = -ALTURA_alien
        #self.alien_velocidadeX = 3 #voltar dps
        #self.alien_velocidadeY = 1 #voltar dps
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)


    def update(self):
        #atualiza a posição do alien  
        #self.rect.x += self.alien_velocidadeX #voltar dps
        #self.rect.y += self.alien_velocidadeY #voltar dps
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > CONFIG.altura_tela or self.rect.right < 0 or self.rect.left > CONFIG.largura_tela:
            self.rect.x = random.randint(0, CONFIG.largura_tela-20) #LARGURA_alien = 20
            self.rect.y = random.randint(-100, -30) #ALTURA_alien = 30
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)
