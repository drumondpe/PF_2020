# -*- coding: utf-8 -*-

#Configurações

import math
import pygame
vetor = pygame.math.Vector2

class Configurações():
    #define as configurações básicas
    def __init__(self):
        self.titulo = 'Star Fight'

        self.largura_tela = 600
        self.altura_tela = 670

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

class Textos(): 
    #define tamanho e fonte dos textos
    def __init__(self):

        self.fonte = 'Futura ZBlk BT'
        self.tamanho_grande = 56
        self.tamanho_pequeno = 40


