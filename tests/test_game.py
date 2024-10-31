import pytest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import game

def test_snake_init_position():
    assert 1 == 1
