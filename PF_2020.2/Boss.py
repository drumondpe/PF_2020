# -*- coding: utf-8 -*-
import pygame
import random #mudar dps
import time
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()

class Death_star(pygame.sprite.Sprite):
    #classe que define a Estrela da Morte
    def __init__(self, CONFIG, sprites, disparos_sprite, disparos_sprite_boss): #disparos_sprite
        super().__init__()

        self.CONFIG = CONFIG
        self.DEATH_STAR_largura = 200
        self.DEATH_STAR_altura = 200

        self.imagem_grande = pygame.image.load('Estrela-da-morte2.png').convert_alpha() #mudar
        self.image = pygame.transform.scale(self.imagem_grande, (self.DEATH_STAR_largura, self.DEATH_STAR_altura))
        self.rect = self.image.get_rect()
        self.rect.centerx = CONFIG.largura_tela / 2
        self.rect.bottom = CONFIG.altura_tela - 400
        self.movimento_direcao = 1
        self.movimento_contador = 0
        self.aceleracaoX = 2.5 #controla a velocidade do boss
        self.vidas = 100

        self.sprites = sprites
        #disparo da Death Star
        self.disparos_sprite = disparos_sprite
        self.disparos_sprite_boss = disparos_sprite_boss
        self.imagem_disparo = pygame.image.load('Disparo2.png').convert_alpha()
        self.imagem_disparo = pygame.transform.scale(self.imagem_disparo, (25, 25))

        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 1200 #tempo para atirar

    def update(self): #MUDAR
        #atualiza os disparos
        now = pygame.time.get_ticks() #momento atual
        elapsed_ticks = now - self.last_update  #quantos ticks se passaram desde a ultima mudança de frame

        #se já está na hora de mudar de imagem executa
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            self.disparou = self.tiro() #funcao que faz boss atirar (Death_star.tiro())

        #atualiza a posição da estrela da morte
        self.rect.x += self.movimento_direcao

        #Mantem dentro da tela
        self.movimento_contador += 5 #velocidade do boss
        if self.movimento_contador == 1100:
            self.movimento_contador = 0
            self.movimento_direcao *= -1

    def tiro(self):
        novo_disparo2 = Disparo2(self.imagem_disparo, self.rect.bottom, self.rect.centerx)
        self.sprites.add(novo_disparo2)
        self.disparos_sprite.add(novo_disparo2)
        self.disparos_sprite_boss.add(novo_disparo2)

class Disparo2(pygame.sprite.Sprite):
    #classe do disparo
    def __init__(self, imagem, baixo, centerx): #se pá mudar para 'image'
        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = baixo
        self.speedy = 5 #vel do disparo

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill() #tiro desaparece se passar da tela