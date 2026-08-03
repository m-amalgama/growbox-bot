import pytest
from hardware.fake_sensor import read

@pytest.fixture
def d():
    return read()

def test_mock_key_in_dict(d):
    assert "temp" in d            
def test_returns_three_keys(d):
    assert len(d) == 3           
def test_type_temp(d):
    assert isinstance(d["temp"], float)  
def test_temp_in_sensor_range(d):
    assert 25 <= d["temp"] <= 34 