# -*- coding: utf-8 -*-


#Funções
import math
import pygame
from Configurações import Config
from Configurações import Textos
from Configurações import Cores
from Player import Nave
from Aliens import Alien

linhas = 5
colunas = 5
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

def segunda_tela(tela, NAVE, pontos): #apresenta a segunda tela
    #fonte
    fonte_texto_vidas = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_vidas)
    #textos
    restantes = fonte_texto_vidas.render('Vidas restantes: ', True, CORES.branco)
    pontuacao = fonte_texto_vidas.render('Pontuação: {}'.format(pontos), True, CORES.branco) ###MEXER NA PONTUAÇÃO AQUI

    #para mexer na tela, mexer aqui 
    fundo = pygame.image.load('Fundo_galáxia.png').convert()
    fundo = pygame.transform.scale(fundo, (CONFIG.largura_tela, CONFIG.altura_tela))
    tela.fill(CORES.preto)
    tela.blit(fundo, (0, 0))

    foto_vida_errada = pygame.image.load('Nave.png').convert_alpha()
    foto_vida = pygame.transform.scale(foto_vida_errada, (25, 25))

    vertices = (0, 0, CONFIG.largura_tela, 30)
    pygame.draw.rect(tela, CORES.preto, vertices)
    tela.blit(restantes, (10, 7))
    tela.blit(pontuacao, (750, 7))

    #desenha uma vida na tela
    posicao = 150
    for vida in range(NAVE.vidas):
        tela.blit(foto_vida, (posicao, 6))
        posicao+=30


def cria_aliens(sprites, aliens_colisao): #gera os aliens  
    for linha in range(linhas): #acessa a linha
        for item in range(colunas):
            alien = Alien(100 + item * 100, 100 + linha * 70)
            sprites.add(alien)
            aliens_colisao.add(alien)


def gameover_tela(tela):
    #configurações das fontes
    fonte_texto_tela_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande)
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_nome)
    fonte_texto_medio = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_medio)

    #textos da tela game over
    game_over = fonte_texto_tela_inicial.render('GAME OVER!', True, CORES.vermelho)
    barra_recomeçar = fonte_texto_tela_inicial.render('Pressione barra de espaço para recomeçar!', True, CORES.azul_marinho)

    #preenche a tela com frases
    tela.blit(game_over, (CONFIG.largura_tela // 2 - game_over.get_width() // 2, 180))
    tela.blit(barra_recomeçar, (CONFIG.largura_tela // 2 - barra_recomeçar.get_width() // 2, 380))

def faz_pontos(soma_ponto):
    aumenta_ponto = 0
    if soma_ponto:
        aumenta_ponto += 10
    return aumenta_ponto



def eventos(RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER, NAVE):

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

        elif TELA_SEGUNDA:
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

        elif TELA_GAME_OVER:
            #vamos ver se o player vai querer jogar de novo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    TELA_GAME_OVER = False
                    TELA_SEGUNDA = True


    return RODAR, TELA_INICIAL, TELA_SEGUNDA, TELA_GAME_OVER

        