import pygame
from Ball import Ball

#Brick class
class Brick:
    def __init__(self, x, y, width, height, health, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colors = colors
        self.color = colors[0]
    #draw the brick
    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.width, self.height))

    #Brick and ball collision
    def collide_with_ball(self, ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_velocity(ball.x_velocity, ball.y_velocity * -1)
        return True

    #reduce color of brick when hit by ball and reduce it's health
    def hit(self):
        self.health -= 1
        self.color = self.interpolate(
            *self.colors, self.health/self.max_health)

    @staticmethod
    def interpolate(color_a, color_b, t):
        # 'color_a' and 'color_b' are RGB tuples
        # 't' is a value between 0.0 and 1.0
        # this is a naive interpolation
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))
    
    
   

    

    
            
        


