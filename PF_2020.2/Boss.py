# -*- coding: utf-8 -*-
import pygame
import random #mudar dps
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Death_star(pygame.sprite.Sprite):
    #classe que define a Estrela da Morte
    def __init__(self, CONFIG, sprites, disparos_sprite): #disparos_sprite
        super().__init__()

        self.CONFIG = CONFIG
        self.DEATH_STAR_largura = 200
        self.DEATH_STAR_altura = 200

        self.imagem_grande = pygame.image.load('Estrela-da-morte2.png').convert_alpha() #mudar
        self.image = pygame.transform.scale(self.imagem_grande, (self.DEATH_STAR_largura, self.DEATH_STAR_altura))
        self.rect = self.image.get_rect()
        self.rect.centerx = CONFIG.largura_tela / 2
        self.rect.bottom = CONFIG.altura_tela - 10
        self.movimento_direcao = 1
        self.movimento_contador = 0
        self.aceleracaoX = 2.5 #controla a velocidade do boss
        self.vidas = 10

        self.sprites = sprites
        #disparo da Death Star
        self.disparos_sprite = disparos_sprite
        self.imagem_disparo = pygame.image.load('Disparo2.png').convert_alpha()
        self.imagem_disparo = pygame.transform.scale(self.imagem_disparo, (25, 25))
 
    def update(self): #MUDAR
        #atualiza a posição da estrela da morte
        self.rect.x += self.movimento_direcao

        #Mantem dentro da tela
        self.movimento_contador += 6 #velocidade do boss
        if self.movimento_contador == 600:
            self.movimento_contador = 0
            self.movimento_direcao *= -1

        # novas posições e velocidades, talvez apagar***
        if self.rect.top > CONFIG.altura_tela or self.rect.right < 0 or self.rect.left > CONFIG.largura_tela:
            self.rect.x = random.randint(0, CONFIG.largura_tela-20) #LARGURA_alien = 20
            self.rect.y = random.randint(-100, -30) #ALTURA_alien = 30
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)


    def tiro(self):
        novo_disparo2 = Disparo2(self.imagem_disparo, self.rect.top, self.rect.centerx)
        self.sprites.add(novo_disparo2)
        self.disparos_sprite.add(novo_disparo2)

class Disparo(pygame.sprite.Sprite):
    #classe do disparo
    def __init__(self, imagem, baixo, centerx): #se pá mudar para 'image'
        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = baixo
        self.speedy = -10 #vel do disparo

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill() #tiro desaparece se passar da tela