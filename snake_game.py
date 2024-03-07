import pygame
import sys
import random

pygame.init()
#############################################----1-----##################################
# Snake properties
window_width = 800
window_height = 600
snake_color = (255, 255, 0)  # Green color
snake_size = 20
snake_speed =5
bomb_size = 20   #bomb_size
food_size = 20
food_x = random.randint(0, window_width - food_size)
food_y = random.randint(0, window_height - food_size)
############################---bomb --####################################
bomb_x = random.randint(0, window_width - bomb_size)   # bomb_x
bomb_y= random.randint(0, window_height - bomb_size)    # bomb _y 
#############################################----2-----##################
# Draw the food
food = pygame.Rect(food_x, food_y, food_size, food_size)
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game by Amiran")
food_color = (255, 0, 0)  # Red color

food_image = pygame.image.load("apple.png")
food_image = pygame.transform.scale(food_image, (food_size, food_size))
#################### bomb Draw ########################
bomb = pygame.Rect(bomb_x, bomb_y, bomb_size, bomb_size)
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game by Amiran")
bomb_color = (255, 0, 0)  # Red color

bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (bomb_size, bomb_size))


###########################################
clock = pygame.time.Clock()

#############################################----3-----#####################################################
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(game_window, snake_color, block)

#############################################---4-----#####################################################
def game_over(score):
    game_window.fill((0, 0, 0))

    game_over_font = pygame.font.Font(None, 48)
    game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
    game_window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2,
                                      window_height // 2 - 48))

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render("Final score: " + str(score), True, (255, 255, 255))
    game_window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2))

    restart_font = pygame.font.Font(None, 24)
    restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
    game_window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 + 48))

    pygame.display.update()

#############################################----5-----#####################################################
def main():
    global score
    bomb_size = 20
    snake_x = window_width // 2
    snake_y = window_height // 2
    snake_dx = 0
    snake_dy = 0
    snake_size = 20
    snake_body =[ pygame.Rect(snake_x, snake_y, snake_size, snake_size)]
    snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
    ############## food ##############
    food_x = random.randint(0, window_width - food_size)
    food_y = random.randint(0, window_height - food_size)
    food = pygame.Rect(food_x, food_y, food_size, food_size)
    #############   bomb ##############
    bomb_x = random.randint(0,window_width - bomb_size)
    bomb_y = random.randint(0,window_height - bomb_size )
    bomb = pygame.Rect(bomb_x, bomb_y, bomb_size, bomb_size)
    ######################################
    score = 0
    high_score =0

    while True:
        game_window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_dy = -1
                    snake_dx = 0
                elif event.key == pygame.K_DOWN:
                    snake_dy = 1
                    snake_dx = 0
                elif event.key == pygame.K_LEFT:
                    snake_dx = -1
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx = 1
                    snake_dy = 0
            snake_speed= 5
            snake_x += snake_dx * snake_speed
            snake_y += snake_dy * snake_speed
            snake_size= 20
            bomb_size =20
            snake_head = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
            ###########  food colliderect  ################
            if snake_head.colliderect(food):
                    snake_size +=1
                    score += 1
                    snake_speed += 1
                    high_score +=1
                    if score > high_score:
                        high_score = score
                    snake_body.append(snake_body[-1])  # Grow the snake
                    food_x = random.randint(0, window_width - food_size)
                    food_y = random.randint(0, window_height - food_size)
                    food = pygame.Rect(food_x, food_y, food_size, food_size)
                    bomb_x = random.randint(0, window_width - bomb_size)
                    bomb_y = random.randint(0, window_height - bomb_size)
                    bomb = pygame.Rect(bomb_x, bomb_y, bomb_size, bomb_size)
            ####################   bomb colliderect #####################
            if snake_head.colliderect(bomb):
                    
                    bomb_size =20
                    #bomb_size -=1
                    score -= 1
                    snake_size -=1
                    snake_speed -= 1
                    high_score -=1
                    if score > high_score:
                        high_score = score
                    if score <= -1 :    #bomb-ზე შეხებისას რესტარტი
                        game_menu()
                    snake_body.append(snake_body[-1])  # Grow the snake
                    bomb_x = random.randint(0, window_width - bomb_size)
                    bomb_y = random.randint(0, window_height - bomb_size)
                    bomb = pygame.Rect(bomb_x, bomb_y, bomb_size, bomb_size)
            ######################################################################

        if len(snake_body) < 1 and snake.colliderect(snake_body[i] for i in range(1, len(snake_body))):
            game_over(score)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        main()

        if snake_x < 0 or snake_x + snake_size > window_width or \
                snake_y < 0 or snake_y + snake_size > window_height:
            game_over(score)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        main()
        snake_head = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
        snake_body = [snake_head] + snake_body[:-1]
        draw_snake(snake_body)

        game_window.blit(food_image, (food_x, food_y))
        game_window.blit(bomb_image , (bomb_x, bomb_y))
        pygame.display.update()
        clock.tick(10)
#############################################----6-----#####################################################
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    font = pygame.font.Font(None, 48)
#############################################----7-----#####################################################
def game_menu():
    score=0
    high_score= score
    game_window.fill((0, 0, 0))
    menu_font = pygame.font.Font(None, 36)
    start_text = menu_font.render("Press Enter to start", True, (255, 255, 255))
    game_window.blit(start_text, (window_width // 2 - start_text.get_width() // 2, window_height // 2))
    draw_text("Score: " + str(score), menu_font, (255, 255, 255), game_window, 70, 10)
    draw_text("High Score: " + str(high_score), menu_font, (255, 255, 255), game_window, 620, 10)
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
#############################################----8-----#####################################################
game_menu()
main()
