# -*- coding: utf-8 -*-
"""
Autores: Luiz Durand, Henrry Miguel e Pedro Drumond
"""
import pygame

from Configurações import Config
from Configurações import Textos
from Configurações import Cores
import Funções as funcoes

CONFIG = Config()
TEXTOS = Textos()
RODAR = True

def rodar_jogo():
    #inicializa o jogo
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
    relogio = pygame.time.Clock()

    #booleanos para jogar

    TELA_INICIO = True

    #precisa iniciar os objetos aqui
    ###

    #apresenta tela inicial
    funcoes.primeira_tela(tela)

while RODAR:
    rodar_jogo()

    funcoes.eventos(RODAR)

    






