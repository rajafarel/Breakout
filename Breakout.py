import pygame
import math
from Paddle import Paddle
from Ball import Ball
from Brick import Brick

pygame.init()



#Setting the window 
screen_Width = 800 
screen_Height = 700 
screen = pygame.display.set_mode((screen_Width,screen_Height))
pygame.display.set_caption("Breakout")
Fps = 60
#Background Color
bg_Color = (0,0,0)

#Global Variable
Paddle_width = 170
Paddle_height = 20
Ball_radius = 10
Velocity = 5
font = pygame.font.SysFont("arial",50)

#function to handle ball collision with wall
def ball_collision(ball):

    if ball.x - Ball_radius <= 0 or ball.x + Ball_radius >= screen_Width:
        ball.set_velocity(ball.x_velocity * -1, ball.y_velocity)
    if ball.y + Ball_radius >= screen_Height or ball.y - Ball_radius <= 0:
        ball.set_velocity(ball.x_velocity, ball.y_velocity * -1)


#generate blocks of brick
def generate_bricks(rows, cols):
    gap = 4
    brick_width = screen_Width // cols - gap
    brick_height = 40

    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width + gap * col, row * brick_height +
                          gap * row, brick_width, brick_height, 2, [(0, 0, 255), (255, 0, 255)])
            bricks.append(brick)

    return bricks


#function to handle the ball and paddle collision
def paddle_ball_collision(paddle,ball):
    if not (ball.x <= paddle.x + paddle.width and ball.x >= paddle.x):
        return
    if not (ball.y + ball.radius >= paddle.y):
        return

    paddle_center = paddle.x + paddle.width/2
    distance_to_center = ball.x - paddle_center

    percent_width = distance_to_center / paddle.width
    angle = percent_width * 90
    angle_radians = math.radians(angle)

    x_velocity = math.sin(angle_radians) * ball.Velocity
    y_velocity = math.cos(angle_radians) * ball.Velocity * -1

    ball.set_velocity(x_velocity, y_velocity)






    
    
    



#drawing object to screen
def draw(screen,paddle,ball,bricks,lives):
    screen.fill(bg_Color)
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
   
    lives_text = font.render(f"Lives: {lives}", 1, "white")
    screen.blit(lives_text, (10, screen_Height - lives_text.get_height() - 10))
    
    pygame.display.update()






def main():
    
    clock = pygame.time.Clock()
    #setting the position object
    paddle = Paddle(screen_Width/2 - Paddle_width/2,screen_Height - Paddle_height - 5, Paddle_width,Paddle_height,"red")
    ball = Ball(screen_Width/2 ,screen_Height - Paddle_height - 5 - Ball_radius, Ball_radius, "green")
    lives = 3
    bricks = generate_bricks(3, 6)
    
    #function to reset the game if player win or lose
    def reset():
        paddle.x = screen_Width/2 - Paddle_width/2
        paddle.y = screen_Height - Paddle_height - 5
        ball.x = screen_Width/2
        ball.y = screen_Height - Paddle_height - 5 - Ball_radius

    # create a text surface object and setting it's position
    def display_text(text):
        text_render = font.render(text, True, "white")
        screen.blit(text_render, (screen_Width/2 - text_render.get_width() /
                               2, screen_Height/2 - text_render.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)


    run = True
    
    #Start the main loop of the game
    while run:
        #Setting the limit Fps which is 60
        clock.tick(Fps)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        
        
        #Allocation of keys to move the paddle and stop it if it goes outside of the window
        keys = pygame.key.get_pressed()  

        if keys[pygame.K_LEFT] and paddle.x - paddle.Velocity >= 0:
            paddle.move_left()
        if keys[pygame.K_RIGHT] and paddle.x + paddle.width + paddle.Velocity <= screen_Width:
            paddle.move_right()

        for brick in bricks[:]:
            brick.collide_with_ball(ball)
            #Remove brick if it's health is zero
            if brick.health <= 0:
                bricks.remove(brick)

        # when the ball hit the bottom of the screen the life amount will be reduced
        if ball.y + ball.radius >= screen_Height:
            lives -= 1
            ball.x = paddle.x + paddle.width/2
            ball.y = paddle.y - Ball_radius
            ball.set_velocity(0, ball.Velocity * -1)

        
        #reset the game after 5 seconds if player hit the last brick
        if len(bricks) == 0:
            bricks = generate_bricks(3, 6)
            lives = 3
            reset()
            display_text("Congratulations,You Won!")

        #reset the game after 5 seconds if player's health is 0 
        if lives <= 0:
            bricks = generate_bricks(3, 6)
            lives = 3
            reset()
            display_text("Game Over! ")
            
        
        ball.move()
        ball_collision(ball)
        paddle_ball_collision(paddle,ball)
        draw(screen,paddle,ball,bricks,lives)
        
    
    
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()