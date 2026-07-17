from __future__ import annotations

import requests

from astraquant.config.telegram_config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)

from .alert import Alert


class TelegramAlert:

    @staticmethod
    def send(alert: Alert):

        message = (
            "🚀 ASTRAQUANT DIDRS\n\n"
            f"🟢 {alert.signal}\n\n"
            f"Index        : {alert.symbol}\n"
            f"Option      : {alert.option}\n"
            f"Discount  : {alert.discount:.2f}\n"
            f"Time         : {alert.timestamp.strftime('%d-%b-%Y %H:%M:%S')}"
        )

        url = (
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        )

        response = requests.post(
            url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
            },
            timeout=10,
        )

        response.raise_for_status()