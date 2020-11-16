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
        self.imagem_diminui = pygame.transform.scale(self.imagemimagem, (LARGURA_alien, ALTURA_alien))
        self.imagem.set_colorkey((CORES.preto))

        self.alien_x = 100
        self.alien_y = -ALTURA_alien
        self.alien_velocidadeX = 3
        self.alien_velocidadeY = 1


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (METEOR_WIDTH, METEOR_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, -METEOR_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)