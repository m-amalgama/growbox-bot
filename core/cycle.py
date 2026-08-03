import asyncio
from hardware.fake_sensor import read
from core.control import calc_fan_speed
from core.targets import setpoint
from hardware.fan import set_speed
from core.status import current

async def run(bot):
    while True:
        mock_data = read()
        temp = mock_data["temp"]
        fan_speed = calc_fan_speed(temp, **setpoint)
        current["temp"] = temp
        current["fan"] = fan_speed
        set_speed(fan_speed)
        await asyncio.sleep(5)