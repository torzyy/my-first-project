import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка на Pygame')
clock = pygame.time.Clock()

# Начальная позиция и тело змейки
snake_pos = [100, 60]
snake_body = [[100, 60], [80, 60], [60, 60]]
snake_direction = 'RIGHT'

# Позиция еды
apple_pos = [random.randint(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
             random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]

# Игровой флаг
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = -BLOCK_SIZE, 0
            if event.key == pygame.K_RIGHT:
                snake_direction = BLOCK_SIZE, 0
            if event.key == pygame.K_UP:
                snake_direction = 0, -BLOCK_SIZE
            if event.key == pygame.K_DOWN:
                snake_direction = 0, BLOCK_SIZE

    # Обновление позиции головы
    snake_pos += snake_direction
    snake_pos += snake_direction  [1](https://thecode.media/snake-js/)

    # Добавление нового сегмента
    snake_body.insert(0, list(snake_pos))
    if snake_pos != apple_pos:
        snake_body.pop()
    else:
        # Появление новой еды
        apple_pos = [random.randint(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                     random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]

    # Проверка на столкновение с телом
    if snake_pos in snake_body[1:]:
        print("Игра окончена!")
        running = False
    elif snake_pos < 0 or snake_pos >= SCREEN_WIDTH or snake_pos < 0 or snake_pos >= SCREEN_HEIGHT:
        print("Игра окончена!")
        running = False  [1](https://thecode.media/snake-js/)

    # Отрисовка
    screen.fill((0, 0, 0))  # Чёрный фон
    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment, segment, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple_pos, apple_pos, BLOCK_SIZE, BLOCK_SIZE))  [1](https://thecode.media/snake-js/)

    pygame.display.flip()
    clock.tick(10)  # Контроль FPS

pygame.quit()
