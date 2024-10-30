import pytest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import playtime

### Timeplay ###
@pytest.fixture
def timeplay():
    return playtime.TimePlay()

def test_timeplay_initialization(timeplay):
    assert timeplay.t0 >= 0
    assert timeplay.t >= 0
    assert timeplay.t >= timeplay.t0

def test_timeplay_get_time_to_display(timeplay):
    assert timeplay.Get_Time_To_Display(0) == "00.00"
    assert timeplay.Get_Time_To_Display(64340) == "01:04.34"


def test_timeplay_get_top():
    tp = playtime.TimePlay()
    assert tp.get_TOP() >= 0

### Time Converter ###
def test_timeconverter_initialization():
    tc = playtime.TimeConverter(5000)
    assert tc.milliseconds == 5000

def test_timeconverter_to_seconds():
    tc = playtime.TimeConverter(5000)
    assert tc.to_seconds() == 5

def test_timeconverter_to_str_seconds():
    tc = playtime.TimeConverter(5000)
    assert tc.to_str_seconds() == "05.00"

def test_timeconverter_to_minutes():
    tc = playtime.TimeConverter(636349)
    assert tc.to_minutes_seconds() == "10:36.35"

def test_timeconverter_to_hours():
    tc = playtime.TimeConverter(3665000)
    assert tc.to_hours_minutes_seconds() == "01:01:05.00"

testdata = [ 
    (360000000,"100:00:00.00"),
    (3600000,"01:00:00.00"),
    (12345678,"03:25:45.68"),
    (765432,"12:45.43"),
    (54321, "54.32"),
]
@pytest.mark.parametrize("time_ms, expected", testdata)
def test_timeconverter_to_str_timer(time_ms, expected):
    tc = playtime.TimeConverter(time_ms)
    assert tc.to_str_timer() == expected

if __name__ == "__main__": 
    pytest.main()
