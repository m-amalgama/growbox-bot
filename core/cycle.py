import asyncio
from hardware.fake_sensor import read
from core.control import calc_fan_speed
from core import status, targets
from hardware.fan import set_speed

async def run(bot):
    while True:
        reading = read()
        temp = reading["temp"]
        fan_speed = calc_fan_speed(temp, **targets.setpoint)
        status.current["temp"] = temp
        status.current["fan"] = fan_speed
        set_speed(fan_speed)
        await asyncio.sleep(5)