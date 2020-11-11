# -*- coding: utf-8 -*-

#Funções
import math
import pygame
from Configurações import Config

CONFIG = Config()
TEXTOS = Config.textos()
CORES = Config.cores()

def primeira_tela():
    #apresenta a primeira tela

    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)

    #textos da primeira tela
    titulo_do_jogo = fonte_texto_tela_inicial.render(CONFIG.titulo, True, CORES.vermelho)