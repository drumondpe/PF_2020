# -*- coding: utf-8 -*-

#Funções
import math
import pygame
from Configurações import Config
from Configurações import Textos
from Configurações import Cores

from Jogo import tela

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()
def primeira_tela(tela):
    #apresenta a primeira tela

    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)

    #textos da primeira tela
    titulo_do_jogo = fonte_texto_tela_inicial.render(CONFIG.titulo, True, CORES.vermelho)



    #posição na primeira tela
    tela.blit(titulo_do_jogo())



def eventos(RODAR):

    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            RODAR = False
            break
