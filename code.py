import pygame
from os import startfile

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("Files/Sound/walk.mp3")
pygame.mixer.music.set_volume(0.5)

font = pygame.font.Font("Files/Pixeltype.ttf", 40)
font_2 = pygame.font.Font("Files/Pixeltype.ttf", 70)
test_surf = pygame.image.load("Files/map.png")
text = font.render("Hahaha, You thought", False, "Black")
text_2 = font.render("I can feel it coming...", False, "Black")
text_3 = font.render("Wdym", False, "Black")
text_rect = text.get_rect(topleft=(350, 450))

c1 = pygame.image.load("Files/Walking/0.png")
c2 = pygame.image.load("Files/Walking/1.png")
c3 = pygame.image.load("Files/Walking/2.png")
c4 = pygame.image.load("Files/Walking/3.png")
c5 = pygame.image.load("Files/Walking/4.png")

c1_l = pygame.image.load("Files/Left/00.png")
c2_l = pygame.image.load("Files/Left/0.png")
c3_l = pygame.image.load("Files/Left/1.png")
c4_l = pygame.image.load("Files/Left/2.png")
c5_l = pygame.image.load("Files/Left/3.png")

btn = pygame.image.load("Files/btn.png")
btn_r1 = btn.get_rect(center=(100, 600))
btn2 = pygame.image.load("Files/btn_2.png")
btn_r2 = btn.get_rect(center=(100, 600))
btn_state = 0

dummy_l = pygame.image.load("Files/Static/Left.png")
dummy_state = dummy_r = pygame.image.load("Files/Static/Right.png")
dummy_rect = dummy_r.get_rect(center=(460, 550))

start_surf = pygame.Surface((700, 700))
text_start = font_2.render("Hit Space to Unpause", False, "White")
start_surf.fill("Black")

start = False
position = [180, 30]
state_var = 0
pressed = False        
side = 0
counter = 0
start_counter = False
show_text = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
        if btn_state == 1 and event.type == pygame.MOUSEBUTTONDOWN and btn_r1.collidepoint(event.pos):
            dummy_state = dummy_l
            show_text = True

    if start:
        screen.blit(test_surf, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not side:
                side = 1
            else:
                position[0] -= 4
            pressed = True
        elif keys[pygame.K_RIGHT]:
            if side:
                side = 0
            else:
                position[0] += 4
            pressed = True
        elif keys[pygame.K_UP]:
            pressed = True
            position[1] -= 4
        elif keys[pygame.K_DOWN]:
            pressed = True
            position[1] += 4
        else:
            pressed = False

        if not pressed: 
            pygame.mixer.music.stop() 
            if not side:
                screen.blit(c1, position)
                state_var = 0
                current_state = c2
            else:
                screen.blit(c1_l, position)
                state_var = 0
                current_state = c2_l
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            if not side:
                state_var += 1
                if state_var == 5:
                    current_state = c3
                elif state_var == 10:
                    current_state = c4
                elif state_var == 15:
                    current_state == c5
                elif state_var == 20:
                    current_state = c2
                    state_var = 0
                screen.blit(current_state, position)
            else:
                state_var += 1
                if state_var == 5:
                    current_state = c3_l
                elif state_var == 10:
                    current_state = c4_l
                elif state_var == 15:
                    current_state == c5_l
                elif state_var == 20:
                    current_state = c2_l
                    state_var = 0
                screen.blit(current_state, position)

        screen.blit(dummy_state, dummy_rect)
        if not btn_state:
            screen.blit(btn2, btn_r2)
        else:
            screen.blit(btn, btn_r1)

        x1, y1 = list(dummy_rect.topleft)
        x1, y1 = x1 - 200, y1 - 200
        x2, y2 = list(dummy_rect.bottomright)
        x2, y2 = x2 + 200, y2 + 200
        x, y = position
        if x2 >= x >= x1 and y2 >= y >= y1:
            btn_state = 1
        else:
            btn_state = 0
        
        if show_text and counter < 60:
            pygame.draw.rect(screen, "white", text_rect, 10)
            pygame.draw.rect(screen, "white", text_rect)
            screen.blit(text, text_rect)
            start_counter = True

        if start_counter:
            counter += 1
            btn_state = False
            if 180 > counter >= 80:
                pygame.draw.rect(screen, "white", text_rect, 10)
                pygame.draw.rect(screen, "white", text_rect)
                screen.blit(text_2, text_rect)
            elif 280 >= counter >= 180:
                rect = pygame.Rect(position[0] + 30, position[1] - 30, 50, 30)
                pygame.draw.rect(screen, "white", rect, 10)
                pygame.draw.rect(screen, "white", rect)
                screen.blit(text_3, rect)
            elif counter > 280:
                startfile("Files\\Static\\End.mp4")
                pygame.quit()
                exit()
    else:
        screen.blit(start_surf, (0, 0))
        screen.blit(text_start, (130, 300))

    pygame.display.update()
    clock.tick(60)