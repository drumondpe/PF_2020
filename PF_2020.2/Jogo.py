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
from Aliens import Alien
import Funções as funcoes

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()
ALIEN = Alien()
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


    ### INICIA OBJETOS ###
    NAVE = Nave(tela, CONFIG)

    Aliens = pygame.sprite.Group()
    for cada_alien in range (10):
        alien = ALIEN(tela) #precisa da tela aq?
        Aliens.add(alien)


    #apresenta tela inicial
    funcoes.primeira_tela(tela)
    #pygame.mixer.music.load('xxx')
    #pygame.mixer.music.play()
    
    while RODAR:
        
        #atualiza os booleanos
        RODAR, TELA_INICIAL, TELA_SEGUNDA = funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA)

        if TELA_SEGUNDA and not TELA_INICIAL: #isso vai ficar rodando infinitamente, então a cada passagem vai "blitar" a nave? como arrumar?
        
            tela.fill(CORES.preto)
            #mapa
            segunda_tela = funcoes.segunda_tela(tela)

            Aliens.update() #atualiza a posição dos Aliens
            Aliens.draw(tela) #desenha todos os Aliens
            
            funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA) #verifica os eventos

            NAVE.atualiza_posicao_NAVE() #atualiza a posição da nave

            tela.blit(NAVE.imagem, NAVE.rect) #mostra a nave na tela

            pygame.display.update()
        



        pygame.display.flip()

rodar_jogo()





