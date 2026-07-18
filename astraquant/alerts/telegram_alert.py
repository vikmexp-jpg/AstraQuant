from __future__ import annotations

import logging

import requests

from astraquant.config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)
from astraquant.config.index_config import INDEX_CONFIG

from .alert import Alert

logger = logging.getLogger("AstraQuant")


class TelegramAlert:

    @staticmethod
    def send(alert: Alert):
        threshold = INDEX_CONFIG.get(alert.symbol, {}).get("discount_threshold", 10.0)

        if alert.signal != "BUY" or alert.discount <= threshold:
            logger.info(
                "alert | event=telegram_ignored | symbol=%s | signal=%s | option=%s | discount=%.2f | threshold=%.2f | status=skipped",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
                threshold,
            )
            return

        signal_label = "💥 STRONG BUY"

        message_body = (
            "🚀 ASTRAQUANT DIDRS\n\n"
            f"{signal_label}\n\n"
            f"Index        :  {alert.symbol}\n"
            f"Option      :  {alert.option}\n"
            f"Discount  :{alert.discount:>8.2f}\n"
            f"Time         :  {alert.timestamp.strftime('%d-%b-%y %H:%M:%S')}"
        )

        message = f"<pre>{message_body}</pre>"
        url = (
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        )
        logger.info(
            "alert | event=telegram_dispatch | symbol=%s | signal=%s | option=%s | discount=%.2f | status=sending",
            alert.symbol,
            alert.signal,
            alert.option,
            alert.discount,
        )
        try:
            response = requests.post(
                url,
                json={
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "HTML",
                },
                timeout=10,
            )

            response.raise_for_status()
            logger.info(
                "alert | event=telegram_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=delivered",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
            )
        except Exception as e:
            logger.error(
                "alert | event=telegram_delivery | symbol=%s | signal=%s | option=%s | discount=%.2f | status=failed | error=%s",
                alert.symbol,
                alert.signal,
                alert.option,
                alert.discount,
                e,
                exc_info=True,
            )