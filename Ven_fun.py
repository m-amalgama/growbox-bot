def ven(box_temp,target,max_speed):
    base = 45
    K = 10
    error = box_temp - target
    speed = max(min((base + error * K), max_speed), 0)
    return int(speed)