from __future__ import annotations

import logging

from win10toast import ToastNotifier

from .alert import Alert

logger = logging.getLogger("AstraQuant")


class WindowsAlert:
    _toaster = ToastNotifier()

    @staticmethod
    def send(alert: Alert) -> None:
        title = f"{alert.option}"
        message = (
            f"Top Discount            Time\n"
            f"-----------------------------------\n"
            f"{alert.top_discount[0].discount:>0.2f} ---> "
            f"{alert.top_discount[0].timestamp.strftime('%d-%b-%y %H:%M:%S')}\n"
            f"{alert.top_discount[1].discount:>0.2f} ---> "
            f"{alert.top_discount[1].timestamp.strftime('%d-%b-%y %H:%M:%S')}\n"
        )

        logger.debug(
            "alert | event=windows_dispatch | symbol=%s | signal=%s | option=%s | discount=%.2f | status=sending",
            alert.symbol,
            alert.signal,
            alert.option,
            alert.top_discount[0].discount,
        )

        try:
            WindowsAlert._toaster.show_toast(
                title,
                message,
                duration=5,
                threaded=True,
            )
        except Exception as exc:
            logger.error(
                "alert | event=windows_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=failed | error=%s",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.top_discount[0].discount,
                exc,
                exc_info=True,
            )
            return

        logger.debug(
            "alert | event=windows_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=delivered",
            alert.symbol,
            alert.signal,
            alert.option,
            alert.top_discount[0].discount,
        )