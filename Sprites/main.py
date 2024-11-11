import pygame


pygame.init()

Width = 600
Height = 500
display_surface = pygame.display.set_mode([Width, Height])
background = pygame.image.load("Background.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Rocket.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect= self.image.get_rect()

    def update(self, pressed_keys):
        if(pressed_keys[pygame.K_UP]):
            self.rect.move_ip(0,-1)
        if(pressed_keys[pygame.K_DOWN]):
            self.rect.move_ip(0,1)
        if(pressed_keys[pygame.K_LEFT]):
            self.rect.move_ip(-1,0)
        if(pressed_keys[pygame.K_RIGHT]):
            self.rect.move_ip(1,0)
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.top<0:
            self.rect.top = 0
        if self.rect.bottom > Height:
            self.rect.bottom = Height

sprites = pygame.sprite.Group()

def startGame():
    rocket = Player()
    sprites.add(rocket)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pressed_keys = pygame.key.get_pressed()
        rocket.update(pressed_keys)
        display_surface.blit(background, (0,0))
        sprites.draw(display_surface)
        pygame.display.update()

startGame()


