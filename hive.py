import sys, pygame
import map.hex_map as map
m = map.Map(5,5)
pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
w_queen = pygame.image.load("./assets/w_queen.png")
w_queenrect = w_queen.get_rect()
v = w_queen.get_rect().collidepoint([1,1])
gamepieces = [w_queenrect]


def handle_clicked_pieces(pieces, pos):
    for piece in pieces:
        print(piece)
        #global clicked_piece 
        #clicked_piece = piece.get_rect()


    if len(pieces) == 0:
        #clicked_piece.x = pos[0]
        #clicked_piece.y = pos[1]
        #w_queenrect.x = pos[0]
        #w_queenrect.y = pos[1]
        w_queenrect.center = pos
        #clicked_piece = None

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_DOWN: w_queenrect = w_queenrect.move([0, 1])
            if event.key == pygame.K_UP: w_queenrect = w_queenrect.move([0, -1])
            if event.key == pygame.K_LEFT: w_queenrect = w_queenrect.move([-1, 0])
            if event.key == pygame.K_RIGHT: w_queenrect = w_queenrect.move([1, 0])

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in gamepieces if s.collidepoint(pos)]
            handle_clicked_pieces(clicked_sprites, pos)
    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(w_queen, w_queenrect)
    pygame.display.flip()