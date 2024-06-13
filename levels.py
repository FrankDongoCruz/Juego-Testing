import pygame
import os
from opciones import get_screen_dimensions

# Función para cargar las texturas de los bloques
def load_block_textures():
    block_textures = []
    bloques_dir = os.path.join(os.path.dirname(__file__), 'bloques')
    for i in range(1, 8):
        filename = f'bloque{i}.png'
        filepath = os.path.join(bloques_dir, filename)
        block_texture = pygame.image.load(filepath).convert_alpha()
        # Ajustar tamaño de la textura según sea necesario
        block_texture_resized = pygame.transform.scale(block_texture, (65, 25))  # Ajustar tamaño según necesites
        block_textures.append(block_texture_resized)
    return block_textures

def load_level(level):
    bricks = []
    block_textures = load_block_textures()  # Cargar texturas de bloques
    screen_width, screen_height = get_screen_dimensions()  # Obtener dimensiones de la pantalla

    if level == 1:
        num_rows = 3
        num_cols = 5
        brick_width = 65
        brick_height = 25
        level_width = num_cols * brick_width
        level_height = num_rows * brick_height

        start_x = (screen_width - level_width) // 2
        start_y = 50
        
        for i in range(num_rows):
            for j in range(num_cols):
                brick_rect = pygame.Rect(start_x + j * brick_width, 
                                         start_y + i * brick_height, brick_width, brick_height)
                bricks.append((brick_rect, block_textures[(i * num_cols + j) % len(block_textures)]))
                
    elif level == 2:
        num_rows = 4
        num_cols = 5
        brick_width = 65
        brick_height = 25
        level_width = num_cols * brick_width
        level_height = num_rows * brick_height

        start_x = (screen_width - level_width) // 2
        start_y = 40
        
        for i in range(num_rows):
            for j in range(num_cols):
                brick_rect = pygame.Rect(start_x + j * brick_width, 
                                         start_y + i * brick_height, brick_width, brick_height)
                bricks.append((brick_rect, block_textures[(i * num_cols + j) % len(block_textures)]))

    return bricks
