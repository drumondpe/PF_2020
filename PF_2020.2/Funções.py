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
def primeira_tela(tela): #apresenta a primeira tela

    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    fonte_texto_medio = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_medio)

    #textos da primeira tela
    titulo_do_jogo = fonte_texto_tela_inicial.render(CONFIG.titulo, True, CORES.vermelho)
    barra_comecar = fonte_texto_medio.render('Barra de Espaço para começar!', True, CORES.azul_marinho)
    #barra_comecar2 = fonte_texto_tela_inicial.render('para começar!', True, CORES.azul_marinho)
    nome_criador1 = fonte_texto_nomes.render('Henrry Miguel', True, CORES.verde)
    nome_criador2 = fonte_texto_nomes.render('Luiz Durand', True, CORES.verde)
    nome_criador3 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.verde)
    insper = fonte_texto_nomes.render('ENG - INSPER 2020.2', True, CORES.vermelho)

    #posição na primeira tela
    ###PUXAR A TELA LÁ DE JOGO
    tela.fill(CORES.preto) #preenche a tela com a cor preta
    #preenche a tela com frases
    tela.blit(titulo_do_jogo, (CONFIG.largura_tela // 2 - titulo_do_jogo.get_width() // 2, 85))
    tela.blit(barra_comecar, (CONFIG.largura_tela // 2 - barra_comecar.get_width() // 2, 180))
    tela.blit(nome_criador1, (CONFIG.largura_tela // 2 - nome_criador1.get_width() // 2, 480))
    tela.blit(nome_criador2, (CONFIG.largura_tela // 2 - nome_criador2.get_width() // 2, 520))
    tela.blit(nome_criador3, (CONFIG.largura_tela // 2 - nome_criador3.get_width() // 2, 560))
    tela.blit(insper, (CONFIG.largura_tela // 2 - insper.get_width() // 2, 600))

def segunda_tela(tela): #apresenta a segunda tela
    #para add textos mexer aqui
    textos = pygame.font.SysFont(TEXTOS.fonte, TEXTOS)
    #para mexer na tela, mexer aqui 
    fundo = pygame.image.load('Fundo_galáxia').convert()

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

        