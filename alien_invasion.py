import sys  # to be able to exit the game

import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    """Overall class to save game assets and behaviour"""
    def __init__(self):
        #intialise the backgrond so that pygame can work properly
        pygame.init() 
        #make instance of Settings class
        self.settings = Settings()
        # This object is called a surface
        # This where all graphics can fit
        # we used self.screen attribute to make it accessible throught class
        # Each element like enemy and ship has its own surface but this is the 
        # entire window
        self.screen =pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #sets an attribute that contain color of the window
        self.bg_color=self.settings.bg_color

        #make an instance of Ship after we made the screen
        self.ship =Ship(self)
    def run_game(self):
        """Starts the main loop for the game"""
        while(True):
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    #refactoring code using helper methods        
    def _check_events(self):
        """A helper mehod-can't be called outside class- to check mouth or keyboard check"""
        #it checks for any mouse or keyboard events
        #Note pygame.event.get() lists all the events from
        # last time the function was called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif pygame.KEYUP:
                    self._check_keyup_events(event)
                   
    def _check_keydown_events(self, event):
        """respond to keypress, made to cofactor _check_events"""
        if event.key == pygame.K_RIGHT:
            #update moving_right flag
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            """respond to keyup, made to cofactor _check_events"""
            #update moving_left flag
            self.ship.moving_left=True
        elif event.key ==pygame.k_q:
            sys.exit()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
    def _update_screen(self):
        """update image on screen and flip to the new scene"""
        #Redraw the screen throuhg each path through each pass through the loop
        #using fill method
        self.screen.fill(self.bg_color)

        #After displaying the screen, we draw ship by using bltime fuction
        self.ship.bltime()

        #Make the most recnetly drawn screens visible
        #it erases the old screen making the new scene visible
        # making the illusion of motion 
        pygame.display.flip()

if __name__ == '__main__': #if the file is called directly, not imported as module
    # as python sets the special value __name__ = '__main__' when run directly 
    #Make the game instances and start the game
    ai = AlienInvasion()
    ai.run_game()









