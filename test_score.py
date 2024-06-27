# test_score_increment.py
import pytest
from unittest.mock import patch
import game

def test_score_increment():
    game.score = 0  # Reiniciar el puntaje antes del test

    # Ejecutar game_loop para simular incremento de score
    game.game_loop('easy', 1)

    assert game.score > 0, "No se incrementó el score durante game_loop"

if __name__ == "__main__":
    pytest.main()
