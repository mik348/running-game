import pygame as py

from sys import exit

py.init()  # starting the window
screen = py.display.set_mode((800, 400))  # setting window size
py.display.set_caption("DEMO")  # Naming the window
clock = py.time.Clock()  # variable for framerate
test_font = py.font.Font('sprites/Pixeltype.ttf', 50)

game_active = True

sky_surface = py.image.load('sprites/Sky.png').convert()  # tells code to load the sky image
ground_surface = py.image.load('sprites/ground.png').convert()  # tells code to load the ground image
score_surf = test_font.render('Demo Game', False, (64, 64, 64)).convert()  # tells code to load the text and font
score_rect = score_surf.get_rect(center=(400, 50))

snail_surface = py.image.load('sprites/snail1.png').convert_alpha()  # tells code to load the snail image
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = py.image.load('sprites/player_walk_1.png').convert_alpha()  # tells the code to load the player sprite
player_rect = player_surface.get_rect(midbottom=(80, 300))  # draws a rectangle around the player to be able to control the position
player_gravity = 0
player_on_ground = True

loss_text_surface = py.image.load('sprites/you lose.JPG')

while True:
    # loop for closing the window:
    for event in py.event.get():
        if event.type == py.QUIT:  # if the event == pressing red x...
            py.quit()  # ..quit the code
            exit()  # ... and exit the window.

        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and player_on_ground:
                player_gravity = -20
                player_on_ground = False

    if game_active:

        if not player_on_ground: # Apply gravity only if not on the ground
            player_gravity += 1
            player_rect.y += player_gravity

        if player_rect.bottom >= 300:# Check for ground collision
            player_rect.bottom = 300
            player_on_ground = True
            player_gravity = 0

        snail_rect.x -= 5

        if snail_rect.right <= 0:
            snail_rect.left = 800

        if snail_rect.colliderect(player_rect):
            game_active = False

        screen.blit(sky_surface, (0, 0))  # displays the sky image
        screen.blit(ground_surface, (0, 300))  # displays the ground image
        py.draw.rect(screen, '#c0e8ec', score_rect)
        py.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)  # displays the text
        screen.blit(snail_surface, snail_rect)  # displays the snail
        screen.blit(player_surface, player_rect)  # displays the player sprite

    else:
        screen.fill('Black')
        you_lose = py.image.load('sprites/you lose.jpg')
        screen.blit(you_lose, (89, 0))


    py.display.update()  # update the window
    clock.tick(60)  # maximum value for framerate (60fps)