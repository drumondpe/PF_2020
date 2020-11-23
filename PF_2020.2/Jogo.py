# -*- coding: utf-8 -*-

### Próximos passos ###
#add Boss (pontuação 700!) acho que precisará de uma nova tela, ou se bater 700 pontos...

### Problemas ###
#ordem de desenhos

### Plus ###
#musica de fundo na primeira tela
#musica de fundo no jogo
#musica de fundo na Estrela da morte
#musica de fundo no game over
#musica de fundo no vencedor
#musica de fundo no disparo

"""
Autores: Luiz Durand, Henrry Miguel e Pedro Drumond
"""
import pygame

from Configurações import Config
from Configurações import Textos
from Configurações import Cores
from Configurações import INIT, GAME, GAME_OVER, VENCEDOR, QUIT, BOSS
from Player import Nave
from Aliens import Alien
import Funções as funcoes

pygame.init()
pygame.mixer.init()

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()


def rodar_init(tela):
    estado = INIT
    while estado == INIT:
        #DEVE ABRIR A PRIMEIRA TELA
        funcoes.primeira_tela(tela)

        estado = funcoes.eventos_init(estado)
        pygame.display.flip()
    return estado


def rodar_game_over(tela):
    estado = GAME_OVER
    while estado == GAME_OVER:
        #TELA GAME OVER
        game_over_tela = funcoes.gameover_tela(tela)

        estado = funcoes.eventos_game_over(estado) #verifica os eventos

        pygame.display.flip()
    return estado



def rodar_jogo(tela):
    relogio = pygame.time.Clock()
    COLISAO_ALIEN = False #usar para quando houver colisão do alien com a nave
    COLISAO_DISPARO = False #usar para quando houver colisão do disparo da nave com o alien

    ### INICIA OBJETOS ###
    sprites = pygame.sprite.Group()
    aliens_colisao = pygame.sprite.Group()
    disparos_sprite = pygame.sprite.Group()
    NAVE = Nave(CONFIG, sprites, disparos_sprite) #cria a nave
    funcoes.cria_aliens(sprites, aliens_colisao) #cria os aliens

    nave = NAVE
    sprites.add(nave)
    pontos = 0


    estado = GAME
    while estado == GAME:
        #SEGUNDA TELA
        tela.fill(CORES.preto)
        #mapa

        funcoes.segunda_tela(tela, NAVE, pontos)

        sprites.update() #mudar isso pra função da tela
        sprites.draw(tela)

        estado = funcoes.eventos_game(estado, NAVE) #verifica os eventos

        colisao = pygame.sprite.spritecollide(NAVE, aliens_colisao, True) #verifica se houve colisão dos aliens com a nave e destroi o que colidiu, super útil
        acertou_disparo = pygame.sprite.groupcollide(aliens_colisao, disparos_sprite, True, True) #verifica se houve colisão do disparo com os aliens
        #foi criado um dicionario que as chaves são os aliens e os valores os disparos

        #fará a colisão:
        for alien in acertou_disparo:
            soma_ponto = True #se for True, irá add 10 pontos na função 'pontos'
            pontos += funcoes.faz_pontos(soma_ponto) #precisa colocar isso aqui lá na função 'segunda tela'

        if len(colisao)>0: #reduz as vidas conforme as colisões
            NAVE.vidas -= 1

        if pontos == 700 or (pontos == 690 and NAVE.vidas == 2) or (pontos == 680 and NAVE.vidas == 1):
            estado = BOSS

        if NAVE.vidas <= 0:
            estado = GAME_OVER

        pygame.display.flip()
    return estado, NAVE, pontos, sprites

def rodar_jogo_boss(tela, NAVE, pontos, sprites):
    #pegar as coisas da funcao de cima e rodar a tela
    relogio = pygame.time.Clock()
    COLISAO_DISPARO = False #usar para quando houver colisão do disparo da nave com a Death Star
    COLISAO_DISPARO2 = False #usar para quando houver colisão do disparo2 com a nave

    disparos_sprite = pygame.sprite.Group()

    estado = BOSS
    while estado == BOSS:
    #TELA DO BOSS

        funcoes.boss_tela(tela, NAVE, pontos, BOSS)

        sprites.update() #mudar isso pra função da tela
        sprites.draw(tela)

        estado = funcoes.eventos_game(estado, NAVE) #verifica os eventos

        #fazer uma nova colisao
        #MUDAR ESSAS DUAS LINHAS DE BAIXO
        # colisao = pygame.sprite.spritecollide(NAVE, aliens_colisao, True) #verifica se houve colisão dos aliens com a nave e destroi o que colidiu, super útil
        # acertou_disparo = pygame.sprite.groupcollide(aliens_colisao, disparos_sprite, True, True) #verifica se houve colisão do disparo com os aliens


        if NAVE.vidas <= 0:
            estado = GAME_OVER

        pygame.display.flip()
        pass
    return estado


#inicializa o jogo
tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
pygame.display.set_caption('X-Wing Fight')

estado_jogo = INIT
while estado_jogo != QUIT:
    if estado_jogo == INIT:
        pygame.mixer.music.load('musica_primeira_tela.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_init(tela)

    elif estado_jogo == GAME:
        print(GAME)
        pygame.mixer.music.load('musica_game.mp3')
        pygame.mixer.music.play()
        estado_jogo, NAVE, pontos, sprites = rodar_jogo(tela)

    elif estado_jogo == BOSS:
        pygame.mixer.music.load('musica_boss.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_jogo_boss(tela, NAVE, pontos, sprites) #NOVO

    elif estado_jogo == GAME_OVER:
        pygame.mixer.music.load('musica_game_over.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_game_over(tela)
        
    else:
        estado_jogo = QUIT
