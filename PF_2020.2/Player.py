# -*- coding: utf-8 -*-

import pygame
import time
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Nave(pygame.sprite.Sprite):
    #classe do player

    def __init__(self, CONFIG, sprites, disparos_sprite, disparos_sprite_nave):
        super().__init__()

        self.CONFIG = CONFIG
        self.NAVE_largura = 50
        self.NAVE_altura = 50

        self.imagem_grande = pygame.image.load('Nave.png').convert_alpha() #mudar
        self.image = pygame.transform.scale(self.imagem_grande, (self.NAVE_largura, self.NAVE_altura))
        self.rect = self.image.get_rect()
        self.rect.centerx = CONFIG.largura_tela / 2
        self.rect.bottom = CONFIG.altura_tela - 10
        self.velocidadeX = 0
        self.aceleracaoX = 3 #controla a velocidade da nave
        self.vidas = 3

        self.sprites = sprites
        #disparo da nave
        self.disparos_sprite = disparos_sprite
        self.disparos_sprite_nave = disparos_sprite_nave
        self.imagem_disparo = pygame.image.load('Disparo.png').convert_alpha()
        self.imagem_disparo = pygame.transform.scale(self.imagem_disparo, (25, 25))
        
    
    def update(self):
        #atualiza a posição da nave
        self.rect.x += self.velocidadeX

        #Mantem dentro da tela
        if self.rect.right > CONFIG.largura_tela:
            self.rect.right = CONFIG.largura_tela
        if self.rect.left < 0:
            self.rect.left = 0
    
    def tiro(self):
        novo_disparo = Disparo(self.imagem_disparo, self.rect.top, self.rect.centerx)
        self.sprites.add(novo_disparo)
        self.disparos_sprite_nave.add(novo_disparo)

class Disparo(pygame.sprite.Sprite):
    #classe do disparo
    def __init__(self, imagem, baixo, centerx): #se pá mudar para 'image'
        pygame.sprite.Sprite.__init__(self)

        self.image = imagem #se pá mudar para 'image'
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = baixo
        self.speedy = -10 #vel do disparo

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill() #tiro desaparece se passar do topo da tela