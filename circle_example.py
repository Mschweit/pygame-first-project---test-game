# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

windowWidth = 1280
windowHeight = 720
displaySurface = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
running = True
dt = 0

playerStartLocation = pygame.Vector2(windowWidth / 2, windowHeight / 2)
player_pos = playerStartLocation

# origin = top left corner with the co-ordinates (0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    displaySurface.fill("purple")


    # draw player
    pygame.draw.circle(screen, "red", player_pos, 40)


    # keep player in-bounds
    
    # get keys currently pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt


    # display player coordinates
    if pygame.font:
        font = pygame.font.Font(None, 32)
        text = font.render(f'{player_pos}', True, (10, 10, 10))
        textpos = text.get_rect(windowWidth / 2, y=10)
        displaySurface.blit(text, textpos)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()