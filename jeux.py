import pygame
import random

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
window_width = 800
window_height = 600
cell_size = 20
fps = 10

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Fonction pour dessiner le serpent
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], cell_size, cell_size])

# Fonction principale du jeu
def game():
    game_over = False
    game_close = False

    # Position initiale du serpent
    snake_list = []
    snake_length = 1
    snake_speed = 20
    direction = 'RIGHT'

    # Position initiale de la pomme
    apple_x = round(random.randrange(0, window_width - cell_size) / cell_size) * cell_size
    apple_y = round(random.randrange(0, window_height - cell_size) / cell_size) * cell_size

    # Position initiale de la tête du serpent
    lead_x = window_width / 2
    lead_y = window_height / 2
    lead_x_change = 0
    lead_y_change = 0

    while not game_over:

        while game_close:
            window.fill(white)
            font = pygame.font.SysFont('comicsansms', 35)
            text = font.render("Appuyez sur Q pour quitter ou sur C pour rejouer", True, black)
            window.blit(text, (window_width / 6, window_height / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                    lead_x_change = -cell_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                    lead_x_change = cell_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                    lead_y_change = -cell_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                    lead_y_change = cell_size
                    lead_x_change = 0

        if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        window.fill(white)
        pygame.draw.rect(window, red, [apple_x, apple_y, cell_size, cell_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if lead_x == apple_x and lead_y == apple_y:
            apple_x = round(random.randrange(0, window_width - cell_size) / cell_size) * cell_size
            apple_y = round(random.randrange(0, window_height - cell_size) / cell_size) * cell_size
            snake_length += 1

        clock.tick(fps)

    pygame.quit()
    quit()

game()
