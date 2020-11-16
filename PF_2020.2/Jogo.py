# -*- coding: utf-8 -*-

#fazer a movimentação do Player
#avançar com a classe dos Aliens 
#começar os disparos

"""
Autores: Luiz Durand, Henrry Miguel e Pedro Drumond
"""
import pygame

from Configurações import Config
from Configurações import Textos
from Configurações import Cores
from Player import Nave
import Funções as funcoes

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()
RODAR = True

def rodar_jogo():
    #inicializa o jogo
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
    pygame.display.set_caption('Space Invaders')
    relogio = pygame.time.Clock()

    #booleanos para jogar
    RODAR = True
    TELA_INICIAL = True
    TELA_SEGUNDA = False
    COLISAO_ALIEN = False #usar para quando houver colisão do alien com a nave
    COLISAO_DISPARO = False #usar para quando houver colisão do disparo da nave com o alien


    #inicia objetos
    NAVE = Nave(tela, CONFIG)

    #apresenta tela inicial
    funcoes.primeira_tela(tela)
    #pygame.mixer.music.load('xxx')
    #pygame.mixer.music.play()
    
    while RODAR:
        
        #atualiza os booleanos
        RODAR, TELA_INICIAL, TELA_SEGUNDA = funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA)

        if TELA_SEGUNDA and not TELA_INICIAL: #and not, and not...
        
            tela.fill(CORES.preto)
            #mapa
            segunda_tela = funcoes.segunda_tela(tela)

            NAVE.atualiza_posicao_NAVE() #atualiza a posição da nava

            tela.blit(NAVE.imagem, NAVE.rect) #mostra a nave na tela
        



        pygame.display.flip()

rodar_jogo()





