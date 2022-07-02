import pygame, random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#產生畫布
pygame.display.set_caption("Bitting Image")

#set FPS
FPS = 60
clock = pygame.time.Clock()

#set game valus
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCOTY = 10
COIN_acceleration = 0.5#加速度
BUFFER_DISTANCE = 100

score = 0
lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCOTY

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.Font("hi.ttf.ttf", 32)

score_text = font.render("Scors: "+str(score), True, GREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

title_text = font.render("Feed the Angry bird"+str(score), True, GREEN)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH//2
title_text_rect.y = 10

lives_text = font.render("Lives: "+str(lives), True, GREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH-10, 10)

gameover_text = font.render("GAMEOVER", True, GREEN)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press anykeyto play again", True, GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+32)


coin_sound = pygame.mixer.Sound("coin.wav")
miss_sound = pygame.mixer.Sound("miss.wav")
miss_sound.set_volume(1.0)
pygame.mixer.music.load("background_music.wav")

player_image = pygame.image.load("dafumom.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("shit.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH+BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT-32)

pygame.mixer.music.play(-1, 0.0)

running=True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    #key move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top>64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom<WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    #Coin move
    if coin_rect.x<0:
        lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH+BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT-32)
    else:
        coin_rect.x -= coin_velocity
    #Check the collision
    if player_rect.colliderect(coin_rect):
        score +=1 
        coin_sound.play()
        coin_velocity += COIN_acceleration
        coin_rect.x = WINDOW_WIDTH +BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT-32)
    #Update the text
    score_text = font.render("Scors: "+str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: "+str(lives), True, GREEN, DARKGREEN)
    #check_for_pameover
    if lives<=0:
        displayscreen.blit(gameover_text, gameover_text_rect)
        displayscreen.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running   = False
                    
                if event.type == pygame.KEYDOWN:
                    score         = 0
                    lives         = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCOTY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused    = False
                    

                
    
    displayscreen.fill(BLACK)
    displayscreen.blit(score_text, score_text_rect)
    displayscreen.blit(title_text, title_text_rect)
    displayscreen.blit(lives_text, lives_text_rect)
    pygame.draw.line(displayscreen, WHITE, (0, 64), (WINDOW_WIDTH, 64), 3)
    
    displayscreen.blit(player_image, player_rect)
    displayscreen.blit(coin_image, coin_rect)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()