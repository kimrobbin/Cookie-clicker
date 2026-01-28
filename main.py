import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

window = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
pygame.display.set_caption("Cookie clicker")

# farger 
black = (0,0,0)

# FPS variabler
clock = pygame.Clock()
fps = 60

#cliker variabler 
clicks = 0
cps = 1 
price_clicks = 100

auto_cps = 0
auto_price = 200
auto_level = 0
count = 1

class Cookie:
    def __init__(self, x_pos, y_pos:int, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height


    def draw_cookie(self):
        cookie = pygame.image.load(f"cookies/cookies_{cookie_level}.png")
        cookie_rect = cookie.get_rect()
        cookie_rect.center = (self._width // 2, self._height // 2)

        window.blit(cookie, cookie_rect)
        return cookie_rect
    
    def draw_upgrade(self):
        upgrade_tekst_render = font.render(f"Upgrade cookie for {price_clicks}!", True, black)
        upgrade_tekst_rect = upgrade_tekst_render.get_rect(center=(self._width // 2, 30))

        window.blit(upgrade_tekst_render,upgrade_tekst_rect)
        return upgrade_tekst_rect

    def draw_auto_price(self):
        auto_tekst_render = font.render(f"Upgrade auto cookie for {auto_price}!", True, black)
        auto_tekst_rect = auto_tekst_render.get_rect(center=(self._width // 2, 450))
        window.blit(auto_tekst_render,auto_tekst_rect)

        return auto_tekst_rect

    def auto_clicker(self):
        global count
        global clicks

        # Hvis count er minder en 60 +1. Hvis den er større eller = 60 så +1 
        if count < 60:
            count += 1
            # print("counting")
        elif count >= 60:
            # print("Gained one click ") 
            clicks += auto_cps
            count = 1 

    def display_clicks(self):
        clicks_render = font.render(f"{clicks}", True, black)
        clicks_rect = clicks_render.get_rect(center=(self._width // 2, 110))
        window.blit(clicks_render,clicks_rect)


cookie_level = 1
# seter fonten

font = pygame.font.SysFont('Arial', 30)

# Definerer cookie
cookie = Cookie(WINDOW_WIDTH,WINDOW_HEIGHT)

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
                    
                     #Cookie pris update     
                    if cookie_level == 2:
                         price_clicks = 200 
                    elif cookie_level == 3:
                         price_clicks = 500 
                    elif cookie_level == 4:
                         price_clicks = 1000 
                    else:
                        price_clicks *= 2
                    # Cookie trykk update 
                    if cookie_level == 2:
                        cps = 5 
                    elif cookie_level == 3:
                        cps = 20
                    elif cookie_level == 4:
                        cps = 50 
                    elif cookie_level > 2:
                            cps *= 2

            if auto_rect.collidepoint(event.pos) and clicks >= auto_price:
                clicks -= auto_price
                auto_level += 1 
                if auto_level == 1:
                    auto_cps += 1 
                elif auto_level == 2:
                    auto_cps += 5 
                elif auto_level == 3:
                    auto_cps += 10 
                else:
                    auto_cps *= 2 

                if auto_level == 1:
                    auto_price += 400 
                elif auto_level == 1:
                    auto_price += 1000 
                elif auto_level == 1:
                    auto_price += 2000 
                else:
                    auto_price *= 2 
                 
                    
            else:
                if upgrade_tekst_rect.collidepoint(event.pos) and clicks >= price_clicks:
                    price_clicks *=3
                    if cookie_level >= 13:
                         price_clicks *= 8


            if cookie_rect.collidepoint(event.pos):
                    clicks += cps

    # print(f"{auto_cps}, {auto_level}, {auto_price}")
    if auto_level >= 1:
        cookie.auto_clicker()



    window.fill((255, 255, 255))
    

    cookie_rect = cookie.draw_cookie()
    cookie.draw_upgrade()
    cookie.display_clicks()
    auto_rect = cookie.draw_auto_price()


    pygame.display.update()
    clock.tick(fps)
pygame.quit()
