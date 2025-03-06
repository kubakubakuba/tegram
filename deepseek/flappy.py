import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRAVITY = 0.25
BIRD_JUMP = -6
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets (replace with your own images)
BIRD_IMGS = [
    pygame.image.load("sprites/yellowbird-upflap.png").convert_alpha(),
    pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha(),
    pygame.image.load("sprites/yellowbird-downflap.png").convert_alpha()
]
BG_IMG = pygame.image.load("sprites/background-day.png").convert()
BASE_IMG = pygame.image.load("sprites/base.png").convert()
PIPE_IMG = pygame.image.load("sprites/pipe-green.png").convert_alpha()

# Game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

class Bird:
    def __init__(self):
        self.img = BIRD_IMGS
        self.rect = self.img[0].get_rect(center=(50, SCREEN_HEIGHT//2))
        self.movement = 0
        self.frame = 0
        self.anim_speed = 5
        
    def update(self):
        # Animation
        self.frame += 1
        if self.frame % self.anim_speed == 0:
            self.frame = 0
        self.current_img = self.img[self.frame // self.anim_speed]
        
        # Movement
        self.movement += GRAVITY
        self.rect.centery += self.movement
        
        # Rotation
        self.rotated_img = pygame.transform.rotozoom(self.current_img, -self.movement * 3, 1)
        
    def jump(self):
        self.movement = BIRD_JUMP
        
    def draw(self):
        screen.blit(self.rotated_img, self.rect)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, SCREEN_HEIGHT - 350)
        self.top_pipe = PIPE_IMG.get_rect(midbottom=(x, self.height - 100))
        self.bottom_pipe = PIPE_IMG.get_rect(midtop=(x, self.height + PIPE_GAP))
        self.passed = False
        
    def update(self):
        self.x -= PIPE_SPEED
        self.top_pipe.centerx = self.x
        self.bottom_pipe.centerx = self.x
        
    def draw(self):
        screen.blit(PIPE_IMG, self.top_pipe)
        screen.blit(pygame.transform.flip(PIPE_IMG, False, True), self.bottom_pipe)

def draw_base(base_x):
    screen.blit(BASE_IMG, (base_x, SCREEN_HEIGHT - 100))
    screen.blit(BASE_IMG, (base_x + SCREEN_WIDTH, SCREEN_HEIGHT - 100))

def main():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(2)]
    base_x = 0
    score = 0
    game_active = True
    
    # Pipe timer
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, PIPE_FREQUENCY)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird.jump()
                if event.key == pygame.K_SPACE and not game_active:
                    main()
                    
            if event.type == SPAWNPIPE and game_active:
                pipes.append(Pipe(SCREEN_WIDTH + 100))
        
        # Background
        screen.blit(BG_IMG, (0, 0))
        
        if game_active:
            # Bird
            bird.update()
            bird.draw()
            
            # Pipes
            for pipe in pipes:
                pipe.update()
                pipe.draw()
                
                # Collision detection
                if bird.rect.colliderect(pipe.top_pipe) or bird.rect.colliderect(pipe.bottom_pipe):
                    game_active = False
                
                # Score
                if not pipe.passed and pipe.x < bird.rect.centerx:
                    pipe.passed = True
                    score += 1
                
            # Remove off-screen pipes
            pipes = [pipe for pipe in pipes if pipe.x > -100]
            
            # Floor collision
            if bird.rect.bottom >= SCREEN_HEIGHT - 100:
                game_active = False
            
        else:
            # Game over text
            text = font.render(f"Score: {score}  Press SPACE to restart", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
        
        # Base
        base_x -= 1
        draw_base(base_x)
        if base_x <= -SCREEN_WIDTH:
            base_x = 0
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()