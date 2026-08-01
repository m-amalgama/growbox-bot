def ven(box_temp,target,max_speed):
    base = 45
    K = 10
    error = target - box_temp
    speed = max(min((base + error * K), max_speed), 0)
    return int(speed)