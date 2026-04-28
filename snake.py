import pygame
import random
import json
import psycopg2
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Ultimate FINAL")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
DARK_RED = (139,0,0)

FONT = pygame.font.SysFont("Arial", 22)

# ---------- DB ----------
conn = psycopg2.connect(
    host="localhost",
    database="snake_game",
    user="postgres",
    password="human1or6",
    port="5432"
)
cur = conn.cursor()

def get_player(username):
    cur.execute("SELECT id FROM players WHERE username=%s",(username,))
    r = cur.fetchone()
    if r: return r[0]
    cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id",(username,))
    conn.commit()
    return cur.fetchone()[0]

def save_score(username,score,level):
    pid = get_player(username)
    cur.execute("INSERT INTO game_sessions(player_id,score,level_reached) VALUES(%s,%s,%s)",
                (pid,score,level))
    conn.commit()

def get_top():
    cur.execute("""
    SELECT username,score,level_reached,played_at
    FROM game_sessions JOIN players ON players.id=player_id
    ORDER BY score DESC LIMIT 10
    """)
    return cur.fetchall()

def best_score(username):
    cur.execute("""
    SELECT MAX(score) FROM game_sessions
    JOIN players ON players.id=player_id
    WHERE username=%s
    """,(username,))
    r=cur.fetchone()[0]
    return r if r else 0

# ---------- SETTINGS ----------
def load_settings():
    try:
        return json.load(open("settings.json"))
    except:
        return {"color":[0,255,0],"grid":False,"sound":False}

def save_settings(s):
    json.dump(s,open("settings.json","w"))

settings = load_settings()

# ---------- UTILS ----------
def text(msg,x,y,color=WHITE):
    screen.blit(FONT.render(msg,True,color),(x,y))

def random_cell(exclude):
    while True:
        pos = (random.randrange(0,WIDTH,CELL),random.randrange(0,HEIGHT,CELL))
        if pos not in exclude:
            return pos

# ---------- GAME ----------
def game(username):
    snake=[(100,100)]
    dx,dy=CELL,0
    length=1

    obstacles=[]
    food = random_cell(snake)
    poison=None
    power=None

    power_active=None
    power_start=0
    spawn_time=0

    shield=False

    score=0
    level=1
    base_speed=10
    speed=base_speed

    best = best_score(username)

    def spawn_obstacles():
        nonlocal obstacles
        for _ in range(level):
            while True:
                p = random_cell(snake+obstacles)
                # не рядом с головой
                hx,hy = snake[-1]
                if abs(p[0]-hx)>20 and abs(p[1]-hy)>20:
                    obstacles.append(p)
                    break

    run=True
    while run:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_LEFT and dx==0: dx,dy=-CELL,0
                if e.key==pygame.K_RIGHT and dx==0: dx,dy=CELL,0
                if e.key==pygame.K_UP and dy==0: dx,dy=0,-CELL
                if e.key==pygame.K_DOWN and dy==0: dx,dy=0,CELL

        x,y=snake[-1]
        x+=dx; y+=dy

        collision = (
            x<0 or x>=WIDTH or y<0 or y>=HEIGHT or
            (x,y) in snake or (x,y) in obstacles
        )

        if collision:
            if shield:
                shield=False
            else:
                save_score(username,score,level)
                game_over(username,score,level,best)
                return

        snake.append((x,y))
        if len(snake)>length:
            snake.pop(0)

        # FOOD
        if (x,y)==food:
            length+=1
            score+=1
            food=random_cell(snake+obstacles)

            if score%5==0:
                level+=1
                base_speed+=1
                spawn_obstacles()

        # POISON
        if not poison and random.random()<0.02:
            poison=random_cell(snake+obstacles+[food])

        if poison and (x,y)==poison:
            length-=2
            poison=None
            if length<=1:
                save_score(username,score,level)
                game_over(username,score,level,best)
                return

        # POWER SPAWN
        if not power and pygame.time.get_ticks()-spawn_time>2000:
            if random.random()<0.02:
                power={
                    "type":random.choice(["speed","slow","shield"]),
                    "pos":random_cell(snake+obstacles+[food])
                }
                spawn_time=pygame.time.get_ticks()

        # POWER DESPAWN
        if power and pygame.time.get_ticks()-spawn_time>8000:
            power=None

        # TAKE POWER
        if power and (x,y)==power["pos"]:
            power_active=power["type"]
            power_start=pygame.time.get_ticks()
            if power_active=="shield":
                shield=True
            power=None

        # POWER EFFECT
        speed=base_speed
        if power_active:
            elapsed = pygame.time.get_ticks()-power_start

            if power_active=="speed":
                speed=base_speed+5
            elif power_active=="slow":
                speed=max(5,base_speed-5)

            if power_active!="shield" and elapsed>5000:
                power_active=None

        # DRAW
        screen.fill(BLACK)

        if settings["grid"]:
            for i in range(0,WIDTH,CELL):
                pygame.draw.line(screen,(40,40,40),(i,0),(i,HEIGHT))
            for j in range(0,HEIGHT,CELL):
                pygame.draw.line(screen,(40,40,40),(0,j),(WIDTH,j))

        for s in snake:
            pygame.draw.rect(screen,settings["color"],(*s,CELL,CELL))

        pygame.draw.rect(screen,RED,(*food,CELL,CELL))

        if poison:
            pygame.draw.rect(screen,DARK_RED,(*poison,CELL,CELL))

        if power:
            col = BLUE if power["type"]=="shield" else YELLOW
            pygame.draw.rect(screen,col,(*power["pos"],CELL,CELL))

        for o in obstacles:
            pygame.draw.rect(screen,BLUE,(*o,CELL,CELL))

        text(f"Score: {score}",10,10)
        text(f"Level: {level}",10,30)
        text(f"Best: {best}",10,50)

        pygame.display.update()
        clock.tick(speed)

