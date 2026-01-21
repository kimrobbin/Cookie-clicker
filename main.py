import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

window = pygame.display.set_mode([WINDOW_HEIGHT,WINDOW_WIDTH])
pygame.display.set_caption("Cookie clicker")


class Cookie:
    def __init__(self, x_pos, y_pos,width, height):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height

    def draw():
        
        cookie = pygame.image.load(f"cookies/cookies_{cookie_level}.png")
        cookie_rect = cookie.get_rect()
        cookie_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        window.blit(cookie, cookie_rect)







cookie_level = 1


font = pygame.font.SysFont('Arial', 32)

upgrade_tekst_render = font.render("Upgrade cookie!", True, (0,0,0))
upgrade_tekst_rect = upgrade_tekst_render.get_rect(center=(WINDOW_HEIGHT // 2, 50))
upgrade_tekst_rect.center = (WINDOW_HEIGHT // 2, 50)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
                if cookie_level < 9: 

                        if upgrade_tekst_rect.collidepoint(event.pos):
                            cookie_level +=1

            


    window.fill((255, 255, 255)) 
    window.blit(upgrade_tekst_render,upgrade_tekst_rect)

    Cookie.draw()


    
    pygame.display.update()

pygame.quit()
