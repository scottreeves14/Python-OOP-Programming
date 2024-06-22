# Pygame Game Dev
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
# Initialise Score
font = pygame.font.Font(None, 36)
score = 0

# Creating a player class with attributes of position and speed

class Player():
    def __init__(self):
        self.position = [0, 40]
        self.speed = 20
        self.size = [20,20]

    # Adding a method to the player class for movement
    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed
        
    def move_down(self):
        self.position[1] += self.speed

# Creating a player Obstacle
class Obstacle():
    def __init__(self):
        self.position = [random.randint(0, 39)*20, random.randint(0,28)*20+20]
        self.size = [20, 20]
        
# Instantiating one instance called player 1

player_one = Player()

# Instantiating the obstacle class
num_obstacles = 10
obstacles = []
for i in range(0, num_obstacles):
    obstacles.append(Obstacle())

def check_collision(player):
    collision = -1
    for i in range(0, num_obstacles):
        if (player.position[0] == obstacles[i].position[0] and
          player.position[1] == obstacles[i].position[1]):
            collision = i
    return collision
        
game_running = True
# Event handling here
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
                
    if check_collision(player_one) >= 0:
        # This code will run if the player started colliding with the obstacle this frame
        score += 1
        # Re-instantiate the obstacle at a new location
        obstacles[check_collision(player_one)] = Obstacle()
     
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw player here
    pygame.draw.rect(screen, (0,0,0), (player_one.position[0], player_one.position[1], player_one.size[0], player_one.size[1]))
    # Draw obstacles
    for i in range(0, num_obstacles):
        pygame.draw.rect(screen, (255,0,0), (obstacles[i].position[0], obstacles[i].position[1], obstacles[i].size[0], obstacles[i].size[1]))
    text = font.render("Score: " + str(score), 1, (10, 10, 10))
    screen.blit(text, (10,10))
    # Swap buffers
    pygame.display.flip()
    
pygame.quit()

