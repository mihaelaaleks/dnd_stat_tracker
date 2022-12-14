import pygame, sys
from button import Button
import setup

pygame.init()

game_paused = False
menu_state = "main"
screen = pygame.display.set_mode((setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

bg = pygame.image.load(setup.BG_IMG)

font = pygame.font.Font("assets/font.ttf", 40)

options_button = Button(304, 125, setup.BTN_IMG, 1)
resume_button = Button(304, 125, setup.BTN_IMG, 1)
dice_button = Button(304, 125, setup.BTN_IMG, 1)
sheet_button = Button(304, 125, setup.BTN_IMG, 1)
quit_button = Button(304, 125, setup.BTN_IMG, 1)

def draw_text(text, font, text_col, x, y): 
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
# game loop 
run = True
while run: 
    screen.fill(bg)
    
    if game_paused == True: 
        if menu_state == "main": 
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen): 
                menu_state = "options"
            if quit_button.draw(screen): 
                pygame.quit()
                sys.exit()

                    
def main_menu(): 
    while True: 
        SCREEN.blit(BG, (0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        MENU_TEXT = get_font(100).render("D&D HelpeR", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        
        PLAY_BUTTON = Button(image = pygame.image.load("assets/rect.png"), pos=(640,250), text_input="PLAY", font=get_font(30), 
                             base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image = pygame.image.load("assets/rect.png"), pos=(640,400), text_input="OPTIONS", font=get_font(30), 
                             base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image = pygame.image.load("assets/rect.png"), pos=(640,550), text_input="QUIT", font=get_font(30), 
                             base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        buttons = [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]
        
        for button in buttons: 
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): 
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): 
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): 
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        
main_menu()