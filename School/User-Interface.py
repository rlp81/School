import pygame
import time
WIDTH, HEIGHT = 500, 500
pygame.display.set_caption("User-Interface")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
back = pygame.image.load(".\\assets\\background-black.png")
pygame.display.set_icon(back)
BG = pygame.transform.scale(back, (WIDTH, HEIGHT))
def projects():
    run = True
    font = pygame.font.SysFont("comicsans", 40)
    pos = (WIDTH/2 - 400/2)
    while run:
        screen.blit(BG, (0,0))
        title_label = font.render("Space Invaders", 1, (0,0,0))
        title_label1 = font.render("Tetris", 1, (0,0,0))
        button = pygame.Rect(pos, 50, 400, 50)
        button1 = pygame.Rect(pos, 110, 400, 50)
        pygame.draw.rect(screen, [255, 255, 255], button)
        pygame.draw.rect(screen, [255, 255, 255], button1)
        screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 60))
        screen.blit(title_label1, (WIDTH/2 - title_label1.get_width()/2, 120))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if button.collidepoint(mousepos):
                    run = False
                    pygame.quit()
                    import Space
                if button1.collidepoint(mousepos):
                    run = False
                    pygame.quit()
                    import Tetris
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
def main():
    run = True
    title_font = pygame.font.SysFont("comicsans", 40)
    while run:
        screen.blit(BG, (0,0))
        pos = (WIDTH/2 - 400/2)
        button = pygame.Rect(pos, 200, 400, 50)
        pygame.draw.rect(screen, [255, 255, 255], button)
        title_label = title_font.render("Cole's Projects", 1, (255,255,255))
        title_label1 = title_font.render("Projects", 1, (0,0,0))
        screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 100))
        screen.blit(title_label1, (WIDTH/2 - title_label1.get_width()/2, 210))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if button.collidepoint(mousepos):
                    run = False
                    projects()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        pygame.display.update()
def load():
    screen.blit(BG, (0,0))
    title_font = pygame.font.SysFont("comicsans", 70)
    loading = True
    size = 10
    pos = (WIDTH/2 - 400/2)
    load = pygame.Rect(pos, 200, 400, 50)
    pygame.draw.rect(screen, [255, 255, 255], load)
    while loading:
        load_label = title_font.render("Loading", 1, (0,0,0))
        load1 = pygame.Rect(pos, 200, size, 50)
        pygame.draw.rect(screen, [0, 255, 0], load1)
        screen.blit(load_label, (WIDTH/2 - load_label.get_width()/2, 200))
        if size == 400:
            loading = False
            main()
        if not size == 400:
            size += 1
            pygame.display.update()
            time.sleep(.02)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.QUIT:
                loading = False
                pygame.quit()

load()