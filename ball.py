import pygame
import sys

# Default Setup for pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# Ball Properties
ball_pos = [400,300]
ball_vel = [2,2]
ball_radius = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
    
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > 800:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - ball_radius <0 or ball_pos[1] + ball_radius > 600:
        ball_vel[1] = -ball_vel[1]

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 0,0), ball_pos, ball_radius)
    pygame.display.flip()
    clock.tick(60)

