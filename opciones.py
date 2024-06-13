import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rompe Bloques')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FONT = pygame.font.Font(None, 74)
SMALL_FONT = pygame.font.Font(None, 36)

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
PADDLE_IMAGE = pygame.transform.scale(pygame.image.load('paddle.png'), (120, 15))
BALL_IMAGE = pygame.transform.scale(pygame.image.load('ball.png'), (25, 25))
WIN_SCREEN_IMAGE = pygame.transform.scale(pygame.image.load('winscreen.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_OVER_IMAGE = pygame.transform.scale(pygame.image.load('perdiste.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

PADDLE_SPEED = 10
BALL_SPEED = {'easy': 3, 'normal': 5, 'hard': 7}
volume = 0.5

pygame.mixer.init()
SOUND_BOUNCE = pygame.mixer.Sound('bounce.wav')
SOUND_BREAK = pygame.mixer.Sound('break.wav')
SOUND_MENU_MOVE = pygame.mixer.Sound('menu_move.wav')
BACKGROUND_MUSIC = 'background_music.mp3'
pygame.mixer.music.load(BACKGROUND_MUSIC)

def get_screen_dimensions():
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_images():
    return BACKGROUND_IMAGE, PADDLE_IMAGE, BALL_IMAGE, WIN_SCREEN_IMAGE, GAME_OVER_IMAGE

def play_sound(sound, volume=1.0):
    sound.set_volume(volume)
    sound.play()
