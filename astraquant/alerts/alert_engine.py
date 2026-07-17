from .alert import Alert
from .alert_state import AlertState
from .console_alert import ConsoleAlert
from .windows_alert import WindowsAlert
from astraquant.alerts import alert
from .sound_alert import SoundAlert


class AlertEngine:

    @staticmethod
    def notify(alert: Alert):

        previous = AlertState.last_action.get(
            alert.symbol
        )

        if previous == alert.signal:
            return

        ConsoleAlert.send(alert)
        if alert.signal == "BUY":
            SoundAlert.buy()
        WindowsAlert.send(alert)

        AlertState.last_action[
            alert.symbol
        ] = alert.signal