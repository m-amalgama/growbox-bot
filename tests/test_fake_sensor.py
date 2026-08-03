import pytest
from hardware.fake_sensor import read

@pytest.fixture
def reading():
    return read()

def test_has_temp_key(reading):
    assert "temp" in reading            
def test_returns_three_keys(reading):
    assert len(reading) == 3           
def test_temp_is_float(reading):
    assert isinstance(reading["temp"], float)  
def test_temp_in_sensor_range(reading):
    assert 25 <= reading["temp"] <= 34 