import math
import random
import numpy as np
import matplotlib.pyplot as plt


def fun(temp,temp_target, max_ven=80):
    base = 45
    K = 10
    error = temp - temp_target
    speed = max(min((base + error * K), max_ven), 0)
    return round(speed, 1)

def mock_1():
    temp = round(random.uniform(25, 34), 2)
    humi = round(random.uniform(40, 55), 2)
    svp = 0.61078 * math.exp((17.27 * temp) / (temp + 237.3))
    avp = svp * (humi / 100.0)
    vpd = svp - avp
    return {"temp": temp, "humi": humi, "vpd": vpd}

def mock_n():
    v_list = []
    count = 0
    base_temp = 15.0
    base_humi = 40.2
    while count < 100:
        dict_t_h_v = {}
        temp = base_temp + (count * 0.1)
        humi = min(base_humi + (count * 0.1), 100)
        svp = 0.61078 * math.exp((17.27 * temp) / (temp + 237.3))
        avp = svp * (humi / 100.0)
        vpd = svp - avp
        dict_t_h_v["temp"] = round(temp, 2)
        dict_t_h_v["humi"] = round(humi, 2)
        dict_t_h_v["vpd"] = round(vpd, 3)
        v_list.append(dict_t_h_v)
        count += 1
    return v_list

mock = mock_n()
temps = [t["temp"] for t in mock]
speeds = [fun(t) for t in temps]
plt.plot(temps, speeds)
plt.xlabel("temp")
plt.ylabel("speed %")
plt.show()
print(temps)
print(speeds)


