def ven(temp,target, max_speed):
    base = 45
    K = 10
    error = temp - target
    speed = max(min((base + error * K), max_speed), 0)
    return round(speed, 1)