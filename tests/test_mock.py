import pytest
from hardware.fake_sensor import mock_1

@pytest.fixture
def d():
    return mock_1()

def test_mock_key_in_dict(d):
    assert "temp" in d            
def test_len_dict(d):
    assert len(d) == 3           
def test_type_temp(d):
    assert isinstance(d["temp"], float)  
def test_temp_in_sensor_range(d):
    assert 25 <= d["temp"] <= 34 