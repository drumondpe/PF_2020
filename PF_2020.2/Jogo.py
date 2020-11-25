"""
Autores: Luiz Durand, Henrry Miguel e Pedro Drumond
"""
import pygame
import time

from Configurações import Config
from Configurações import Textos
from Configurações import Cores
from Configurações import INIT, GAME, GAME_OVER, VENCEDOR, QUIT, BOSS
from Player import Nave
from Aliens import Alien
from Boss import Death_star
import Funções as funcoes

#Aliens = Tie Fighter
#Estrela da Morte / Death Star = Boss

pygame.init()
pygame.mixer.init()

CONFIG = Config()
TEXTOS = Textos()
CORES = Cores()


def rodar_init(tela): #inicia o jogo
    estado = INIT
    while estado == INIT:
        #ABRE A PRIMEIRA TELA
        funcoes.primeira_tela(tela)

        estado = funcoes.eventos_init(estado)
        pygame.display.flip()
    return estado


def rodar_game_over(tela): #roda a tela de game over
    estado = GAME_OVER
    while estado == GAME_OVER:
        #TELA GAME OVER
        game_over_tela = funcoes.gameover_tela(tela)

        estado = funcoes.eventos_game_over(estado) #verifica os eventos

        pygame.display.flip()
    return estado

def rodar_vencedor(tela): #roda a tela de vencedor 
    estado = VENCEDOR
    while estado == VENCEDOR:
        #TELA VENCEDOR 
        vencedor_tela = funcoes.vencedor_tela(tela)

        estado = funcoes.eventos_game_over(estado) #verifica os eventos igual no game over e recomeça o jogo

        pygame.display.flip()
    return estado


def rodar_jogo(tela): #roda a primeira tela de gameplay
    relogio = pygame.time.Clock()

    ### INICIA OBJETOS ###
    sprites = pygame.sprite.Group()
    aliens_colisao = pygame.sprite.Group()
    disparos_sprite = pygame.sprite.Group()
    disparos_sprite_nave = pygame.sprite.Group() #sprites que serão usados depois
    NAVE = Nave(CONFIG, sprites, disparos_sprite, disparos_sprite_nave) #cria a nave
    funcoes.cria_aliens(sprites, aliens_colisao) #cria os aliens

    nave = NAVE
    sprites.add(nave)
    pontos = 0

    estado = GAME
    while estado == GAME:
        #SEGUNDA TELA
        fundo = pygame.image.load('Fundo_galáxia.png').convert()
        fundo = pygame.transform.scale(fundo, (CONFIG.largura_tela, CONFIG.altura_tela))
        tela.fill(CORES.preto)
        tela.blit(fundo, (0, 0))
        #mapa

        sprites.update() #atualiza todos os sprites
        sprites.draw(tela) #desenha todos os sprites

        funcoes.segunda_tela(tela, NAVE, pontos) #apresenta a segunda tela

        estado = funcoes.eventos_game(estado, NAVE) #verifica os eventos

        colisao = pygame.sprite.spritecollide(NAVE, aliens_colisao, True) #verifica se houve colisão dos aliens com a nave e destroi o que colidiu
        acertou_disparo = pygame.sprite.groupcollide(aliens_colisao, disparos_sprite_nave, True, True) #verifica se houve colisão do disparo com os aliens (colisão entre sprites)
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
    return estado, NAVE, pontos, sprites, disparos_sprite, disparos_sprite_nave


def rodar_jogo_boss(tela, NAVE, pontos, sprites, disparos_sprite, disparos_sprite_nave): #roda 
    sprites = sprites #irá desenhar tudo
    disparos_sprite = disparos_sprite #todos os disparos
    disparos_sprite_boss = pygame.sprite.Group()

    #sprites_NAVE_e_BOSS = pygame.sprite.Group()

    BOSS = Death_star(CONFIG, sprites, disparos_sprite, disparos_sprite_boss) #cria o BOSS
    sprites.add(BOSS)

    estado = BOSS
    while estado == BOSS:
    #TELA DO BOSS
        fundo = pygame.image.load('Fundo_galáxia.png').convert()
        fundo = pygame.transform.scale(fundo, (CONFIG.largura_tela, CONFIG.altura_tela))
        tela.fill(CORES.preto)
        tela.blit(fundo, (0, 0))

        sprites.update() #mudar isso pra função da tela
        sprites.draw(tela)

        funcoes.boss_tela(tela, NAVE, pontos, BOSS)
        
        funcoes.barra_vida(tela, BOSS) #desenha a barra de vida do boss   #talvez tirar a variável

        estado = funcoes.eventos_boss(estado, NAVE, BOSS) #verifica os eventos        

        Disparo_acertou_o_BOSS = pygame.sprite.spritecollide(BOSS, disparos_sprite_nave, True) #disparos da nave que acertaram o boss
        Disparo2_acertou_a_NAVE = pygame.sprite.spritecollide(NAVE, disparos_sprite_boss, True) #disparos do boss que acertaram a nave
    

        if len(Disparo2_acertou_a_NAVE) > 0: #se o disparo da Estrela da Morte atingir, a nave perde uma vida
            NAVE.vidas -= 1

        if len(Disparo_acertou_o_BOSS) > 0: #se o disparo da Nave atingir, a Estrela da Morte perde uma vida
            BOSS.vidas -= 1

        if NAVE.vidas <= 0: #se acabar as vidas da nave, o jogo acaba - perde 
            estado = GAME_OVER

        if BOSS.vidas <= 0: #se acabar as vidas do Boss, o jogo acaba - vence
            estado = VENCEDOR

        pygame.display.flip()
    return estado


#inicializa o jogo
tela = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
pygame.display.set_caption('X-Wing Fight')

estado_jogo = INIT
while estado_jogo != QUIT:
    if estado_jogo == INIT: #roda a primeira tela
        pygame.mixer.music.load('musica_primeira_tela.mp3')
        pygame.mixer.music.play() 
        estado_jogo = rodar_init(tela)

    elif estado_jogo == GAME: #roda a tela de gameplay
        pygame.mixer.music.load('musica_game.mp3')
        pygame.mixer.music.play()
        estado_jogo, NAVE, pontos, sprites, disparos_sprite, disparos_sprite_nave = rodar_jogo(tela)

    elif estado_jogo == BOSS: #roda a segunda tela de gameplay
        pygame.mixer.music.load('musica_boss.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_jogo_boss(tela, NAVE, pontos, sprites, disparos_sprite, disparos_sprite_nave)

    elif estado_jogo == VENCEDOR: #roda a tela de vencedor
        pygame.mixer.music.load('vitoria.mp3') 
        pygame.mixer.music.play()
        estado_jogo = rodar_vencedor(tela) 

    elif estado_jogo == GAME_OVER: #roda a tela de game over
        pygame.mixer.music.load('musica_game_over.mp3')
        pygame.mixer.music.play()
        estado_jogo = rodar_game_over(tela)

    else:
        estado_jogo = QUIT #fecha o jogo
