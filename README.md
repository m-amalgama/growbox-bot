# Growbox Climate Bot

Telegram bot for proportional fan control in a Spider Farmer grow tent.

**Problem.** The stock GGS controller and the vendor app only support on/off switching around a dead zone — the fan is either at a fixed speed or off. Temperature oscillates instead of holding.

**Solution.** Fan speed is calculated from the deviation between box temperature and target, so it rises smoothly as the box heats up.

## Stack

- Python 3.14
- aiogram 3.30 — Telegram Bot API, async
- pydantic-settings 2.14 — config from `.env`
- pytest 9.1 — 9 tests

## Layout

```
.
├── main.py              entry point
├── config.py            settings
├── bot/
│   └── handlers.py      router, keyboards, FSM dialog
├── core/
│   ├── control.py       control logic
│   ├── cycle.py         background loop
│   ├── targets.py       target temperature and speed limit
│   └── status.py        latest readings
├── hardware/
│   ├── fake_sensor.py   sensor stub
│   └── fan.py           fan stub
└── tests/
    ├── test_control.py
    └── test_fake_sensor.py
```

Packages are split by layer: `bot` talks to Telegram, `core` holds the logic, `hardware` is the only place that touches devices. Swapping the stub for a real BLE thermometer means replacing one module in `hardware`.

| File | Role |
|---|---|
| `main.py` | Builds the bot, runs polling and the sensor loop together via `asyncio.gather`. |
| `config.py` | Reads the token from `.env`. |
| `bot/handlers.py` | Router and handlers: inline menu, FSM dialog for the target, status on request. |
| `core/control.py` | `calc_fan_speed()` — proportional speed with clamping. |
| `core/cycle.py` | Background loop: read sensor → compute speed → write status → set fan. |
| `core/targets.py` | Setpoint: target temperature and max fan speed. Written by handlers. |
| `core/status.py` | Latest readings. The loop writes, the status handler reads. |
| `hardware/fake_sensor.py` | Sensor stub — returns temperature, humidity, VPD. |
| `hardware/fan.py` | Fan stub — receives a speed and reports it. |
| `tests/__init__.py` | Keeps pytest's basedir at the project root, so `core.*` and `hardware.*` imports resolve. |

## Control logic

```
speed = BASE_SPEED + (box_temp - target) * GAIN
```

clamped to `0 .. max_speed`. At the target the fan holds `BASE_SPEED`; every degree above it adds `GAIN` percent. No PID — the box has a slow thermal response and a proportional term is enough.

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

- `test_control.py` — control logic: at target, below, above, upper clamp, lower clamp.
- `test_fake_sensor.py` — sensor contract: key present, number of fields, value type, value range.

## Status

Runs against a mock sensor. A BLE bridge to a real thermometer (Govee H5075) is the next step; the control logic and the message flow are already in place.