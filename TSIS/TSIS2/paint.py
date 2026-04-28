import pygame
import sys
import datetime
import math

def flood_fill(surface, start_x, start_y, fill_color):
    target_color = surface.get_at((start_x, start_y))
    if target_color == fill_color: return
    width, height = surface.get_size()
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()
        if surface.get_at((x, y)) != target_color: continue
        surface.set_at((x, y), fill_color)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                stack.append((nx, ny))

def draw_shape(surf, tool, start_pos, end_pos, color, thickness):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx, dy = x2 - x1, y2 - y1
    
    if tool == 'line':
        pygame.draw.line(surf, color, start_pos, end_pos, thickness)
    elif tool == 'rect':
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(dx), abs(dy))
        pygame.draw.rect(surf, color, rect, thickness)
    elif tool == 'square':
        side = max(abs(dx), abs(dy))
        rect = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
        pygame.draw.rect(surf, color, rect, thickness)
    elif tool == 'circle':
        radius = int(math.hypot(dx, dy))
        pygame.draw.circle(surf, color, (x1, y1), radius, thickness)
    elif tool == 'right_tri':
        pygame.draw.polygon(surf, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif tool == 'eq_tri':
        side = int(math.hypot(dx, dy))
        h = int(side * math.sqrt(3) / 2)
        pygame.draw.polygon(surf, color, [(x1, y1 - h//2), (x1 - side//2, y1 + h//2), (x1 + side//2, y1 + h//2)], thickness)
    elif tool == 'rhombus':
        pygame.draw.polygon(surf, color, [(x1, y1 - dy), (x1 + dx, y1), (x1, y1 + dy), (x1 - dx, y1)], thickness)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 560))
    pygame.display.set_caption("Full Paint: Shapes, Text, Line")
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((640, 480))
    canvas_color = (0, 0, 0)
    canvas.fill(canvas_color)
    
    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    mode, thickness, tool = 'blue', 5, 'pencil'
    drawing, erasing, last_pos, start_pos = False, False, None, None
    
    # Текст
    font_main = pygame.font.SysFont(None, 24)
    font_text = pygame.font.SysFont(None, 36)
    text_active = False
    text_input = ""
    text_pos = (0, 0)

    while True:
        curr_color = canvas_color if erasing else colors[mode]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if text_active:
                    if event.key == pygame.K_RETURN:
                        txt_surf = font_text.render(text_input, True, curr_color)
                        canvas.blit(txt_surf, text_pos)
                        text_active = False
                    elif event.key == pygame.K_ESCAPE: text_active = False
                    elif event.key == pygame.K_BACKSPACE: text_input = text_input[:-1]
                    else: text_input += event.unicode
                    continue

                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                elif event.key == pygame.K_1: thickness = 2
                elif event.key == pygame.K_2: thickness = 5
                elif event.key == pygame.K_3: thickness = 10
                elif event.key == pygame.K_p: tool = 'pencil'
                elif event.key == pygame.K_l: tool = 'line'
                elif event.key == pygame.K_f: tool = 'fill'
                elif event.key == pygame.K_t: tool = 'text'
                elif event.key >= pygame.K_4 and event.key <= pygame.K_9:
                    tool = ['rect', 'square', 'circle', 'right_tri', 'eq_tri', 'rhombus'][event.key - pygame.K_4]
                elif event.key == pygame.K_c: canvas.fill(canvas_color)
                elif event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    pygame.image.save(canvas, f"save_{datetime.datetime.now().strftime('%H%M%S')}.png")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] < 480:
                    if event.button == 1: drawing = True
                    if event.button == 3: erasing = True
                    start_pos = event.pos
                    if tool == 'fill': flood_fill(canvas, *event.pos, curr_color)
                    if tool == 'text':
                        text_active = True
                        text_input = ""
                        text_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if (drawing or erasing) and tool not in ['pencil', 'fill', 'text'] and start_pos:
                    draw_shape(canvas, tool, start_pos, event.pos, curr_color, thickness)
                drawing = erasing = False
                last_pos = None

            if event.type == pygame.MOUSEMOTION and (drawing or erasing):
                if tool == 'pencil' and event.pos[1] < 480:
                    if last_pos: pygame.draw.line(canvas, curr_color, last_pos, event.pos, thickness)
                    last_pos = event.pos

        screen.fill((50, 50, 50))
        screen.blit(canvas, (0, 0))
        
        # Предпросмотр фигур и линий
        if (drawing or erasing) and tool not in ['pencil', 'fill', 'text'] and start_pos:
            draw_shape(screen, tool, start_pos, pygame.mouse.get_pos(), curr_color, thickness)
        
        # Предпросмотр текста
        if text_active:
            txt_preview = font_text.render(text_input + "|", True, colors[mode])
            screen.blit(txt_preview, text_pos)
            
        status = f"Tool: {tool.upper()} | Size: {thickness} | Colors: R,G,B | Save: Ctrl+S"
        screen.blit(font_main.render(status, True, (255, 255, 255)), (10, 500))
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()