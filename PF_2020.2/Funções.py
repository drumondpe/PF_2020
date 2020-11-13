# -*- coding: utf-8 -*-

#Funções
import math
import pygame
from Configurações import Config
from Configurações import Textos
from Configurações import Cores


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
    ###PUXAR A TELA LÁ DE JOGO
    tela.fill(CORES.preto) #preenche a tela com a cor preta
    tela.blit(titulo_do_jogo, (CONFIG.largura_tela // 2 - titulo_do_jogo.get_width() // 2, 90))

def eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA):

    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            RODAR = False
            break

        #se a tela inicial for True, vai verificar:
        if TELA_INICIAL: #puxar essa variável lá de jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #se pressionar barra de espaço, mudará para a próxima tela
                    #pygame.mixer.music.load('xxx') pega outra musica
                    #pygame.mixer.music.play() load nova música

                    TELA_INICIAL = False
                    TELA_SEGUNDA = True

        #elif TELA_SEGUNDA:
            #aqui vamos criar movimentação e importar o player e mobs


    return RODAR, TELA_INICIAL, TELA_SEGUNDA

        