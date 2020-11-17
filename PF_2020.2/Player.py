# -*- coding: utf-8 -*-

import pygame
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Nave(pygame.sprite.Sprite):
    #classe do player

    def __init__(self, tela, CONFIG):

        self.tela = tela
        self.CONFIG = CONFIG
        self.NAVE_largura = 30
        self.NAVE_altura = 20

        self.imagem = pygame.image.load('Nave.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (self.NAVE_largura, self.NAVE_altura))
        self.rect = self.imagem.get_rect()
        self.rect.centerx = CONFIG.largura_tela / 2
        self.rect.bottom = CONFIG.altura_tela - 10
        self.velocidadeX = 0
        self.aceleracaoX = 5
    
    def atualiza_posicao_NAVE(self):
        #atualiza a posição da nave
        self.rect.x += self.velocidadeX

        #Mantem dentro da tela
        if self.rect.right > CONFIG.largura_tela:
            self.rect.right = CONFIG.largura_tela
        if self.rect.left < 0:
            self.rect.left = 0