import sys  # to be able to exit the game

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to save game assets and behaviour"""
    def __init__(self):
        #intialise the backgrond so that pygame can work properly
        pygame.init() 

        #make instance of Settings class
        self.settings = Settings()

        # This object is called a surface. This where all graphics can fit
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #sets an attribute that contain color of the window
        self.bg_color=self.settings.bg_color

        #make an instance of Ship after we made the screen
        self.ship =Ship(self)
        #Instance of the bullet
        self.bullets = pygame.sprite.Group()
        #isntance of the aien
        self.aliens= pygame.sprite.Group()

        #intilise creation of alien fleet at the game begining
        self._create_fleet()

        while(True):
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                   
    def _check_keydown_events(self, event):
        """respond to keypress, made to cofactor _check_events"""
        if event.key == pygame.K_RIGHT:
            #update moving_right flag
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            #update moving_left flag
            self.ship.moving_left=True
        elif event.key ==pygame.K_q:
            sys.exit()
        elif event.key ==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to keyup, made to cofactor _check_events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        """Creates a new bullet and add it to bullet group"""
        # print(len(self.bullets))
        # print(f"Number of bullets allowed {self.settings.bullets_allowed}")
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """update positon of bullets and git rid of old bullets."""
        self.bullets.update()
        #Get rid of the old bullets so that, it doesn't consume memory
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #create an alien an find the number of aliens in a row
        #spacing between aliens is equal to one alien width
        alien = Alien(self)  #This alien won't be added to the fleet
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Create the first row of aliens.
        for alien_number in range (0, number_aliens_x):
            #create an alien and place it in the row
            alien = Alien(self)
            alien.x = alien_width *2 *(1+alien_number) #heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeere, there is a catch<<<<<<<<<
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _update_screen(self):
        """update image on screen and flip to the new scene"""
        #Redraw the screen throuhg each path through each pass through the loop
        #using fill method
        self.screen.fill(self.bg_color)

        #After displaying the screen, we draw ship by using bltime fuction
        self.ship.bltime()

        #updates Bullets position
        for bullet in self.bullets.sprites():  
            bullet.draw_bullet()

        #add alien to screen
        self.aliens.draw(self.screen)

        #Make the most recnetly drawn screens visible
        #it erases the old screen making the new scene visible
        # making the illusion of motion                  
        pygame.display.flip()

        

if __name__ == '__main__': #if the file is called directly, not imported as module
    # as python sets the special value __name__ = '__main__' when run directly 
    #Make the game instances and start the game
    ai = AlienInvasion()
    ai.run_game()









