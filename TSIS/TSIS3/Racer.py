import pygame
import sys
import random
import json
import os
from pygame.locals import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
PURPLE = (160, 32, 240)

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

pygame.init()
pygame.mixer.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Extreme Racing")
clock = pygame.time.Clock()
FONT_SMALL = pygame.font.SysFont("Verdana", 20)
FONT_MEDIUM = pygame.font.SysFont("Verdana", 35)
FONT_BIG = pygame.font.SysFont("Verdana", 50)

def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return default

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)
        self.speed = 5
        self.shield = False
        self.nitro_active = False

    def update(self):
        keys = pygame.key.get_pressed()
        curr_speed = self.speed * 2 if self.nitro_active else self.speed
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-curr_speed, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(curr_speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.spawn_safely(speed)

    def spawn_safely(self, speed):
        self.speed = speed
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, speed):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((40, 40))
        if type == 'oil': self.image.fill(BLACK)
        elif type == 'pothole': self.image.fill(GRAY)
        else: self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.image = pygame.Surface((30, 30))
        if kind == 'nitro': self.image.fill(GREEN)
        elif kind == 'shield': self.image.fill(BLUE)
        else: self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), -50)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Game:
    def __init__(self):
        self.settings = load_json(SETTINGS_FILE, {"sound": True, "color": "BLUE", "diff": "Medium"})
        self.leaderboard = load_json(LEADERBOARD_FILE, [])
        self.state = "MENU"
        self.username = "Player"
        self.reset_game_stats()

    def reset_game_stats(self):
        self.score = 0
        self.distance = 0
        self.coins_collected = 0
        self.speed_multiplier = 1.0
        if self.settings["diff"] == "Easy": self.base_speed = 4
        elif self.settings["diff"] == "Hard": self.base_speed = 8
        else: self.base_speed = 6
        
        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.enemies = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        
        self.active_powerup = None
        self.powerup_timer = 0

    def draw_text(self, text, font, color, x, y, center=True):
        img = font.render(text, True, color)
        rect = img.get_rect()
        if center: rect.center = (x, y)
        else: rect.topleft = (x, y)
        DISPLAYSURF.blit(img, rect)

    def menu_screen(self):
        DISPLAYSURF.fill(WHITE)
        self.draw_text("EXTREME RACING", FONT_BIG, BLACK, SCREEN_WIDTH//2, 100)
        
        buttons = [("PLAY", 250), ("SETTINGS", 320), ("LEADERBOARD", 390), ("QUIT", 460)]
        mx, my = pygame.mouse.get_pos()
        
        for text, y in buttons:
            color = RED if pygame.Rect(SCREEN_WIDTH//2-100, y-25, 200, 50).collidepoint(mx, my) else BLACK
            self.draw_text(text, FONT_MEDIUM, color, SCREEN_WIDTH//2, y)

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 225 < my < 275: self.state = "NAME_INPUT"
                if 295 < my < 345: self.state = "SETTINGS"
                if 365 < my < 415: self.state = "LEADERBOARD"
                if 435 < my < 485: pygame.quit(); sys.exit()

    def name_input_screen(self):
        DISPLAYSURF.fill(WHITE)
        self.draw_text("ENTER YOUR NAME:", FONT_MEDIUM, BLACK, SCREEN_WIDTH//2, 200)
        self.draw_text(self.username, FONT_MEDIUM, BLUE, SCREEN_WIDTH//2, 300)
        self.draw_text("Press ENTER to Start", FONT_SMALL, GRAY, SCREEN_WIDTH//2, 400)

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN: 
                    self.reset_game_stats()
                    self.state = "GAME"
                elif event.key == K_BACKSPACE: self.username = self.username[:-1]
                else: 
                    if len(self.username) < 10: self.username += event.unicode

    def settings_screen(self):
        DISPLAYSURF.fill(WHITE)
        self.draw_text("SETTINGS", FONT_BIG, BLACK, SCREEN_WIDTH//2, 80)
        
        self.draw_text(f"Sound: {'ON' if self.settings['sound'] else 'OFF'}", FONT_SMALL, BLACK, SCREEN_WIDTH//2, 200)
        self.draw_text(f"Color: {self.settings['color']}", FONT_SMALL, BLACK, SCREEN_WIDTH//2, 250)
        self.draw_text(f"Difficulty: {self.settings['diff']}", FONT_SMALL, BLACK, SCREEN_WIDTH//2, 300)
        self.draw_text("BACK", FONT_MEDIUM, RED, SCREEN_WIDTH//2, 500)

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 190 < my < 220: self.settings['sound'] = not self.settings['sound']
                if 240 < my < 270: self.settings['color'] = "RED" if self.settings['color']=="BLUE" else "BLUE"
                if 290 < my < 320:
                    diffs = ["Easy", "Medium", "Hard"]
                    self.settings['diff'] = diffs[(diffs.index(self.settings['diff'])+1)%3]
                if 480 < my < 530:
                    save_json(SETTINGS_FILE, self.settings)
                    self.state = "MENU"

    def game_loop(self):
        DISPLAYSURF.fill(WHITE)
        
        if random.random() < 0.02 * self.speed_multiplier:
            new_enemy = Enemy(self.base_speed * self.speed_multiplier)
            self.enemies.add(new_enemy)
            self.all_sprites.add(new_enemy)
            
        if random.random() < 0.01:
            kind = random.choice(['nitro', 'shield', 'repair'])
            p = PowerUp(kind)
            self.powerups.add(p)
            self.all_sprites.add(p)

        if random.random() < 0.01:
            c = Coin()
            self.coins.add(c)
            self.all_sprites.add(c)

        self.distance += 0.1 * self.speed_multiplier
        self.speed_multiplier += 0.0001
        
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
        else:
            self.player.nitro_active = False
            self.active_powerup = None

        self.all_sprites.update()
        
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            if self.player.shield:
                self.player.shield = False
                self.active_powerup = None
                for e in pygame.sprite.spritecollide(self.player, self.enemies, True): pass
            else:
                self.game_over()

        coin_hits = pygame.sprite.spritecollide(self.player, self.coins, True)
        for hit in coin_hits:
            self.score += 10
            self.coins_collected += 1

        pw_hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        for pw in pw_hits:
            self.active_powerup = pw.kind
            self.powerup_timer = 300
            if pw.kind == 'nitro': self.player.nitro_active = True
            if pw.kind == 'shield': self.player.shield = True
            if pw.kind == 'repair': self.score += 50

        self.all_sprites.draw(DISPLAYSURF)
        self.draw_text(f"Score: {int(self.score + self.distance)}", FONT_SMALL, BLACK, 10, 10, False)
        self.draw_text(f"Dist: {int(self.distance)}m", FONT_SMALL, BLACK, 10, 40, False)
        
        if self.active_powerup:
            self.draw_text(f"BUFF: {self.active_powerup.upper()} ({self.powerup_timer//60}s)", FONT_SMALL, GREEN, 10, 70, False)

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()

    def game_over(self):
        final_score = int(self.score + self.distance)
        self.leaderboard.append({"name": self.username, "score": final_score})
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x['score'], reverse=True)[:10]
        save_json(LEADERBOARD_FILE, self.leaderboard)
        self.state = "GAMEOVER"

    def game_over_screen(self):
        DISPLAYSURF.fill(BLACK)
        self.draw_text("GAME OVER", FONT_BIG, RED, SCREEN_WIDTH//2, 150)
        self.draw_text(f"Final Score: {int(self.score + self.distance)}", FONT_MEDIUM, WHITE, SCREEN_WIDTH//2, 250)
        self.draw_text("Press M for Menu or R to Retry", FONT_SMALL, GRAY, SCREEN_WIDTH//2, 400)
        
        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_m: self.state = "MENU"
                if event.key == K_r: 
                    self.reset_game_stats()
                    self.state = "GAME"

    def leaderboard_screen(self):
        DISPLAYSURF.fill(WHITE)
        self.draw_text("TOP 10", FONT_MEDIUM, BLACK, SCREEN_WIDTH//2, 50)
        for i, entry in enumerate(self.leaderboard):
            self.draw_text(f"{i+1}. {entry['name']} - {entry['score']}", FONT_SMALL, BLACK, SCREEN_WIDTH//2, 120 + i*35)
        
        self.draw_text("BACK", FONT_MEDIUM, RED, SCREEN_WIDTH//2, 530)
        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 510 < my < 560: self.state = "MENU"

    def run(self):
        while True:
            if self.state == "MENU": self.menu_screen()
            elif self.state == "NAME_INPUT": self.name_input_screen()
            elif self.state == "SETTINGS": self.settings_screen()
            elif self.state == "GAME": self.game_loop()
            elif self.state == "GAMEOVER": self.game_over_screen()
            elif self.state == "LEADERBOARD": self.leaderboard_screen()
            
            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()