# ---------- GAME OVER ----------
def game_over(username,score,level,best):
    while True:
        screen.fill(BLACK)
        text("GAME OVER",220,80)
        text(f"Score: {score}",220,130)
        text(f"Level: {level}",220,160)
        text(f"Best: {best}",220,190)
        text("R - Retry",220,240)
        text("M - Menu",220,270)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_r:
                    game(username)
                if e.key==pygame.K_m:
                    return

# ---------- LEADERBOARD ----------
def leaderboard():
    data=get_top()
    while True:
        screen.fill(BLACK)
        text("TOP 10",250,40)

        y=80
        for i,row in enumerate(data):
            date = row[3].strftime("%Y-%m-%d")
            text(f"{i+1}. {row[0]} {row[1]} L{row[2]} {date}",40,y)
            y+=25

        text("ESC - Back",200,350)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:
                return

# ---------- SETTINGS ----------
def settings_screen():
    while True:
        screen.fill(BLACK)
        text("SETTINGS",230,50)
        text(f"G - Grid: {settings['grid']}",150,150)
        text(f"C - Color",150,180)
        text(f"S - Sound: {settings['sound']}",150,210)
        text("ESC - Save & Back",150,260)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_ESCAPE:
                    save_settings(settings)
                    return
                if e.key==pygame.K_g:
                    settings["grid"]=not settings["grid"]
                if e.key==pygame.K_s:
                    settings["sound"]=not settings["sound"]
                if e.key==pygame.K_c:
                    settings["color"]=[random.randint(0,255) for _ in range(3)]

# ---------- MENU ----------
def menu():
    username=""
    while True:
        screen.fill(BLACK)
        text("SNAKE ULTIMATE",180,50)
        text("Enter Name: "+username,150,120)
        text("ENTER - Play",200,170)
        text("L - Leaderboard",200,200)
        text("S - Settings",200,230)
        text("Q - Quit",200,260)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN and username:
                    game(username)
                elif e.key==pygame.K_l:
                    leaderboard()
                elif e.key==pygame.K_s:
                    settings_screen()
                elif e.key==pygame.K_q:
                    pygame.quit(); sys.exit()
                elif e.key==pygame.K_BACKSPACE:
                    username=username[:-1]
                else:
                    if len(username)<10:
                        username+=e.unicode

# ---------- START ----------
menu()