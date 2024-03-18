import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("media/hand_marker.otf", 50)

background = pygame.image.load("media/Sky.png")
ground = pygame.image.load("media/ground.png")
bg_image_big = pygame.transform.scale(background, (800,300))
bg_image_big2 = pygame.transform.scale(ground, (800,100))
text_surface = font.render("My game", False, "Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_image_big,(0,0))
    screen.blit(bg_image_big2,(0,300))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)