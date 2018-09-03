import pygame
pygame.init()

size = width, height = 1024, 768
black = 200, 200, 200

screen = pygame.display.set_mode(size)

room = pygame.image.load("images/room.png")
bg = pygame.image.load("images/room_background_origin.png")
roomrect = room.get_rect()
roomrect.left = width // 2 - 16
roomrect.top = height // 2 - 16
bgrect = bg.get_rect()

running = True
bgdraw = True

while running:
    dx = 0
    dy = 0

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
            elif event.key == pygame.K_SPACE:
                bgdraw = not bgdraw

    roomrect = roomrect.move(dx, dy)

    screen.fill(black)
    screen.blit(room, roomrect)
    if bgdraw:
        screen.blit(bg, roomrect)
    pygame.display.flip()
    pygame.time.delay(1000 // 60)
