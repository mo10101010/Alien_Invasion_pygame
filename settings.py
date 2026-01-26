#This file will contain all the settings of the project in one place instead of 
# of searching through the entire project

class Settings:
    """A file storing all settings for alien invasion"""
    def __init__(self):
        """intialise the game settings"""
        #screen settings
        self.screen_width =1200
        self.screen_height=800
        self.bg_color = (230, 230, 230)
        #ship setting
        self.ship_speed =1.5
