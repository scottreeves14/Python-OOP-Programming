import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
# Initialise Score
font = pygame.font.Font(None, 36)
score = 0

#Define the player class
class Player():
    def __init__(self):
        self.position = [0, 40]
        self.speed = 20
        self.size = [20,20]

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed
        
    def move_up(self):
        self.position[1] -= self.speed
        
    def move_down(self):
        self.position[1] += self.speed

#Create Obstacle class
class Obstacle():
    def __init__(self):
        self.position = [random.randint(0, 39)*20, random.randint(0,28)*20+20]
        self.size = [20, 20]

def check_collision(player, obstacle):
    if (player.position[0] == obstacle.position[0] and
        player.position[1] == obstacle.position[1]):
        return True
    return False

        

#this creates an instance of player 1
player_one = Player()
obstacle = Obstacle()

font = pygame.font.Font(None, 36)
score = 0

game_running = True
#Event Handling
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_one.move_right()
            if event.key == pygame.K_LEFT:
                player_one.move_left()
            if event.key == pygame.K_UP:
                player_one.move_up()
            if event.key == pygame.K_DOWN:
                player_one.move_down()
                
    if check_collision(player_one, obstacle):
        score += 1
        obstacle = Obstacle()
  
        
    # Clear the screen
    screen.fill((255, 255, 255))
       
            
    # Draw player
    pygame.draw.rect(screen, (0,0,0), (player_one.position[0], player_one.position[1], player_one.size[0], player_one.size[1]))
    # Draw obstacle
    pygame.draw.rect(screen, (255,0,0), (obstacle.position[0], obstacle.position[1], obstacle.size[0], obstacle.size[1]))
    text = font.render("Score: " + str(score), 1, (10, 10, 10))
    screen.blit(text, (10,10))
    # Swap buffers
    pygame.display.flip()          
pygame.quit()
