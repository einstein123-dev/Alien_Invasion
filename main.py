import sys

import pygame

class AllienInvasion:
    """This is to control the overall game play"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,140))
        pygame.display.set_caption = "Allien Invasion"