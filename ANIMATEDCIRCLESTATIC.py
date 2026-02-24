import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

# Circle properties
x = 50
y = height // 2
radius = 30
speed = 3

clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move circle
    x += speed
    if x > width - radius or x < radius:
        speed = -speed  # Bounce effect

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw circle
    pygame.draw.circle(screen, (0, 255, 255), (x, y), radius)

    pygame.display.flip()
    clock.tick(60)
