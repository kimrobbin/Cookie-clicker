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
price_clicks = 100
auto_clicks = 0
auto_cps = 0

class Cookie:
    def __init__(self, x_pos, y_pos:int, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height


    def draw_cookie(self):

        cookie = pygame.image.load(f"cookies/cookies_{cookie_level}.png")
        cookie_rect = cookie.get_rect()
        cookie_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        window.blit(cookie, cookie_rect)
        return cookie_rect
    
    def draw_upgrade(self):
        upgrade_tekst_render = font.render(f"Upgrade cookie for {price_clicks}!", True, black)
        upgrade_tekst_rect = upgrade_tekst_render.get_rect(center=(WINDOW_WIDTH // 2, 50))

        window.blit(upgrade_tekst_render,upgrade_tekst_rect)
        return upgrade_tekst_rect

    def display_clicks(self):
        clicks_render = font.render(f"{clicks}", True, black)
        clicks_rect = clicks_render.get_rect(center=(WINDOW_WIDTH // 2, 80))
        window.blit(clicks_render,clicks_rect)


cookie_level = 1
# seter fonten

font = pygame.font.SysFont('Arial', 32)

# Objekt
cookie = Cookie(0,0)

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
                if upgrade_tekst_rect.collidepoint(event.pos) and clicks >= price_clicks:
                    cookie_level +=1
                    clicks -= price_clicks
                    if cookie_level == 2:
                         price_clicks = 200 
                    elif cookie_level == 3:
                         price_clicks = 500 
                    elif cookie_level == 4:
                         price_clicks = 1000 
                    else:
                        price_clicks *= 2

                    if cookie_level == 2:
                        cps = 5 
                    if cookie_level == 3:
                        cps = 20
                    if cookie_level == 4:
                        cps = 50 
                    elif cookie_level > 2:
                            cps *= 2 
            else:
                if upgrade_tekst_rect.collidepoint(event.pos) and clicks >= price_clicks:
                     price_clicks *=3
            if cookie_rect.collidepoint(event.pos):
                    clicks += cps




    window.fill((255, 255, 255))
    

    cookie_rect = cookie.draw_cookie()
    cookie.draw_upgrade()
    cookie.display_clicks()
    
    pygame.display.update()

pygame.quit()
