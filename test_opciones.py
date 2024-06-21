import pygame
import pytest
from opciones import adjust_volume, volume, load_sound, SOUND_BOUNCE, SOUND_BREAK, SOUND_MENU_MOVE, MUSIC_PATH

pygame.init()

bounce_sound = load_sound(SOUND_BOUNCE)
break_sound = load_sound(SOUND_BREAK)
menu_move_sound = load_sound(SOUND_MENU_MOVE)
pygame.mixer.music.load(MUSIC_PATH)

@pytest.fixture(scope="module", autouse=True)
def pygame_setup():
    pygame.display.set_mode((800, 600))

    yield

    pygame.quit()

def test_adjust_volume():
    adjust_volume(0.8)
    assert volume == 0.8
    assert pygame.mixer.music.get_volume() == 0.8
    assert bounce_sound.get_volume() == 0.8
    assert break_sound.get_volume() == 0.8
    assert menu_move_sound.get_volume() == 0.8

    adjust_volume(0.5)
    assert volume == 0.5
    assert pygame.mixer.music.get_volume() == 0.5
    assert bounce_sound.get_volume() == 0.5
    assert break_sound.get_volume() == 0.5
    assert menu_move_sound.get_volume() == 0.5

    adjust_volume(1.0)
    assert volume == 1.0
    assert pygame.mixer.music.get_volume() == 1.0
    assert bounce_sound.get_volume() == 1.0
    assert break_sound.get_volume() == 1.0
    assert menu_move_sound.get_volume() == 1.0

    adjust_volume(0.0)
    assert volume == 0.0
    assert pygame.mixer.music.get_volume() == 0.0
    assert bounce_sound.get_volume() == 0.0
    assert break_sound.get_volume() == 0.0
    assert menu_move_sound.get_volume() == 0.0

if __name__ == "__main__":
    pytest.main()
