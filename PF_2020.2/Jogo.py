# -*- coding: utf-8 -*-

### Próximos passos ###
#arrumar o layout da tela de jogo
#começar os disparos

### Problemas ### 
#não está mudando de tela após apertar K_SPACE

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

pygame.init()
pygame.mixer.init()

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()
RODAR = True

def rodar_jogo():
    #inicializa o jogo
    tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
    pygame.display.set_caption('Space Invaders')
    relogio = pygame.time.Clock()

    #booleanos para jogar
    RODAR = True
    TELA_INICIAL = True
    TELA_SEGUNDA = False
    COLISAO_ALIEN = False #usar para quando houver colisão do alien com a nave
    COLISAO_DISPARO = False #usar para quando houver colisão do disparo da nave com o alien
    TELA_GAME_OVER = False


    ### INICIA OBJETOS ###
    NAVE = Nave(CONFIG)

    sprites = pygame.sprite.Group()
    aliens_colisao = pygame.sprite.Group()
    for cada_alien in range (10):
        alien = Alien()
        sprites.add(alien)
        aliens_colisao.add(alien)

    nave = NAVE
    sprites.add(nave)
    

    funcoes.primeira_tela(tela)
    #pygame.mixer.music.load('xxx')
    #pygame.mixer.music.play()
    
    while RODAR:
        #atualiza os booleanos
        RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER = funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER, NAVE)

        if TELA_SEGUNDA and not TELA_INICIAL and not TELA_GAME_OVER: #isso vai ficar rodando infinitamente, então a cada passagem vai "blitar" a nave? como arrumar?
        
            tela.fill(CORES.preto)
            #mapa
            segunda_tela = funcoes.segunda_tela(tela, NAVE)

            sprites.update()
            sprites.draw(tela) #desenha todos

            RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER = funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER, NAVE) #verifica os eventos
            
            colisao = pygame.sprite.spritecollide(NAVE, aliens_colisao, True) #verifica se houve colisão
            
            if len(colisao)>0: #reduz as vidas conforme as colisões
                NAVE.vidas -= 1

            if NAVE.vidas <= 0:
                TELA_SEGUNDA = False
                TELA_GAME_OVER = True
            
        if TELA_GAME_OVER and not TELA_INICIAL and not TELA_SEGUNDA: #vai para a tela game_over 
            
            game_over_tela = funcoes.gameover_tela(tela) #não está mudando de tela

            RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER = funcoes.eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER, NAVE) #verifica os eventos

                





            pygame.display.update()
        



        pygame.display.flip()

rodar_jogo()





