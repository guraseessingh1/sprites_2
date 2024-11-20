import pygame

WIDTH = 700
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("robot as sprites")

#player class is a child class an sprite class will be the parent class for inheriting the propertys from parent
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #innitialising the propertys of parent class
        super().__init__()
        self.image = pygame.image.load("images/robot.png")
        self.rect = self.image.get_rect()

    def update(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys_pressed[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_d]:
            self.rect.move_ip(5,0)

# creating sprite group to use sprites
sprite_group = pygame.sprite.Group()

def start_game():
    #creating object of our player class
    
    robot = Player()
    #adding sprite to the group
    sprite_group.add(robot)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        robot.update(keys_pressed)
        screen.fill((255,255,255))
        sprite_group.draw(screen)
        pygame.display.update()
start_game()



        


      

      
    



