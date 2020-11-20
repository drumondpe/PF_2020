# -*- coding: utf-8 -*-

#Configurações

import math
import pygame
vetor = pygame.math.Vector2

INIT = 0
GAME = 1
GAME_OVER = 2
VENCEDOR = 3
QUIT = 4

class Config():
    #define as configurações básicas
    def __init__(self):
        self.titulo = 'X-Wing Fight'

        self.largura_tela = 1000
        self.altura_tela = 650

        self.cores = Cores()
        self.textos = Textos()

class Cores():
    #define as cores básicas
    def __init__(self):
        self.vermelho = (255, 0, 0)
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.aqua = (0, 128, 128)
        self.azul_marinho = (0, 0, 128)
        self.verde = (0, 255, 0)
        self.laranja = (255, 165, 0)
        self.amarelo = (255, 255, 0)
        self.rosa = (255, 0, 255)
        self.nomes = (220, 0, 0)
        self.roxo = (220, 0, 255)

class Textos(): 
    #define tamanho e fonte dos textos
    def __init__(self):

        self.fonte = 'Futura ZBlk BT'
        self.tamanho_grande = 75
        self.tamanho_medio = 55
        self.tamanho_nome = 30
        self.tamanho_vidas = 25


