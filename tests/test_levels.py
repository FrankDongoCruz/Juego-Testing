import pygame
import pytest
from unittest.mock import MagicMock
from levels import load_block_textures, load_level

@pytest.fixture(autouse=True)
def mock_get_screen_dimensions():
    with pytest.MonkeyPatch.context() as m:
        m.setattr("opciones.get_screen_dimensions", lambda: (800, 600))
        yield

def test_load_block_textures():
    block_textures = load_block_textures()
    assert len(block_textures) == 7
    for texture in block_textures:
        assert isinstance(texture, pygame.Surface)

@pytest.mark.parametrize("level, expected_num_bricks", [
    (1, 72),  
    (2, 43),  
])
def test_load_level(level, expected_num_bricks):
    bricks = load_level(level)
    assert len(bricks) == expected_num_bricks
    for brick_rect, block_texture in bricks:
        assert isinstance(brick_rect, pygame.Rect)
        assert isinstance(block_texture, pygame.Surface)
        assert brick_rect.width == 100
        assert brick_rect.height == 45

def test_load_level_invalid_level():
    with pytest.raises(ValueError):
        load_level(3)

def test_load_level_level2_brick_positions():
    bricks = load_level(2)
    for brick_rect, _ in bricks:
        assert brick_rect.left >= 0
        assert brick_rect.right <= 800
        assert brick_rect.top >= 0
        assert brick_rect.bottom <= 600
