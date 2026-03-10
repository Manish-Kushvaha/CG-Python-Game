import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch The Ball")

# Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

# Basket
basket_width = 100
basket_height = 20
basket_x = width // 2
basket_y = height - 40
basket_speed = 8

# Ball
ball_radius = 10
ball_x = random.randint(20,width-20)
ball_y = 0
ball_speed = 5

score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()
running = True

while running:

    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed

    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed

    # Ball falling
    ball_y += ball_speed

    # Collision detection
    if (basket_y < ball_y + ball_radius and
        basket_x < ball_x < basket_x + basket_width):

        score += 1
        ball_y = 0
        ball_x = random.randint(20,width-20)

    # Game over
    if ball_y > height:
        print("Game Over! Score:",score)
        running = False

    # Draw basket
    pygame.draw.rect(screen, blue, (basket_x,basket_y,basket_width,basket_height))

    # Draw ball
    pygame.draw.circle(screen, red, (ball_x,ball_y), ball_radius)

    # Display score
    score_text = font.render("Score: "+str(score),True,black)
    screen.blit(score_text,(10,10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()