import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Настройки")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font("game_files/game_font/Evalter.ttf", 50)

# Кнопки
buttons = [
    {"text": "Увеличить громкость", "color": BLUE, "hover_color": GRAY, "action": "increase_volume", "size": (400, 60)},
    {"text": "Уменьшить громкость", "color": BLUE, "hover_color": GRAY, "action": "decrease_volume", "size": (400, 60)},
    {"text": "Остановить музыку", "color": BLUE, "hover_color": GRAY, "action": "stop_music", "size": (400, 60)},
    {"text": "Вернуться в меню", "color": BLUE, "hover_color": GRAY, "action": "return_to_menu", "size": (400, 60)}
]

# Позиции кнопок
button_margin = 20
start_y = 150  # Начало расположения кнопок

# Загрузка фоновых изображений
background_images = [
    pygame.image.load("game_files/background_images/bg_image1.jpg"),
    pygame.image.load("game_files/background_images/bg_image2.jpg"),
    pygame.image.load("game_files/background_images/bg_image3.jpg"),
    pygame.image.load("game_files/background_images/bg_image4.jpg")
]

# Масштабирование изображений под размер экрана
background_images = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in background_images]

# Переменные для переключения фона
current_bg_index = 0
bg_switch_time = 5000  # Время переключения в миллисекундах (5 секунд)
last_switch_time = pygame.time.get_ticks()

# Переменная для громкости
volume = 0.5

# Загрузка и настройка фоновой музыки
pygame.mixer.music.load("game_files/music/menu_music.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)  # -1 означает зацикливание

# Функция отрисовки кнопок
def draw_buttons():
    for index, button in enumerate(buttons):
        button_width, button_height = button["size"]
        x = start_x
        y = start_y + index * (button_height + button_margin)
        mouse_pos = pygame.mouse.get_pos()

        # Проверка, находится ли мышка на кнопке
        if x <= mouse_pos[0] <= x + button_width and y <= mouse_pos[1] <= y + button_height:
            color = button["hover_color"]
        else:
            color = button["color"]

        # Рисуем кнопку с закругленными краями
        pygame.draw.rect(screen, color, (x, y, button_width, button_height), border_radius=15)
        text = font.render(button["text"], True, BLACK)
        text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))
        screen.blit(text, text_rect)

# Основной цикл
running = True
while running:
    # Получение текущего времени
    current_time = pygame.time.get_ticks()

    # Смена фона каждые 5 секунд
    if current_time - last_switch_time > bg_switch_time:
        current_bg_index = (current_bg_index + 1) % len(background_images)
        last_switch_time = current_time

    # Отображение текущего фонового изображения
    screen.blit(background_images[current_bg_index], (0, 0))

    # Отрисовка кнопок
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for index, button in enumerate(buttons):
                button_width, button_height = button["size"]
                x = start_x
                y = start_y + index * (button_height + button_margin)
                if x <= mouse_pos[0] <= x + button_width and y <= mouse_pos[1] <= y + button_height:
                    action = button["action"]
                    if action == "increase_volume":
                        volume = min(1.0, volume + 0.1)
                        pygame.mixer.music.set_volume(volume)
                        print(f"Громкость увеличена: {volume}")
                    elif action == "decrease_volume":
                        volume = max(0.0, volume - 0.1)
                        pygame.mixer.music.set_volume(volume)
                        print(f"Громкость уменьшена: {volume}")
                    elif action == "stop_music":
                        pygame.mixer.music.stop()
                        print("Музыка остановлена.")
                    elif action == "back_to_menu":
                        print("Возвращение в меню...")
                        pygame.quit()
                        os.system("python menu.py")
                        sys.exit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
