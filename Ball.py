import pygame


class Ball:
    Velocity = 6

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_velocity = 2
        self.y_velocity = -self.Velocity

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def set_velocity(self, x_velocity, y_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
    
    #draw the ball
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    


   