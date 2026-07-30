import asyncio
from Mock import mock_1
from Default import default
from Ven_fun import ven
from Mock_fan import faan
from Status import status_dict

async def loop(bot):
    while True:
        mock_data = mock_1()
        temp = mock_data["temp"]
        ven_speed = ven(temp, **default)
        status_dict["temp"] = temp
        status_dict["ven"] = ven_speed
        faan(ven_speed)
        await asyncio.sleep(5)