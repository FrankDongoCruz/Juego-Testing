import pytest
import pygame
from game import game_loop

def test_game_loop(monkeypatch):
    monkeypatch.setattr('pygame.event.get', lambda: [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_w})])
    assert game_loop('easy', 1) == 'next_level'
