import pygame
pygame.init()

size = width, height = 1024, 768
black = 200, 200, 200

screen = pygame.display.set_mode(size)

room = pygame.image.load("images/room.png")
roomrect = room.get_rect()
roomrect.left = width // 2 - 16
roomrect.top = height // 2 - 16

running = True

dx = 0
dy = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
                continue
            elif event.key == pygame.K_DOWN:
                dy -= 32
            elif event.key == pygame.K_UP:
                dy += 32
            elif event.key == pygame.K_LEFT:
                dx += 32
            elif event.key == pygame.K_RIGHT:
                dx -= 32

    roomrect = roomrect.move(dx, dy)
    dx = 0
    dy = 0

    screen.fill(black)
    screen.blit(room, roomrect)
    pygame.display.flip()
    pygame.time.delay(1000 // 60)
