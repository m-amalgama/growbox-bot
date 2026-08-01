from Mock import mock_1

def test_mock_key_in_dict():
    d = mock_1()
    assert "temp" in d            
def test_len_dict():
    d = mock_1()
    assert len(d) == 3           
def test_type_temp():
    d = mock_1()
    assert isinstance(d["temp"], float)  
def test_temp_in_sensor_range():
    d = mock_1()
    assert 25 <= d["temp"] <= 34 