import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("media/hand_marker.otf", 50)

background = pygame.image.load("media/Sky.png").convert()
ground = pygame.image.load("media/ground.png").convert()
text_surface = font.render("Running Game", False, "Green").convert()

snail = pygame.image.load("media/snail.png").convert_alpha()
snail_x_pos = 600

# pc = pygame.image.load()

bg_image_big = pygame.transform.scale(background, (800,300))
bg_image_big2 = pygame.transform.scale(ground, (800,100))
bg_image_big3 = pygame.transform.scale(snail, (50,50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_image_big,(0,0))
    screen.blit(bg_image_big2,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < 1:
        snail_x_pos = 800
    screen.blit(bg_image_big3,(snail_x_pos,257))

    pygame.display.update()
    clock.tick(60)
    mouse = pygame.mouse.get_pos()