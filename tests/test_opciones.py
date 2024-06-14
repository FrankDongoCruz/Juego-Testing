import pytest
from opciones import *

def test_adjust_volume():
    initial_volume = 0.5
    adjust_volume(0.8)
    assert volume == 0.8
    adjust_volume(initial_volume)
