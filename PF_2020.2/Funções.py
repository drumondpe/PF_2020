# -*- coding: utf-8 -*-
import math
import pygame
import time
from Configurações import Config
from Configurações import Textos
from Configurações import Cores
from Configurações import INIT, GAME, GAME_OVER, QUIT, BOSS
from Player import Nave
from Aliens import Alien
from Boss import Death_star


linhas = 7 #serão usadas para construir a nave
colunas = 10 #serão usadas para construir a nave

CONFIG = Config() #importa as classes das Configurações
TEXTOS = Textos()
CORES = Cores()

def primeira_tela(tela): #apresenta a primeira tela

    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    fonte_texto_medio = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_medio)

    #textos da primeira tela
    titulo_do_jogo = fonte_texto_tela_inicial.render(CONFIG.titulo, True, CORES.rosa)
    instrucao = fonte_texto_medio.render('Destrua os caças Tie!', True, CORES.roxo)
    barra_comecar = fonte_texto_medio.render('Barra de espaço para começar', True, CORES.roxo)
    comandos = fonte_texto_medio.render('A/D para andar e Barra de espaço para atirar', True, CORES.roxo)
    nome_criador1 = fonte_texto_nomes.render('Henrry Miguel', True, CORES.nomes)
    nome_criador2 = fonte_texto_nomes.render('Luiz Durand', True, CORES.nomes)
    nome_criador3 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.nomes)
    insper = fonte_texto_nomes.render('ENG - INSPER 2020.2', True, CORES.vermelho)

    #posição na primeira tela
    tela.fill(CORES.preto) #preenche a tela com a cor preta
    fundo = pygame.image.load('Fundo_galáxia.png').convert()
    fundo = pygame.transform.scale(fundo, (CONFIG.largura_tela, CONFIG.altura_tela))
    tela.blit(fundo, (0, 0)) #preenche a tela com imagem

    #preenche a tela com frases
    tela.blit(titulo_do_jogo, (CONFIG.largura_tela // 2 - titulo_do_jogo.get_width() // 2, 60))
    tela.blit(instrucao, (CONFIG.largura_tela // 2 - instrucao.get_width() // 2, 180))
    tela.blit(barra_comecar, (CONFIG.largura_tela // 2 - barra_comecar.get_width() // 2, 250))
    tela.blit(comandos, (CONFIG.largura_tela // 2 - comandos.get_width() // 2, 310))
    tela.blit(nome_criador1, (CONFIG.largura_tela // 2 - nome_criador1.get_width() // 2, 525))
    tela.blit(nome_criador2, (CONFIG.largura_tela // 2 - nome_criador2.get_width() // 2, 550))
    tela.blit(nome_criador3, (CONFIG.largura_tela // 2 - nome_criador3.get_width() // 2, 575))
    tela.blit(insper, (CONFIG.largura_tela // 2 - insper.get_width() // 2, 600))

    #imagens
    imagem_estrela_da_morte = pygame.image.load('Estrela-da-morte2.png').convert_alpha()
    imagem_estrela_da_morte = pygame.transform.scale(imagem_estrela_da_morte, (210, 200)) #dimensão
    tela.blit(imagem_estrela_da_morte, (780, 30)) #posição

    imagem_XWing = pygame.image.load('Nave2.png').convert_alpha()
    imagem_XWing = pygame.transform.scale(imagem_XWing, (340, 200))
    tela.blit(imagem_XWing, (50, 430))

    imagem_tie_fighter = pygame.image.load('Alien2.png').convert_alpha()
    imagem_tie_fighter = pygame.transform.scale(imagem_tie_fighter, (260, 260))
    tela.blit(imagem_tie_fighter, (650, 380))

def segunda_tela(tela, NAVE, pontos): #apresenta a segunda tela (layout)
    #fonte
    fonte_texto_vidas = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    #textos
    restantes = fonte_texto_vidas.render('Vidas restantes: ', True, CORES.rosa)
    pontuacao = fonte_texto_vidas.render('Pontuação: {}'.format(pontos), True, CORES.rosa)

    foto_vida_errada = pygame.image.load('Nave.png').convert_alpha()
    foto_vida = pygame.transform.scale(foto_vida_errada, (30, 30))

    vertices = (0, 0, CONFIG.largura_tela, 40)

    pygame.draw.rect(tela, CORES.preto, vertices)
    tela.blit(restantes, (10, 11))
    tela.blit(pontuacao, (750, 11))


    #desenha uma vida na tela
    posicao = 175
    for vida in range(NAVE.vidas):
        tela.blit(foto_vida, (posicao, 6))
        posicao+=30

def boss_tela(tela, NAVE, pontos, BOSS):
    #fonte
    fonte_texto_vidas = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    #textos
    restantes = fonte_texto_vidas.render('Vidas restantes: ', True, CORES.rosa)
    pontuacao = fonte_texto_vidas.render('Pontuação: {}'.format(pontos), True, CORES.rosa)

    #para mexer na tela, mexer aqui
    #fundo = pygame.image.load('Fundo_galáxia.png').convert()
    #fundo = pygame.transform.scale(fundo, (CONFIG.largura_tela, CONFIG.altura_tela))
    #tela.fill(CORES.preto)
    #tela.blit(fundo, (0, 0)) #preenche o fundo com preto

    #DESENHAR AS NAVES AQUI

    foto_vida_errada = pygame.image.load('Nave.png').convert_alpha()
    foto_vida = pygame.transform.scale(foto_vida_errada, (30, 30))

    vertices = (0, 0, CONFIG.largura_tela, 40)

    pygame.draw.rect(tela, CORES.preto, vertices)
    tela.blit(restantes, (10, 11))
    tela.blit(pontuacao, (750, 11))

    #desenha uma vida na tela
    posicao = 175
    for vida in range(NAVE.vidas):
        tela.blit(foto_vida, (posicao, 6))
        posicao+=30


def cria_aliens(sprites, aliens_colisao): #gera os aliens
    for linha in range(linhas): #acessa a linha
        for item in range(colunas):
            alien = Alien(50 + item * 100, 10 + linha * 70)
            sprites.add(alien)
            aliens_colisao.add(alien)


def gameover_tela(tela):
    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    fonte_texto_medio = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_medio)

    #textos da tela game over
    game_over = fonte_texto_tela_inicial.render('GAME OVER!', True, CORES.vermelho)
    barra_recomeçar = fonte_texto_medio.render('Pressione barra de espaço para recomeçar!', True, CORES.laranja)
    palpatine = pygame.image.load('Palpatine.jpg').convert()
    palpatine = pygame.transform.scale(palpatine, (CONFIG.largura_tela, CONFIG.altura_tela))
    #preenche a tela com frases
    tela.fill(CORES.preto)
    tela.blit(palpatine, (0, 0))
    tela.blit(game_over, (CONFIG.largura_tela // 2 - game_over.get_width() // 2, 180))
    tela.blit(barra_recomeçar, (CONFIG.largura_tela // 2 - barra_recomeçar.get_width() // 2, 380))

def vencedor_tela(tela):
    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    fonte_texto_medio = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_medio)

    #textos da tela game over
    voce_venceu = fonte_texto_tela_inicial.render('VOCÊ VENCEU!', True, CORES.laranja)
    parabens = fonte_texto_medio.render('Parabéns por vencer o Império', True, CORES.laranja)
    barra_recomeçar = fonte_texto_medio.render('Pressione barra de espaço para recomeçar!', True, CORES.laranja)
    rebelde = pygame.image.load('Rebelde.jpg').convert()
    rebelde = pygame.transform.scale(rebelde, (CONFIG.largura_tela, CONFIG.altura_tela))

    tela.fill(CORES.preto)
    tela.blit(rebelde, (0, 0))
    tela.blit(voce_venceu, (CONFIG.largura_tela // 2 - voce_venceu.get_width() // 2, 180))
    tela.blit(parabens, (CONFIG.largura_tela // 2 - parabens.get_width() // 2, 380))
    tela.blit(barra_recomeçar, (CONFIG.largura_tela // 2 - barra_recomeçar.get_width() // 2, 580))

def faz_pontos(soma_ponto):
    aumenta_ponto = 0
    if soma_ponto:
        aumenta_ponto += 10
    return aumenta_ponto

def barra_vida(tela, BOSS):
    if BOSS.vidas > 75:
        barra_vida_cor = CORES.verde
    elif BOSS.vidas > 50:
        barra_vida_cor = CORES.amarelo
    elif BOSS.vidas > 25:
        barra_vida_cor = CORES.laranja
    else:
        barra_vida_cor = CORES.vermelho

    pygame.draw.rect(tela, barra_vida_cor, (450, 30, 200, 13)) #posicao, comprimentoy, comprimentox, largura





def eventos_init(estado):
    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            return QUIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #se pressionar barra de espaço, mudará para a próxima tela

                return GAME
    return estado


def eventos_game_over(estado):
    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            return QUIT

        #vamos ver se o player vai querer jogar de novo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return GAME
    return estado


def eventos_game(estado, NAVE):

    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            return QUIT

        #aqui vamos criar movimentação e importar o player e mobs
        #vê se apertou alguma tecla
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                NAVE.velocidadeX -= NAVE.aceleracaoX

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                NAVE.velocidadeX += NAVE.aceleracaoX

            if event.key == pygame.K_SPACE:
                NAVE.tiro()

        #vê se soltou alguma tecla
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                NAVE.velocidadeX += NAVE.aceleracaoX

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                NAVE.velocidadeX -= NAVE.aceleracaoX

    return estado


def eventos_boss(estado, NAVE, BOSS):

    #verifica se apertou alguma tecla
    for event in pygame.event.get():

        #verifica se usuário saiu
        if event.type == pygame.QUIT:
            return QUIT

        #aqui vamos criar movimentação e importar o player e mobs
        #vê se apertou alguma tecla
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                NAVE.velocidadeX -= NAVE.aceleracaoX

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                NAVE.velocidadeX += NAVE.aceleracaoX

            if event.key == pygame.K_SPACE:
                NAVE.tiro()

        #vê se soltou alguma tecla
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                NAVE.velocidadeX += NAVE.aceleracaoX

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                NAVE.velocidadeX -= NAVE.aceleracaoX

    return estado
