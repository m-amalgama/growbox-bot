def calc_fan_speed(box_temp,target,max_speed):
    BASE_SPEED = 45
    GAIN = 10
    error = box_temp - target
    speed = max(min((BASE_SPEED + error * GAIN), max_speed), 0)
    return int(speed)