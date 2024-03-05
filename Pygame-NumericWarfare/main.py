import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("NumericWarfare")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
bigfont=pygame.font.Font(None, 54)

player_hp = 3
enemy_hp = 10

numbers1=random.randint(1, 100)
numbers2=random.randint(1, 100)

user_input = ""

enemy_surface = pygame.image.load("Enemy/Sprite-0003.png").convert()
enemy_rect = enemy_surface.get_rect(center=(400, 100))

playerhp_surface=font.render(f"Player HP: {player_hp}",False,(255,255,255)).convert()

enemyhp_surface=font.render(f"Enemy Hp:{enemy_hp}",False,(255,255,255)).convert()

question_surface=bigfont.render(f"What is the answer of {numbers1}+{numbers2}",False,(255,255,255)).convert()

text_surface= bigfont.render(f"",False,(255,255,255)).convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif player_hp<=0:
            text_surface = bigfont.render(f"Your HP is 0! You lose the game!", False, (255, 255, 255)).convert()
        elif enemy_hp<=0:
            text_surface = font.render(f"The enemy's HP is 0! You win the game!", False, (255, 255, 255)).convert()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    user_answer = int(user_input)
                    text_surface = bigfont.render(f"Your answer is {user_answer}", False, (255, 255, 255)).convert()

                    if user_answer == numbers1 + numbers2:
                        enemy_hp -= 1
                        text_surface = bigfont.render(f"Your answer is {user_answer},correct!", False, (255, 255, 255)).convert()
                    else:
                        player_hp -= 1
                        text_surface = bigfont.render(f"Your answer is {user_answer},wrong!", False, (255, 255, 255)).convert()

                    playerhp_surface = font.render(f"Player HP: {player_hp}", False, (255, 255, 255)).convert()
                    enemyhp_surface = font.render(f"Enemy HP: {enemy_hp}", False, (255, 255, 255)).convert()

                    numbers1 = random.randint(1, 100)
                    numbers2 = random.randint(1, 100)
                    question_surface = bigfont.render(f"What is the answer of {numbers1}+{numbers2}?", False,
                                                      (255, 255, 255)).convert()

                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                user_input = ""

            elif event.key in (
            pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
            pygame.K_9):
                user_input += event.unicode

    screen.fill((0, 0, 0))

    screen.blit(enemy_surface, enemy_rect)

    screen.blit(playerhp_surface, (0, 0))
    screen.blit(enemyhp_surface, (0, 30))
    screen.blit(question_surface,(150,200))
    screen.blit(text_surface,(150,300))

    pygame.display.update()
    clock.tick(60)
