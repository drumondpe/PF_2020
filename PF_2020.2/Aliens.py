# -*- coding: utf-8 -*-

import pygame
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Alien(pygame.sprite.Sprite):
    #classe que define os aliens 

    def __init__(self, tela):
        self.tela = tela
        
        LARGURA_alien = 20
        ALTURA_alien = 30
        self.imagem = pygame.image.load('Alien.png')convert_alpha() #carrega a imagem
        #self.imagem = pygame.transform.scale(self.imagem, (23, 23)) #muda o tamanho da imagem
        self.imagem_diminui = pygame.transform.scale(imagem, (LARGURA_alien, ALTURA_alien))
        self.imagem.set_colorkey((CORES.preto))

        self.alien_x = 100
        self.alien_y = -ALTURA_alien
        self.alien_velocidadeX = 3
        self.alien_velocidadeY = 1
