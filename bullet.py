import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired by a ship"""
    def __init__(self, ai_game):
        """Creates a bullet Object at the ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings =ai_game.settings
        #debug line that prints all in settings class
        #print(dir(self.settings))
        self.color = self.settings.bullet_color

        #Creates a bullet objest at position (0 , 0) then move to ship positon
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #stores the bullets position at a decinal value
        self.y =float(self.rect.y)
        
    #update the positon of the bullet to move up
    def update (self):
        """Move the bullets up the screen"""
        #update the decimal position of the bullet
        self.y -=self.settings.bullet_speed
        #update the rect _position 
        self.rect.y=self.y

    def draw_bullet (self):
        """Draw the bullets intp the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
