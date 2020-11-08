import pygame
from pygame import DOUBLEBUF

class Display(object):
    def __init__(self, W, H):
        pygame.init() # connect abstractions to specific hardware
        self.screen = pygame.display.set_mode((W, H), DOUBLEBUF) # canvas
        self.surface = pygame.Surface(self.screen.get_size()).convert() # convert pxl format

    def paint(self, img):
        for event in pygame.event.get():
            pass

        # blit directly from array interface
        pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:,:,[2,1,0]]) # cv2 BGR
        # blit surface onto screen
        self.screen.blit(self.surface, (0,0))
        # update the full display surface to the screen
        pygame.display.flip()
        
