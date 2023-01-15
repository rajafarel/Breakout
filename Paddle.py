import pygame

#paddle class
class Paddle:
    Velocity = 6

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect( screen, self.color, (self.x, self.y, self.width, self.height))
    
    
    #Function to move the paddle to the right
    def move_right(self):
       self.x += self.Velocity
 
    #Function to move the paddle to the left 
    def move_left(self):
       self.x += -self.Velocity
 