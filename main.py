# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

#imports constants for use in the game
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()