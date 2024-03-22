import pygame
import random
import time
 
window_x = 400
window_y = 700
 
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
dark_red = pygame.Color(70, 0, 0)
blue = pygame.Color(0, 0, 255)
 
pygame.init()
 
pygame.display.set_caption('gra')
game_window = pygame.display.set_mode((window_x, window_y))
 
fps = pygame.time.Clock()
 
player_position = [200, 600]
player_body = [[100, 100]] 

cubes = [] # x, y
new_position_cubes = 0

score = 0
 
game_running = True
clock = pygame.time.Clock()
timer = 1000
substract_time = 0

def spawn_cubes(pozycja, kolor):
    random_nums = random.sample(range(1, 5), 3)
    # klocek 1 - najbardziej na lewo
    # klocek 4 - najbardziej na prawo
    if len(cubes) == 0:
        if 1 in random_nums:
            cubes.append([0, 000])
        if 2 in random_nums:
            cubes.append([100, 000])
        if 3 in random_nums:
            cubes.append([200, 000])
        if 4 in random_nums:
            cubes.append([300, 000])

    if len(cubes) == 3:    
        for i in range(3):
            pygame.draw.rect(game_window, kolor, (cubes[i][0], cubes[i][1] + pozycja, 100, 100))

def draw_cubes():
    if score < 300:
        spawn_cubes(new_position_cubes, blue)
    elif score >= 300 and score < 420:
        spawn_cubes(new_position_cubes, red)
    else:
        spawn_cubes(new_position_cubes, dark_red)

def show_score(kolor, font, rozmiar):
    font_score = pygame.font.SysFont(font, rozmiar)
    surface_score = font_score.render('score : ' + str(score), True, kolor)

    rect_score = surface_score.get_rect()

    game_window.blit(surface_score, rect_score)

def game_over():
    my_font = pygame.font.SysFont('Arial', 30)
    surface_game_over = my_font.render('Your score is: ' + str(score), True, white)

    rect_game_over = surface_game_over.get_rect()
    rect_game_over.midtop = (window_x/2, window_y/4)

    game_window.blit(surface_game_over, rect_game_over)
    pygame.display.flip()
    time.sleep(2)

    pygame.quit()

    quit()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
 
        keys = pygame.key.get_pressed()

        if (player_position[0] < window_x - player_body[0][0]):
            if keys[pygame.K_RIGHT]:
                player_position[0] += 100

        if (player_position[0] > 0):
            if keys[pygame.K_LEFT]:
                player_position[0] -= 100
    
        player_body.insert(1, list(player_position))
        player_body.pop()

    game_window.fill((0, 0, 0))
    pygame.draw.rect(game_window, white, (player_position[0], player_position[1], player_body[0][0], player_body[0][1]))
    
    draw_cubes()

    if pygame.time.get_ticks() >= timer:
        game_window.fill((0, 0, 0))
        pygame.draw.rect(game_window, white, (player_position[0], player_position[1], player_body[0][0], player_body[0][1]))

        draw_cubes()

        if timer > 1000:
            new_position_cubes += 100
        if new_position_cubes == 700:
            if cubes[0][0] == player_position[0]:
                game_over()
            if cubes[1][0] == player_position[0]:
                game_over()
            if cubes[2][0] == player_position[0]:
                game_over()
            score += 10
            if score % 30 == 0 and substract_time <= 140:
                substract_time += 10
            for i in range(3):
                cubes.pop()
            new_position_cubes = 0

        timer += 250 - substract_time

    show_score(white, 'Arial', 20)

    pygame.display.update()
    clock.tick(50)
