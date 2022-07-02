import pygame, random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#產生畫布
pygame.display.set_caption("Bitting Image")

#set FPS(Freqency Per Sound) andclock(抓CPU的時序)
FPS=60
clock = pygame.time.Clock()

#set game values
VELOCITY = 5#速率
BLACK = (0,0,0)

angry_bird = pygame.image.load("angrybird.png")
angry_bird_rest = angry_bird.get_rect()
angry_bird_rest.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin = pygame.image.load("shit.png")
coin_rest = coin.get_rect()
coin_rest.center = (100,100)


running=True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()#偵測目前有哪個鍵按下
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and angry_bird_rest.left>0:
        angry_bird_rest.x -= VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and angry_bird_rest.top>0:
        angry_bird_rest.y -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and angry_bird_rest.right<WINDOW_WIDTH:
        angry_bird_rest.x += VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and angry_bird_rest.bottom<WINDOW_HEIGHT:
        angry_bird_rest.y += VELOCITY
        
    if angry_bird_rest.colliderect(coin_rest):
        print("HIT")
        coin_rest.x = random.randint(0, WINDOW_WIDTH-50)
        coin_rest.y = random.randint(0, WINDOW_HEIGHT-50)
        
    displayscreen.fill(BLACK)
    displayscreen.blit(angry_bird, angry_bird_rest)
    displayscreen.blit(coin, coin_rest)
    pygame.display.update()
    clock.tick(FPS)
    

pygame.quit()