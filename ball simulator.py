import pygame
import sys

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulator - Bouncing Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 28)

# Physics variables
x = WIDTH // 2
y = 50
radius = 25
velocity = 0
gravity = 0.5
gravity_enabled = True
bounce = -0.7
MAX_VELOCITY = 20

clock = pygame.time.Clock()

def reset_ball():
    global y, velocity
    y = 50
    velocity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                gravity_enabled = not gravity_enabled
            if event.key == pygame.K_r:
                reset_ball()

    screen.fill(WHITE)

    # Apply gravity
    if gravity_enabled:
        velocity += gravity

    # Limit velocity
    velocity = max(-MAX_VELOCITY, min(velocity, MAX_VELOCITY))
    y += velocity

    # Collision with ground
    if y + radius > HEIGHT - 40:
        y = HEIGHT - 40 - radius
        velocity *= bounce

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, HEIGHT - 40), (WIDTH, HEIGHT - 40), 3)

    # Draw Ball
    pygame.draw.circle(screen, RED, (x, int(y)), radius)

    # Display info
    gravity_text = font.render(
        f"Gravity: {'ON' if gravity_enabled else 'OFF'} | Velocity: {round(velocity, 2)}",
        True, BLACK
    )
    controls_text = font.render("Controls: G = Toggle Gravity | R = Reset", True, BLACK)

    screen.blit(gravity_text, (20, 20))
    screen.blit(controls_text, (20, 50))

    pygame.display.flip()
    clock.tick(60)
