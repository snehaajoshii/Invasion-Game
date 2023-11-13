class Settings: 
    '''A class to store all settings for Alien Invasion'''
    def __init__(self):
        '''Initialize the game's settings'''
        #Screen Settings 
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,64,64)
        # Rocket settings
        self.rocket_speed = 1
        self.rocket_limit = 3
        #Bullet setiings 
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1