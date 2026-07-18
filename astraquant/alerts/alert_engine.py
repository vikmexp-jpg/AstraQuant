import logging

from .alert import Alert
from .alert_state import AlertState
from .console_alert import ConsoleAlert
from .windows_alert import WindowsAlert
from .sound_alert import SoundAlert
from .telegram_alert import TelegramAlert

logger = logging.getLogger("AstraQuant")


def _log_alert_event(event: str, alert: Alert, status: str, extra: str | None = None):
    parts = [
        f"event={event}",
        f"symbol={alert.symbol}",
        f"signal={alert.signal}",
        f"option={alert.option}",
        f"discount={alert.discount:.2f}",
        f"status={status}",
    ]
    if extra:
        parts.append(extra)
    logger.info("alert | " + " | ".join(parts))


class AlertEngine:

    @staticmethod
    def notify(alert: Alert):
        if alert.signal not in {"BUY", "SELL"}:
            logger.info(
                "alert | event=ignored | symbol=%s | signal=%s | option=%s | discount=%.2f | status=skipped",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
            )
            return

        previous = AlertState.last_action.get(alert.symbol)

        if previous == alert.signal:
            logger.debug(
                "alert | event=duplicate | symbol=%s | signal=%s | option=%s | discount=%.2f | status=skipped",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
            )
            return

        _log_alert_event(
            event="dispatch",
            alert=alert,
            status="processing",
        )
        ConsoleAlert.send(alert)

        if alert.signal == "BUY":
            logger.info("Playing buy sound for %s", alert.symbol)
            SoundAlert.buy()

        WindowsAlert.send(alert)
        TelegramAlert.send(alert)

        AlertState.last_action[alert.symbol] = alert.signal
        _log_alert_event(
            event="delivery",
            alert=alert,
            status="delivered",
        )