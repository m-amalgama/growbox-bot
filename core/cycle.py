import asyncio
from hardware.fake_sensor import mock_1
from core.control import ven
from core.targets import default
from hardware.fan import set_speed
from core.status import status_dict

async def loop(bot):
    while True:
        mock_data = mock_1()
        temp = mock_data["temp"]
        ven_speed = ven(temp, **default)
        status_dict["temp"] = temp
        status_dict["ven"] = ven_speed
        set_speed(ven_speed)
        await asyncio.sleep(5)