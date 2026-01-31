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

# seter fonten
font = pygame.font.SysFont('Arial', 24)






class Cookie:
    def __init__(self, x_pos, y_pos:int, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        
       # spill variabler 
        self.clicks = 999999
        self.cps = 1
        self.price_clicks = 100
        self.cookie_level = 1
        self.auto_cps = 0
        self.auto_price = 200
        self.auto_level = 0
        self.count = 1

    # Tegne delen:

    def draw_cookie(self):
        #Heneter bilde/spriten og putter den på plass
        cookie = pygame.image.load(f"cookies/cookies_{self.cookie_level}.png")
        cookie_rect = cookie.get_rect()
        cookie_rect.center = (self._width // 2, self._height // 2)

        window.blit(cookie, cookie_rect)
        return cookie_rect
    
    def draw_upgrade(self):
        #Teksten for å oppgradere
        upgrade_tekst_render = font.render(f"Upgrade cookie for {self.price_clicks}!", True,  "black")
        upgrade_tekst_rect = upgrade_tekst_render.get_rect(midleft=(10, 10))

        window.blit(upgrade_tekst_render,upgrade_tekst_rect)
        return upgrade_tekst_rect

    def draw_auto_price(self):
        #Teksten for å oppgradere 
        auto_tekst_render = font.render(f"Upgrade auto cookie for {self.auto_price}!", True,  "black")
        auto_tekst_rect = auto_tekst_render.get_rect(midleft=(10, 40))
        window.blit(auto_tekst_render,auto_tekst_rect)

        return auto_tekst_rect
    
    def stats(self):

        stats_render = font.render(f"Cps: {self.cps} \n Auto Cps: {self.auto_cps} \n Auto level: {self.auto_level} ", True, "black")
        stats_rect = stats_render.get_rect(midleft=(10,430))
        window.blit(stats_render,stats_rect)

    
    def auto_clicker(self):
        # Hvis count er minder en 60 +1. Hvis den er større eller = 60 så +1 
        if self.count < 60:
            self.count += 1
            # print("counting")
        elif self.count >= 60:
            # print("Gained one click ") 
            self.clicks += self.auto_cps
            self.count = 1 
            


    def display_clicks(self):
        clicks_render = font.render(f"You have {self.clicks} cookies!", True, "black")
        clicks_rect = clicks_render.get_rect(midleft=( 10,70 ))
        window.blit(clicks_render,clicks_rect)

# Definerer cookie
cookie = Cookie(WINDOW_WIDTH,WINDOW_HEIGHT)



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # if upgrade_tekst_rect.collidepoint(event.pos):
                #     print(f"hit , {upgrade_tekst_rect}")

                # Logikken for når cookie levelet er under 9 
                if cookie.cookie_level < 9: 
                    if upgrade_tekst_rect.collidepoint(event.pos) and cookie.clicks >= cookie.price_clicks:
                        cookie.cookie_level +=1
                        cookie.clicks -= cookie.price_clicks
                        
                        #Cookie pris update     
                        if cookie.cookie_level == 2:
                            cookie.price_clicks = 200 
                        elif cookie.cookie_level == 3:
                            cookie.price_clicks = 500 
                        elif cookie.cookie_level == 4:
                            cookie.price_clicks = 1000 
                        else:
                            cookie.price_clicks *= 2
                        # Cookie trykk update 
                        if cookie.cookie_level == 2:
                            cookie.cps = 5 
                        elif cookie.cookie_level == 3:
                            cookie.cps = 20
                        elif cookie.cookie_level == 4:
                            cookie.cps = 50 
                        elif cookie.cookie_level > 2:
                                cookie.cps *= 2
                else:
                    if upgrade_tekst_rect.collidepoint(event.pos) and cookie.clicks >= cookie.price_clicks:

                        cookie.clicks -= cookie.price_clicks
                        if cookie.cookie_level >= 9:
                            cookie.price_clicks *= 2
                            cookie.cps *= 2


                if auto_rect.collidepoint(event.pos) and cookie.clicks >= cookie.auto_price:
                    cookie.clicks -= cookie.auto_price
                    cookie.auto_level += 1 

                    # Oppgraderer hvor mange auto cookie gir og opptaterer prisen
                    if cookie.auto_level == 1:
                        cookie.auto_cps += 1 
                        cookie.auto_price += 400 
                    elif cookie.auto_level == 2:
                        cookie.auto_cps += 20 
                        cookie.auto_price += 1000 
                    elif cookie.auto_level == 3:
                        cookie.auto_cps += 50 
                        cookie.auto_price += 2000 
                    else:
                        cookie.auto_cps *= 2  
                        cookie.auto_price *= 2 
               
                    
                        


                if cookie_rect.collidepoint(event.pos):
                        cookie.clicks += cookie.cps
                


    # print(f"{cookie.auto_cps}, {cookie.auto_level}, {cookie.auto_price}")
    if cookie.auto_level >= 1:
        cookie.auto_clicker()
        



    window.fill((255, 255, 255))
    

    cookie.display_clicks()
    # Tegne funksjonene
    cookie_rect = cookie.draw_cookie()
    upgrade_tekst_rect = cookie.draw_upgrade()
    auto_rect = cookie.draw_auto_price()

    cookie.stats()


    pygame.display.update()
    clock.tick(fps)
pygame.quit()
