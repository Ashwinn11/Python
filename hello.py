import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY  = (100, 100, 100)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24, bold=True)
game_over_font = pygame.font.SysFont("Arial", 36, bold=True)

# Snake and Food
def random_food_position(snake):
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if [x, y] not in snake:
            return [x, y]

def draw(snake, food, score):
    screen.fill(BLACK)
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

def handle_input(current_direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and current_direction != 'DOWN':
        return 'UP'
    if keys[pygame.K_DOWN] and current_direction != 'UP':
        return 'DOWN'
    if keys[pygame.K_LEFT] and current_direction != 'RIGHT':
        return 'LEFT'
    if keys[pygame.K_RIGHT] and current_direction != 'LEFT':
        return 'RIGHT'
    return current_direction

def move_snake(snake, direction):
    head = snake[0][:]
    if direction == 'UP':
        head[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        head[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        head[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        head[0] += BLOCK_SIZE
    snake.insert(0, head)
    return snake

def check_collision(snake):
    head = snake[0]
    return (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    )

def show_game_over(score):
    screen.fill(BLACK)
    game_over_text = game_over_font.render("Game Over!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    retry_text = font.render("Press R to Restart or Q to Quit", True, GRAY)

    screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - 80, HEIGHT//3 + 50))
    screen.blit(retry_text, (WIDTH//2 - 150, HEIGHT//3 + 100))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Main Game Loop
def main():
    snake = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    food = random_food_position(snake)
    score = 0

    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        direction = handle_input(direction)
        snake = move_snake(snake, direction)

        # Check food collision
        if snake[0] == food:
            score += 1
            food = random_food_position(snake)
        else:
            snake.pop()  # only pop when not eating food

        if check_collision(snake):
            break

        draw(snake, food, score)
        clock.tick(FPS)

    show_game_over(score)

if __name__ == "__main__":
    main()