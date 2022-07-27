import pygame
import sys

SIZE = (720, 720)

screen = pygame.display.set_mode(size=SIZE)

while True:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    
