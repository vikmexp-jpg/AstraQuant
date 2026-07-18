from __future__ import annotations

import logging

from win10toast import ToastNotifier

from .alert import Alert

logger = logging.getLogger("AstraQuant")


class WindowsAlert:
    _toaster = ToastNotifier()

    @staticmethod
    def send(alert: Alert) -> None:
        title = f"{alert.signal} - {alert.symbol}"
        message = (
            f"{alert.option}\n"
            f"Time: {alert.timestamp}\n"
            f"Discount : {alert.discount:.2f}"
        )

        logger.info(
            "alert | event=windows_dispatch | symbol=%s | signal=%s | option=%s | discount=%.2f | status=sending",
            alert.symbol,
            alert.signal,
            alert.option,
            alert.discount,
        )

        try:
            WindowsAlert._toaster.show_toast(
                title,
                message,
                duration=60,
                threaded=True,
            )
        except Exception as exc:
            logger.error(
                "alert | event=windows_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=failed | error=%s",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
                exc,
                exc_info=True,
            )
            return

        logger.info(
            "alert | event=windows_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=delivered",
            alert.symbol,
            alert.signal,
            alert.option,
            alert.discount,
        )