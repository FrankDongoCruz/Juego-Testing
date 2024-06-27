import pygame
import os

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rompe Bloques')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FONT = pygame.font.Font(None, 100)
SMALL_FONT = pygame.font.Font(None, 36)

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
BALL_IMAGE = pygame.transform.scale(pygame.image.load('ball.png'), (30, 30))
WIN_SCREEN_IMAGE = pygame.transform.scale(pygame.image.load('winscreen.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_OVER_IMAGE = pygame.transform.scale(pygame.image.load('perdiste.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

PADDLE_SIZE = {
    'easy': (250, 20),
    'normal': (120, 20),
    'hard': (100, 20)
}
current_difficulty = 'normal'
PADDLE_IMAGE = pygame.transform.scale(pygame.image.load('paddle.png'), PADDLE_SIZE[current_difficulty])

PADDLE_IMAGE = pygame.transform.scale(pygame.image.load('paddle.png'), (150, 20))

PADDLE_SPEED = 20
BALL_SPEED = {'easy': 7, 'normal': 10, 'hard': 15}

SOUND_PATH = 'sonido/'
SOUND_BOUNCE = os.path.join(SOUND_PATH, 'bounce.wav')
SOUND_BREAK = os.path.join(SOUND_PATH, 'break.wav')
SOUND_MENU_MOVE = os.path.join(SOUND_PATH, 'menu_move.wav')
MUSIC_PATH = os.path.join(SOUND_PATH, 'background_music.mp3')

volume = 0.5

def load_sound(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.set_volume(volume)
    return sound

bounce_sound = load_sound(SOUND_BOUNCE)
break_sound = load_sound(SOUND_BREAK)
menu_move_sound = load_sound(SOUND_MENU_MOVE)

def play_sound(sound):
    sound.play()

def set_sound_volume(sound, volume):
    sound.set_volume(volume)

pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

def adjust_volume(new_volume):
    global volume
    volume = new_volume
    pygame.mixer.music.set_volume(volume)
    bounce_sound.set_volume(volume)
    break_sound.set_volume(volume)
    menu_move_sound.set_volume(volume)

def get_screen_dimensions():
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_images():
    return BACKGROUND_IMAGE, PADDLE_IMAGE, BALL_IMAGE, WIN_SCREEN_IMAGE, GAME_OVER_IMAGE
    
def set_difficulty(difficulty):
    global current_difficulty, PADDLE_IMAGE
    current_difficulty = difficulty
    PADDLE_IMAGE = pygame.transform.scale(pygame.image.load('paddle.png'), PADDLE_SIZE[current_difficulty])