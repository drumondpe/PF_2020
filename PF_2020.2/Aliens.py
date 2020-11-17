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
        self.imagem = pygame.image.load('Alien.png').convert_alpha() #carrega a imagem
        self.imagem_diminui = pygame.transform.scale(self.imagemimagem, (LARGURA_alien, ALTURA_alien)) #muda o tamanho da imagem
        self.imagem.set_colorkey((CORES.preto))

        self.rect = self.imagem_diminui.get_rect()
        self.rect.x = 100
        self.rect.y = -ALTURA_alien
        self.alien_velocidadeX = 3
        self.alien_velocidadeY = 1


    def atualiza_posicao_ALIENS(self):
        #atualiza a posição do alien  
        self.rect.x += self.alien_velocidadeX
        self.rect.y += self.alien_velocidadeY
