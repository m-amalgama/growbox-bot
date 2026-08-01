from Ven_fun import ven

def test_returns_base_at_target():      # 27, 27, 60  → 45
    assert ven(27, 27, 60) == 45
def test_below_target_lowers_speed():   # 25, 27, 40  → 25
    assert ven(25, 27, 40) == 25
def test_above_target_raises_speed():   # 30, 27, 80  → 75
    assert ven(30, 27, 80) == 75 
def test_clamped_to_max_speed():        # 40, 25, 100 → 100
    assert ven(40, 25, 100) == 100
def test_never_goes_below_zero():       # 0, 25, 60   → 0
    assert ven(0, 25, 60) == 0