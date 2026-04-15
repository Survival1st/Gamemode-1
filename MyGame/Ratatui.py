import pygame
import datetime
import sys

# --- Настройки ---
WIDTH, HEIGHT = 800, 800
FPS = 60 # Обновляем экран 60 раз в секунду для плавности приложения

def main():
    # 1. Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock = pygame.time.Clock()

    # 2. Загрузка изображений
    # Конвертация (convert_alpha) ускоряет отрисовку PNG с прозрачным фоном
    try:
        # 'assets/' указывает программе, что нужно заглянуть в эту папку
        bg_image = pygame.image.load("assets/mickey_clock.png").convert_alpha()
        left_hand_img = pygame.image.load("assets/left_hand.png").convert_alpha()   # Секунды
        right_hand_img = pygame.image.load("assets/right_hand.png").convert_alpha() # Минуты
    except FileNotFoundError as e:
        print(f"Ошибка: Не удалось найти файлы в папке assets. Проверь названия!")
        sys.exit()

    # Находим центр фона (центр циферблата)
    bg_rect = bg_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 3. Синхронизация с системным временем
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute

        # 4. Вычисление углов (отрицательные значения для вращения по часовой стрелке)
        sec_angle = -(second * 6)
        min_angle = -(minute * 6)

        # 5. Поворот и центрирование левой руки (Секунды)
        rotated_left_hand = pygame.transform.rotate(left_hand_img, sec_angle)
        left_hand_rect = rotated_left_hand.get_rect(center=bg_rect.center)

        # 6. Поворот и центрирование правой руки (Минуты)
        rotated_right_hand = pygame.transform.rotate(right_hand_img, min_angle)
        right_hand_rect = rotated_right_hand.get_rect(center=bg_rect.center)

        # 7. Отрисовка (Blitting)
        screen.fill((255, 255, 255)) # Заливаем фон белым цветом (на случай если картинка фона не на весь экран)
        
        # Порядок важен: сначала фон, затем минутная стрелка (обычно она ниже), затем секундная
        screen.blit(bg_image, bg_rect)
        screen.blit(rotated_right_hand, right_hand_rect)
        screen.blit(rotated_left_hand, left_hand_rect)

        # 8. Обновление экрана
        pygame.display.flip()
        
        # Ограничиваем частоту кадров. Хоть время меняется раз в секунду, 
        # цикл программы должен крутиться быстрее, чтобы окно не зависало и реагировало на закрытие
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()