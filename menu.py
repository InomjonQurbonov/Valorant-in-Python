import pygame
import sys
import webbrowser
import os

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 50)

# Кнопки
buttons = [
    {"text": "Играть", "color": BLUE, "hover_color": GRAY, "action": "play", "size": (200, 60)},
    {"text": "Настройки", "color": GREEN, "hover_color": GRAY, "action": "settings", "size": (200, 60)},
    {"text": "Выход", "color": RED, "hover_color": GRAY, "action": "quit", "size": (200, 60)},
    {"text": "Программер", "color": YELLOW, "hover_color": GRAY, "action": "github", "size": (240, 70)}
]

# Позиции кнопок
button_margin = 20
start_y = 100  # Начало расположения кнопок
start_x = 50   # Расстояние от левого края экрана

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

# Загрузка и настройка фоновой музыки
pygame.mixer.music.load("game_files/music/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)
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
                    if action == "play":
                        print("Запуск игры...")
                        running = False
                    elif action == "settings":
                        print("Открытие настроек...")
                        pygame.quit()
                        os.system("python settings.py")
                        sys.exit()
                    elif action == "quit":
                        running = False
                    elif action == "github":
                        webbrowser.open("https://github.com/InomjonQurbonov")  # Открываем GitHub

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
