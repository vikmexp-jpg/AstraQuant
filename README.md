# AstraQuant

AstraQuant is a modular quantitative trading framework for monitoring option discount opportunities (DIDRS), generating trading signals, and delivering real-time alerts. The framework is designed to be extensible, allowing future integration with live trading, backtesting, and portfolio management.

---

## Current Version

**v1.0.0-alpha**

---

## Current Status

### ✅ Implemented

- DIDRS Discount Scanner
- Multi-Index Monitoring
  - NIFTY
  - SENSEX
- Dynamic Expiry Cycle Management
- Deep ITM Strike Selection
- Real-time Live Monitor
- Alert Engine
- Console Alerts
- Windows Sound Alerts
- Telegram Notifications
- Scan Result Model
- Configurable Index Support
- Structured Project Layout

### 🚧 In Progress

- Logging Framework
- Paper Trading Engine
- Strategy Analytics
- Dashboard
- Live Order Execution

---

## Features

- Multi-index DIDRS scanning
- Real-time option discount calculation
- Deep ITM strike selection
- Configurable expiry handling
- Telegram alert integration
- Windows sound notifications
- Console monitoring
- Modular architecture
- Broker-independent design
- Easy configuration using `.env`

---

## Project Structure

```text
AstraQuant/
│
├── astraquant/
│   ├── alerts/
│   ├── broker/
│   ├── calendar/
│   ├── config/
│   ├── logger/
│   ├── pricing/
│   ├── scanners/
│   ├── strategy/
│   └── ...
│
├── assets/
│   └── sounds/
│
├── logs/
├── reports/
├── sample_data/
├── scripts/
├── tests/
│
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AstraQuant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install as an editable package:

```bash
pip install -e .
```

---

## Configuration

Create a `.env` file from `.env.example`.

Example:

```text
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

UPSTOX_API_KEY=
UPSTOX_API_SECRET=
UPSTOX_ACCESS_TOKEN=
```

---

## Running the Live Monitor

```bash
python scripts/live_monitor.py
```

---

## Available Scripts

| Script | Description |
|---------|-------------|
| `scripts/live_monitor.py` | Starts live market monitoring |
| `scripts/run_scanner.py` | Runs the DIDRS scanner |
| `scripts/demo_history.py` | Historical scanner example |

---

## Alert Channels

Currently supported:

- Console Alerts
- Windows Sound Alerts
- Telegram Notifications

---

## Logging

Application logs are stored in:

```text
logs/YYYY-MM-DD.log
```

---

## Roadmap

- [x] DIDRS Scanner
- [x] Telegram Alerts
- [x] Live Monitoring
- [ ] Logging Framework
- [ ] Paper Trading
- [ ] Trade Journal
- [ ] Strategy Analytics
- [ ] Dashboard
- [ ] Live Order Execution

---

## License

This project is licensed under the MIT License.