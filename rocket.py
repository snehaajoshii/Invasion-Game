import pygame
class Rocket:
    ''' A class to manage the rocket'''
    def __init__(self, ai_game):
        '''Initialize the rocket and set its starting position'''
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
       
        # Load the rocket image and get its rect. 
        self.image = pygame.image.load('/Users/snehajoshi/Desktop/projects/PythonClass11/Rocket.png')
        self.rect= self.image.get_rect() 
        #Start each new rocket at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the rocket's horizontal position.
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the rocket's position based on the movement flag'''
        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    
    def blitme(self):
        # Draw the rocket at its current location.
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """Center the rocket on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)