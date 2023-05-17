import pygame
import random

# Initialize Pyame
pygame.init()

# Set the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 900

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Brick Breaker Game")


darkorchid1 = (191, 62, 255)
darksalmon = (233, 150, 122)
orchid1 = (255, 131, 250)
slateblue4 = (71, 60, 139)
pink4 = (139, 99, 108)
peachpuff1 = (255, 218, 185)


# Set the font
font = pygame.font.SysFont("georgia", 30)
game_over_font = pygame.font.SysFont("georgia", 70)


# Set the ball speed
BALL_SPEED = 1
# Set the paddle speed
PADDLE_SPEED = 1
# Set the brick dimensions
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
# Set the number of rows and columns of bricks
BRICK_ROWS = 12
BRICK_COLS = 8

# Create the ball
ball = pygame.Rect(WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2 - 10, 20, 20)

# Set the ball's direction
dx = random.choice([-1, 1])
dy = -1

# Create the paddle
paddle = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 50, 100, 20)

# Create the bricks
bricks = []
for i in range(BRICK_ROWS):
    for j in range(BRICK_COLS):
        brick = pygame.Rect(
            j * (BRICK_WIDTH + 10) + 70,
            i * (BRICK_HEIGHT + 10) + 70,
            BRICK_WIDTH,
            BRICK_HEIGHT,
        )
        bricks.append(brick)

score = 0
lives = 3
gameOver = False
running = True

# Create the game loop
while running:
    # Fill the screen with black
    screen.fill(peachpuff1)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameOver:

                # Reset the game
                ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                paddle.centerx = WINDOW_WIDTH // 2
                dx = random.choice([-1, 1])
                dy = -1
                bricks = []
                for i in range(BRICK_ROWS):
                    for j in range(BRICK_COLS):
                        brick = pygame.Rect(
                            j * (BRICK_WIDTH + 10) + 70,
                            i * (BRICK_HEIGHT + 10) + 70,
                            BRICK_WIDTH,
                            BRICK_HEIGHT,
                        )
                        bricks.append(brick)
                score = 0
                lives = 3
                gameOver = False

    if not gameOver:
        # Move the ball
        ball.x += dx * BALL_SPEED
        ball.y += dy * BALL_SPEED
    # Bounce the ball off the walls
    if ball.left < 0 or ball.right > WINDOW_WIDTH:
        dx *= -1
    if ball.top < 0:
        dy *= -1

    # Check if the ball hits the paddle
    if ball.colliderect(paddle):
        dy *= -1

    # Check if the ball hits a brick
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            dy *= -1
            score += 100

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.x += PADDLE_SPEED

    # Draw the ball, paddle, and bricks
    pygame.draw.rect(screen, darksalmon, ball)
    pygame.draw.rect(screen, orchid1, paddle)
    for brick in bricks:
        pygame.draw.rect(screen, darkorchid1, brick)

    # Draw the score and lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, pink4)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, pink4)
    screen.blit(text, (650, 10))
    # score_text = font.render(f"Score: {score}", True, RED)
    # screen.blit(score_text, (10, 10))
    # lives_text = font.render(f"Lives: {lives}", True, RED)
    # screen.blit(lives_text, (WINDOW_WIDTH - lives_text.get_width() - 10, 10))
    # Check if the player loses a life
    if ball.bottom > WINDOW_HEIGHT:
        lives -= 1
        if lives == 0:
            running = False
            game_over_text = game_over_font.render("Game Over", True, slateblue4)
            game_over_rect = game_over_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            )
            screen.blit(game_over_text, game_over_rect)
            font = pygame.font.Font(None, 65)
            text = font.render("Score: " + str(score), 1, pink4)
            screen.blit(text, (230, 550))
            text = font.render("Lives: " + str(lives), 1, pink4)
            screen.blit(text, (230, 500))
        else:
            ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            paddle.centerx = WINDOW_WIDTH // 2

    # Update the display
    pygame.display.update()
# Quit pygame
pygame.time.wait(3000)
pygame.quit()