import math
import random

def read():
    temp = round(random.uniform(25, 34), 2)
    humi = round(random.uniform(40, 55), 2)
    svp = 0.61078 * math.exp((17.27 * temp) / (temp + 237.3))
    avp = svp * (humi / 100.0)
    vpd = svp - avp
    return {"temp": temp, "humi": humi, "vpd": vpd}