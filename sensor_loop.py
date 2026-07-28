import asyncio
from Mock import mock_1
from Default import default
from Ven_fun import ven
from Mock_fan import faan

async def loop(bot):
    while True:
        mock_data = mock_1()
        temp = mock_data["temp"]
        ven_speed = ven(temp, **default)
        faan(ven_speed)
        await asyncio.sleep(5)