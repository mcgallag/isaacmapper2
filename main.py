import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

room = pygame.image.load("images/room.png")
roomrect = room.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    roomrect = roomrect.move(speed)

    if roomrect.left < 0 or roomrect.right > width:
        speed[0] = -speed[0]
    if roomrect.top < 0 or roomrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(room, roomrect)
    pygame.display.flip()
