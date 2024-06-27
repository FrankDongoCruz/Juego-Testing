# test_game.py
import pytest
from unittest.mock import patch

# Asumimos que el archivo se llama game.py
import game

@pytest.fixture
def mock_pygame(mocker):
    mocker.patch('game.pygame.mixer.Sound')
    return mocker

def test_game_win_sound(mock_pygame):
    with patch('game.play_win_sound') as mock_play_win_sound:
        game.game_win()
        mock_play_win_sound.assert_called_once()

def test_game_lose_sound(mock_pygame):
    with patch('game.play_lose_sound') as mock_play_lose_sound:
        game.game_over()
        mock_play_lose_sound.assert_called_once()
