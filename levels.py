import pygame
import os
from opciones import get_screen_dimensions

def load_block_textures():
    block_textures = []
    bloques_dir = os.path.join(os.path.dirname(__file__), 'bloques')
    for i in range(1, 8):
        filename = f'bloque{i}.png'
        filepath = os.path.join(bloques_dir, filename)
        block_texture = pygame.image.load(filepath).convert_alpha()
        block_texture_resized = pygame.transform.scale(block_texture, (100, 45))
        block_textures.append(block_texture_resized)
    return block_textures

def load_level(level):
    bricks = []
    block_textures = load_block_textures()
    screen_width, screen_height = get_screen_dimensions()
    
    if level == "test":
        num_rows = 1
        num_cols = 1
        brick_width = 100
        brick_height = 45
        level_width = num_cols * brick_width
        level_height = num_rows * brick_height

        start_x = (screen_width - level_width) // 2
        start_y = 50
        
        for i in range(num_rows):
            for j in range(num_cols):
                brick_rect = pygame.Rect(start_x + j * brick_width, 
                                         start_y + i * brick_height, brick_width, brick_height)
                bricks.append((brick_rect, block_textures[(i * num_cols + j) % len(block_textures)]))
                
    if level == 1:
        num_rows = 6
        num_cols = 12
        brick_width = 100
        brick_height = 45
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
        num_rows = 7
        num_cols = 11
        brick_width = 100
        brick_height = 45
        level_width = num_cols * brick_width
        level_height = num_rows * brick_height

        start_x = (screen_width - level_width) // 2
        start_y = 40
        
        for i in range(num_rows):
            for j in range(num_cols - i):
                brick_rect = pygame.Rect(start_x + j * brick_width + i * (brick_width // 2), 
                                         start_y + i * brick_height, 
                                         brick_width, 
                                         brick_height)
                bricks.append((brick_rect, block_textures[(i * num_cols + j) % len(block_textures)]))

    return bricks
