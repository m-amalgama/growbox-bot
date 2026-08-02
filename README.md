# Growbox Climate Bot

Telegram bot for proportional fan control in a Spider Farmer grow tent.

**Problem.** The stock GGS controller and the vendor app only support on/off switching around a dead zone — the fan is either at a fixed speed or off. Temperature oscillates instead of holding.

**Solution.** Fan speed is calculated from the deviation between box temperature and target, so it rises smoothly as the box heats up.

## Stack

- Python 3.14
- aiogram 3.30 — Telegram Bot API, async
- pytest 9.1 — 9 tests

## How it works

| File | Role |
|---|---|
| `main.py` | Entry point. Builds the bot, runs polling and the sensor loop together. |
| `Bot_proto.py` | Router and handlers: inline menu, FSM config dialog, status on request. |
| `config.py` | Settings from `.env` via pydantic-settings. |
| `sensor_loop.py` | Background loop: reads the sensor, calls the control logic, writes the result. |
| `Ven_fun.py` | Control logic. Proportional speed with min/max clamping. |
| `Default.py` | Default settings: target temperature and max fan speed. |
| `Status.py` | Latest readings. The loop writes, the handler reads. |
| `Mock.py` | Sensor stub — returns temperature, humidity, VPD. |
| `Mock_fan.py` | Fan stub — receives a speed and reports it. |
| `test_ven.py` | Tests for the control logic. |
| `test_mock.py` | Tests for the sensor stub. |

## Run

```bash
git clone https://github.com/m-amalgama/growbox-bot.git
cd growbox-bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
TOKEN=your_token_from_botfather
```

Start it:

```bash
python main.py
```

## Tests

```bash
pytest
```

- `test_ven.py` — control logic: target, minimum, maximum and clamping.
- `test_mock.py` — sensor contract: keys, number of fields, value type, value range.

## Status

Runs against a mock sensor. A BLE bridge to a real thermometer (Govee H5075) is the next step; the control logic and the message flow are already in place.
