import logging

from astraquant.tracker.opportunity_state import OpportunityState

from .alert import Alert
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
        f"discount={alert.top_discount[0].discount:.2f}",
        f"status={status}",
    ]
    if extra:
        parts.append(extra)
    logger.info("alert | " + " | ".join(parts))


class AlertEngine:

    @staticmethod
    def notify(alert: Alert):

        state = alert.opportunity.state

        #
        # Ignore unchanged opportunities
        #
        if state in (
            OpportunityState.STABLE,
            OpportunityState.WEAKENING,
        ):
            return

        #
        # New Opportunity
        #
        if state == OpportunityState.NEW:

            ConsoleAlert.send(alert)

            SoundAlert.buy()

            WindowsAlert.send(alert)

            TelegramAlert.send(alert)

            logger.info(
                "[%s] NEW Opportunity (%.2f)",
                alert.symbol,
                alert.current_discount,
            )

        #
        # Opportunity Improved
        #
        elif state == OpportunityState.IMPROVING:

            ConsoleAlert.send(alert)

            WindowsAlert.send(alert)

            TelegramAlert.send(alert)

            logger.info(
                "[%s] Opportunity Improved Current=%.2f Peak=%.2f",
                alert.symbol,
                alert.opportunity.current_discount,
                alert.opportunity.max_discount,
            )

        #
        # Opportunity Recovered
        #
        elif state == OpportunityState.RECOVERED:

            ConsoleAlert.send(alert)

            TelegramAlert.send(alert)

            logger.info(
                "[%s] Opportunity Recovered",
                alert.symbol,
            )