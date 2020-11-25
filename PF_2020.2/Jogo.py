# -*- coding: utf-8 -*-

### Próximos passos ###
#disparos aleatórios do boss, conforme o tempo (boss atira a cada segundo, exemplo)

### Problemas ###
#ordem de desenhos
#tela boss bugada

### Plus ###
#musica de fundo no vencedor
#som do disparo

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
from Boss import Death_star
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

def rodar_vencedor(tela):
    estado = VENCEDOR
    while estado == VENCEDOR:
        #TELA VENCEDOR 
        vencedor_tela = funcoes.vencedor_tela(tela)

        estado = funcoes.eventos_game_over(estado) #verifica os eventos igual no game over e recomeça o jogo

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
        acertou_disparo = pygame.sprite.groupcollide(aliens_colisao, disparos_sprite, True, True) #verifica se houve colisão do disparo com os aliens (colisão entre sprites)
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
    return estado, NAVE, pontos, sprites, disparos_sprite


def rodar_jogo_boss(tela, NAVE, pontos, sprites, disparos_sprite):
    #pegar as coisas da funcao de cima e rodar a tela
    relogio = pygame.time.Clock()
    COLISAO_DISPARO = False #usar para quando houver colisão do disparo da nave com a Death Star
    COLISAO_DISPARO2 = False #usar para quando houver colisão do disparo2 com a nave

    sprites = sprites #irá desenhar tudo
    disparos_sprite = disparos_sprite #todos os disparos
    #sprites_NAVE_e_BOSS = pygame.sprite.Group()
    #tem mais um sprite aqui

    BOSS = Death_star(CONFIG, sprites, disparos_sprite) #cria o BOSS
    sprites.add(BOSS)

    estado = BOSS
    while estado == BOSS:
    #TELA DO BOSS

        #talvez chamar o segunda tela aqui

        sprites.update() #mudar isso pra função da tela
        sprites.draw(tela)

        funcoes.barra_vida(tela, BOSS) #talvez tirar a variável

        estado = funcoes.eventos_boss(estado, NAVE, BOSS) #verifica os eventos

        Disparo_acertou_o_BOSS = pygame.sprite.spritecollide(BOSS, disparos_sprite, True) #disparos da nave que acertaram o boss
        Disparo2_acertou_a_NAVE = pygame.sprite.spritecollide(NAVE, disparos_sprite, True) #disparos do boss que acertaram a nave
    
        if len(Disparo2_acertou_a_NAVE) > 0:
            NAVE.vidas -= 1

        if len(Disparo_acertou_o_BOSS) > 0:
            BOSS.vidas -= 1

        if NAVE.vidas <= 0:
            estado = GAME_OVER

        if BOSS.vidas <= 0:
            estado = VENCEDOR

        pygame.display.flip()
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
        pygame.mixer.music.load('musica_game.mp3')
        pygame.mixer.music.play()
        estado_jogo, NAVE, pontos, sprites, disparos_sprite = rodar_jogo(tela) #talvez tirar o disparos_sprite

    elif estado_jogo == BOSS:
        pygame.mixer.music.load('musica_boss.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_jogo_boss(tela, NAVE, pontos, sprites, disparos_sprite) #NOVO

    elif estado_jogo == VENCEDOR:
        #pygame.mixer.music.load('musica_boss.mp3') #NOVA MUSICA
        #pygame.mixer.music.play()
        estado_jogo = rodar_vencedor(tela) #NOVO

    elif estado_jogo == GAME_OVER:
        pygame.mixer.music.load('musica_game_over.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_game_over(tela)

    else:
        estado_jogo = QUIT
