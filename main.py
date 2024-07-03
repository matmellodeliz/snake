import pygame, random
from pygame.locals import *


# criacao de maca em uma posicao aleatoria
def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return x * 10, y * 10


# tamanho da cobra depois de comer maca
def comeu(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# definicoes de movimentacao
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
# tamanho da tela
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da cobrinha')

# cobrinha com tamanho tres
tamanho_cobra = [(200, 200), (210, 200), (220, 200)]
# cada segmento da cobrinha
quadrado_cobrinha = pygame.Surface((10, 10))
# cobrinha branca
quadrado_cobrinha.fill((255, 255, 255))

# aleatoriedade da criacao da maca
maca_nova = on_grid_random()
#tamanho da maca
maca = pygame.Surface((10, 10))
#maca vermelha
maca.fill((255, 0, 0))

# cobrinha comeca andando pra esquerda
direcao_cobrinha = LEFT

# fps do jogo
clock = pygame.time.Clock()

# estilo de fonte do jogo
fonte = pygame.font.Font('freesansbold.ttf', 18)
pontuacao = 0

game_over = False
while not game_over:
    # velocidade da cobrinha
    clock.tick(10)
    # sair do programa
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # proibindo de fazer 360 graus
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao_cobrinha != DOWN:
                direcao_cobrinha = UP
            if event.key == K_DOWN and direcao_cobrinha != UP:
                direcao_cobrinha = DOWN
            if event.key == K_LEFT and direcao_cobrinha != RIGHT:
                direcao_cobrinha = LEFT
            if event.key == K_RIGHT and direcao_cobrinha != LEFT:
                direcao_cobrinha = RIGHT
    # se comeu a maca, nascer nova maca e ganhar mais um ponto
    if comeu(tamanho_cobra[0], maca_nova):
        maca_nova = on_grid_random()
        tamanho_cobra.append((0, 0))
        pontuacao = pontuacao + 1

    # se cobrinha bateu na parede
    if tamanho_cobra[0][0] == 600 or tamanho_cobra[0][1] == 600 or tamanho_cobra[0][0] < 0 or tamanho_cobra[0][1] < 0:
        game_over = True
        break

    # se cobrinha bateu nela mesma
    for i in range(1, len(tamanho_cobra) - 1):
        if tamanho_cobra[0][0] == tamanho_cobra[i][0] and tamanho_cobra[0][1] == tamanho_cobra[i][1]:
            game_over = True
            break
    if game_over:
        break
    for i in range(len(tamanho_cobra) - 1, 0, -1):
        tamanho_cobra[i] = (tamanho_cobra[i - 1][0], tamanho_cobra[i - 1][1])

    # direcao da cobrinha
    if direcao_cobrinha == UP:
        tamanho_cobra[0] = (tamanho_cobra[0][0], tamanho_cobra[0][1] - 10)
    if direcao_cobrinha == DOWN:
        tamanho_cobra[0] = (tamanho_cobra[0][0], tamanho_cobra[0][1] + 10)
    if direcao_cobrinha == RIGHT:
        tamanho_cobra[0] = (tamanho_cobra[0][0] + 10, tamanho_cobra[0][1])
    if direcao_cobrinha == LEFT:
        tamanho_cobra[0] = (tamanho_cobra[0][0] - 10, tamanho_cobra[0][1])
    # limpa tela e desenha nova maca
    screen.fill((0, 0, 0))
    screen.blit(maca, maca_nova)

    # pontos no topo direito da tela
    pontuacao_font = fonte.render('Pontos: %s' % (pontuacao), True, (255, 255, 255))
    pontuacao_rect = pontuacao_font.get_rect()
    pontuacao_rect.topleft = (600 - 120, 10)
    screen.blit(pontuacao_font, pontuacao_rect)

    for pos in tamanho_cobra:
        screen.blit(quadrado_cobrinha, pos)

    pygame.display.update()
# tela game over
while True:
    game_over_fonte = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_fonte.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.meioTopo = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
