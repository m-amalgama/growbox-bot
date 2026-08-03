from core.control import calc_fan_speed

def test_returns_base_at_target():      # 27, 27, 60  → 45
    assert calc_fan_speed(27, 27, 60) == 45
def test_below_target_lowers_speed():   # 25, 27, 40  → 25
    assert calc_fan_speed(25, 27, 40) == 25
def test_above_target_raises_speed():   # 30, 27, 80  → 75
    assert calc_fan_speed(30, 27, 80) == 75 
def test_clamped_to_max_speed():        # 40, 25, 100 → 100
    assert calc_fan_speed(40, 25, 100) == 100
def test_never_goes_below_zero():       # 0, 25, 60   → 0
    assert calc_fan_speed(0, 25, 60) == 0