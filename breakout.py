import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

BACKGROUND_COLOR = (234, 218, 184)
BRICK_RED = (242, 85, 96)
BRICK_GREEN = (86, 174, 87)
BRICK_BLUE = (69, 177, 232)
PADDLE_COLOR = (142, 135, 123)
PADDLE_BORDER = (100, 100, 100)
TEXT_COLOR = (78, 81, 139)

font = pygame.font.SysFont('Constantia', 30)

FPS = 60
clock = pygame.time.Clock()
brick_columns = 6
brick_rows = 6
game_active = False
game_state = 0  # 0 = Not started, 1 = Win, -1 = Lose
score = 0

def display_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

class BrickWall:
    def __init__(self):
        self.width = SCREEN_WIDTH // brick_columns
        self.height = 50
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        self.bricks = []
        for row in range(brick_rows):
            brick_row = []
            for col in range(brick_columns):
                x = col * self.width
                y = row * self.height
                rect = pygame.Rect(x, y, self.width, self.height)

                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                else:
                    strength = 1

                brick_row.append([rect, strength])
            self.bricks.append(brick_row)

    def draw_wall(self):
        for row in self.bricks:
            for brick in row:
                rect, strength = brick
                if strength == 3:
                    color = BRICK_BLUE
                elif strength == 2:
                    color = BRICK_GREEN
                else:
                    color = BRICK_RED
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BACKGROUND_COLOR, rect, 2)

class Paddle:
    def __init__(self):
        self.width = SCREEN_WIDTH // brick_columns
        self.height = 20
        self.reset()

    def move(self):
        keys = pygame.key.get_pressed()
        self.direction = 0
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)
        pygame.draw.rect(screen, PADDLE_BORDER, self.rect, 3)

    def reset(self):
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - (self.height * 2)
        self.speed = 8
        self.direction = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.max_speed = 5
        self.reset(x, y)

    def move(self, paddle, wall):
        global score, game_state
        collision_margin = 5
        wall_cleared = True

        for row_idx, row in enumerate(wall.bricks):
            for col_idx, brick in enumerate(row):
                rect, strength = brick
                if self.rect.colliderect(rect):
                    if abs(self.rect.bottom - rect.top) < collision_margin and self.speed_y > 0:
                        self.speed_y *= -1
                    elif abs(self.rect.top - rect.bottom) < collision_margin and self.speed_y < 0:
                        self.speed_y *= -1
                    elif abs(self.rect.right - rect.left) < collision_margin and self.speed_x > 0:
                        self.speed_x *= -1
                    elif abs(self.rect.left - rect.right) < collision_margin and self.speed_x < 0:
                        self.speed_x *= -1

                    if strength > 1:
                        wall.bricks[row_idx][col_idx][1] -= 1
                    else:
                        wall.bricks[row_idx][col_idx][0] = pygame.Rect(0, 0, 0, 0)
                        score += 10

                if wall.bricks[row_idx][col_idx][0].width != 0:
                    wall_cleared = False

        if wall_cleared:
            game_state = 1

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            game_state = -1

        if self.rect.colliderect(paddle.rect):
            if abs(self.rect.bottom - paddle.rect.top) < collision_margin and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += paddle.direction
                self.speed_x = max(min(self.speed_x, self.max_speed), -self.max_speed)
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, PADDLE_COLOR, self.rect.center, self.radius)
        pygame.draw.circle(screen, PADDLE_BORDER, self.rect.center, self.radius, 2)

    def reset(self, x, y):
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4

wall = BrickWall()
paddle = Paddle()
ball = Ball(paddle.rect.centerx, paddle.rect.top)

running = True
while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    wall.draw_wall()
    paddle.draw()
    ball.draw()

    if game_active:
        paddle.move()
        ball.move(paddle, wall)
        if game_state != 0:
            game_active = False
    else:
        if game_state == 0:
            display_text("CLICK TO START", font, TEXT_COLOR, 180, SCREEN_HEIGHT // 2)
        elif game_state == 1:
            display_text("YOU WON!", font, TEXT_COLOR, 230, SCREEN_HEIGHT // 2 - 40)
            display_text("CLICK TO RESTART", font, TEXT_COLOR, 180, SCREEN_HEIGHT // 2)
        elif game_state == -1:
            display_text("YOU LOST!", font, TEXT_COLOR, 230, SCREEN_HEIGHT // 2 - 40)
            display_text("CLICK TO RESTART", font, TEXT_COLOR, 180, SCREEN_HEIGHT // 2)

    display_text(f"Score: {score}", font, TEXT_COLOR, 10, SCREEN_HEIGHT - 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
            score = 0
            wall.create_wall()
            paddle.reset()
            ball.reset(paddle.rect.centerx, paddle.rect.top)
            game_state = 0
            game_active = True

    pygame.display.update()

pygame.quit()
