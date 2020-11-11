# -*- coding: utf-8 -*-
"""
Autores: Luiz Durand, Henrry Miguel e Pedro Drumond
"""
import pygame

from Configurações import Config

CONFIG = Config()
TEXTOS = Textos()

def rodar_jogo():
    #inicializa o jogo
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
    relogio = pygame.time.Clock()
    