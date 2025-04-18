import pygame
import sys
import random
import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="admin",
    host="localhost"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE,
        max_score INT DEFAULT 0
)
""")
conn.commit()

player_name = input("Enter your name: ")

cur.execute("SELECT max_score FROM players WHERE name = %s", (player_name,))
result = cur.fetchone()

if result is None:
    cur.execute("INSERT INTO players (name, max_score) VALUES (%s, 0)", (player_name,))
    max_score = 0
else:
    max_score = result[0]

conn.commit()

pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

black = (0, 0 , 0)
green = (0, 255, 0)

snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction
fruit_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]
score = 0
font = pygame.font.SysFont('Arial', 20)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] +=cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    if snake_pos[0] < 0:
        snake_pos[0] = width - cell_size
    elif snake_pos[0] >= width:
        snake_pos[0] = 0
    elif snake_pos[1] < 0:
        snake_pos[1] = height - cell_size
    elif snake_pos[1] >= height:
        snake_pos[1] = 0
    
    snake_body.insert(0, list(snake_pos))
    if snake_pos == fruit_pos:
        score += 1
        fruit_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]
        x = random.randint(1, 3)
    else:
        snake_body.pop()

    screen.fill(black)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit_pos[0], fruit_pos[1], cell_size, cell_size))
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    max_text = font.render(f"Max Score: {max_score}", True, (255, 255, 255))
    name_text = font.render(f"Player: {player_name}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(max_text, (10, 40))
    screen.blit(name_text, (10, 70))
    pygame.display.flip()
    clock.tick(10)

if score > max_score:
    cur.execute("UPDATE players SET max_score = %s WHERE name = %s", (score, player_name))
    conn.commit()

cur.close()
conn.close()    
pygame.quit()
sys.exit()