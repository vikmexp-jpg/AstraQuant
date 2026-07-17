from __future__ import annotations

from win10toast import ToastNotifier

from .alert import Alert


class WindowsAlert:

    _toaster = ToastNotifier()

    @staticmethod
    def send(alert: Alert):

        title = f"{alert.signal} - {alert.symbol}"

        message = (
            f"{alert.option}\n"
            f"Time: {alert.timestamp}\n"
            f"Discount : {alert.discount:.2f}"
        )

        WindowsAlert._toaster.show_toast(
            title,
            message,
            duration=60,
            threaded=True,
        )