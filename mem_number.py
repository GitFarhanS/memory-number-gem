import pygame
import random
import time
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 50)

class Button:
    def __init__(self, x, y, width, height, color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, font, BLACK, surface, self.rect.centerx, self.rect.centery)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class SlidingNumberDisplay:
    def __init__(self, screen, width, height, font):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = font
        self.color = BLACK
        self.digits = 1
        self.number = str(random.randint(0, 9))
        self.x = self.width
        self.y = 20
        self.speed = 0.1

    def draw(self):
        text_surface = self.font.render(self.number, True, self.color)
        self.screen.blit(text_surface, (self.x, self.y))
        self.x -= self.speed

    def reset(self):
        self.number = str(random.randint(10**(self.digits), 10**(self.digits+1)-1))
        self.digits += 1
        self.x = self.width
        self.draw()
    
    def lost_round(self):
        self.digits = 0
        self.reset()
    
    def get_value(self):
        return self.number

class Score:
    def __init__(self, x, y, font):
        self.score = 0
        self.x = x
        self.y = y
        self.font = font

    def draw(self, surface):
        draw_text(f"Score: {self.score}", self.font, BLACK, surface, self.x, self.y)

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0

class NumberPad:
    def __init__(self):
        self.screen_width = 440
        self.screen_height = 650
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Simple memory game")

        self.buttons = []
        self.create_buttons()

        self.sliding_number_display = SlidingNumberDisplay(self.screen, self.screen_width, self.screen_height, font)
        self.text_box = TextBox(50, 50, self.screen_width - 100, 50, font)

        self.score = Score(70, 630, font)

    def create_buttons(self):
        button_width = 100
        button_height = 100
        spacing = 20
        start_x = 50
        start_y = 150

        number = 1
        for row in range(3):
            for col in range(3):
                x = start_x + col * (button_width + spacing)
                y = start_y + row * (button_height + spacing)
                action = getattr(self, f'button_{number}_action')
                self.buttons.append(Button(x, y, button_width, button_height, GRAY, str(number), action))
                number += 1

        # Add the 0, Delete, and Enter buttons
        self.buttons.append(Button(start_x + button_width + spacing, start_y + 3 * (button_height + spacing), button_width, button_height, RED, "0", self.button_0_action))
        self.buttons.append(Button(start_x, start_y + 3 * (button_height + spacing), button_width, button_height, BLUE, "Del", self.button_del_action))
        self.buttons.append(Button(start_x + 2 * (button_width + spacing), start_y + 3 * (button_height + spacing), button_width, button_height, BLUE, "Enter", self.button_enter_action))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.is_clicked(mouse_pos):
                            if button.action:
                                button.action()

            self.screen.fill(WHITE)

            self.sliding_number_display.draw()

            for button in self.buttons:
                button.draw(self.screen)
            
            # Draw the text box
            self.text_box.draw(self.screen)

            # Draw the score
            self.score.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def flash_screen(self, color, duration=0.2):
        original_surface = self.screen.copy()
        self.screen.fill(color)
        pygame.display.flip()
        time.sleep(duration)
        self.screen.blit(original_surface, (0, 0))
        pygame.display.flip()

    def update_text_box(self, text):
        self.text_box.update_text(text)
    
    def set_text(self, text):
        self.text_box.set_text(text)
    
    def get_text(self):
        return self.text_box.get_text()

    def button_1_action(self):
        self.update_text_box("1")

    def button_2_action(self):
        self.update_text_box("2")

    def button_3_action(self):
        self.update_text_box("3")

    def button_4_action(self):
        self.update_text_box("4")

    def button_5_action(self):
        self.update_text_box("5")

    def button_6_action(self):
        self.update_text_box("6")

    def button_7_action(self):
        self.update_text_box("7")

    def button_8_action(self):
        self.update_text_box("8")

    def button_9_action(self):
        self.update_text_box("9")

    def button_0_action(self):
        self.update_text_box("0")

    def button_del_action(self):
        current_text = self.get_text()
        if current_text:
            self.set_text(current_text[:-1])

    def button_enter_action(self):
        if self.get_text() != self.sliding_number_display.get_value():
            print("Incorrect")
            self.flash_screen(RED)
            self.set_text("")
            self.sliding_number_display.lost_round()
            self.score.reset()  
        else:
            print("Correct")
            self.flash_screen(GREEN)
            self.set_text("")
            self.sliding_number_display.reset()
            self.score.increase()

class TextBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = ""
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        draw_text(self.text, self.font, BLACK, surface, self.rect.centerx, self.rect.centery)

    def update_text(self, new_text):
        self.text = self.text + new_text
    
    def set_text(self, new_text):
        self.text = new_text

    def get_text(self):
        return self.text

if __name__ == "__main__":
    NumberPad().run()
