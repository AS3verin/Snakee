import pytest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import playtime

@pytest.fixture
def timeplay():
    return playtime.TimePlay()

def test_timeplay_initialization(timeplay):
    assert timeplay.t0 >= 0
    assert timeplay.t >= 0
    assert timeplay.t >= timeplay.t0


def test_timeconverter_initialization():
    tc = playtime.TimeConverter(5000)
    assert tc.milliseconds == 5000

def test_timeconverter_to_seconds():
    tc = playtime.TimeConverter(5000)
    assert tc.to_seconds() == 5

def test_timeconverter_to_minutes():
    tc = playtime.TimeConverter(36349)
    assert tc.to_minutes_seconds() == "0:36.35"

def test_timeconverter_to_hours():
    tc = playtime.TimeConverter(3665000)
    assert tc.to_hours_minutes_seconds() == "1:1:5.00"

if __name__ == "__main__": 
    pytest.main()
