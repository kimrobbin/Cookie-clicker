import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

window = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
pygame.display.set_caption("Cookie clicker")

# farger 
black = (0,0,0)


#cliker variabler 
clicks = 0
cps = 1 
auto_clicks = 0
auto_cps = 0

class Cookie:
    def __init__(self, x_pos:int, y_pos:int, width:int, height:int):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height

    def draw(self):
        upgrade_tekst_render = font.render("Upgrade cookie!", True, black)
        upgrade_tekst_rect = upgrade_tekst_render.get_rect(center=(WINDOW_WIDTH // 2, 50))

        cookie = pygame.image.load(f"cookies/cookies_{cookie_level}.png")
        cookie_rect = cookie.get_rect()
        cookie_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        window.blit(upgrade_tekst_render,upgrade_tekst_rect)
        window.blit(cookie, cookie_rect)
        return cookie_rect

    def display_clicks(self):
        clicks_render = font.render(f"{clicks}", True, black)
        clicks_rect = clicks_render.get_rect(center=(WINDOW_WIDTH // 2, 80))
        window.blit(clicks_render,clicks_rect)








cookie_level = 1
# Tekst delen

font = pygame.font.SysFont('Arial', 32)

# Initialize Cookie object
cookie = Cookie(0,0,0,0)

# For collision detection
upgrade_tekst_render = font.render("Upgrade cookie!", True, black)
upgrade_tekst_rect = upgrade_tekst_render.get_rect(center=(WINDOW_WIDTH // 2, 50))
cookie_rect = None

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_level < 9: 
                if upgrade_tekst_rect.collidepoint(event.pos):
                    cookie_level +=1
                    if cookie_level == 2:
                        cps = 5 
                    elif cookie_level > 2:
                            cps *= 2 
            if cookie_rect.collidepoint(event.pos):
                    clicks += cps

    window.fill((255, 255, 255))
    
    # Use Cookie class to draw everything
    cookie_rect = cookie.draw()
    cookie.display_clicks()
    
    pygame.display.update()

pygame.quit()
