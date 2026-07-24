from __future__ import annotations

import logging
import requests

from astraquant.alerts.alert import Alert
from astraquant.config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)

logger = logging.getLogger("AstraQuant")

class TelegramAlert:

    @staticmethod
    def send(alert: Alert) -> None:

        opportunity = alert.opportunity
        state = opportunity.state

        #
        # Header
        #
        headers = {
            "NEW": "🟢 NEW OPPORTUNITY",
            "IMPROVING": "🔥 OPPORTUNITY IMPROVING",
            "WEAKENING": "🟡 OPPORTUNITY WEAKENING",
            "RECOVERED": "✅ OPPORTUNITY CLOSED",
            "STABLE": "ℹ️ OPPORTUNITY STABLE",
        }

        header = headers.get(
            state.name,
            "ℹ️ OPPORTUNITY UPDATE",
        )

        #
        # Opportunity Duration
        #
        duration = (
            opportunity.last_updated
            - opportunity.started_at
        ).total_seconds() / 60

        #
        # Telegram Message
        #
        message_body = (
            "🚀 <b>Discount Strategy</b>\n\n"

            f"{header}\n\n"

            f"🆔 <b>Opportunity</b> : {opportunity.id}\n"
            f"📈 <b>Index</b>         : {alert.symbol}\n"
            f"📌 <b>Option</b>       : {opportunity.option}\n\n"

            f"💰 <b>Current</b>      : {opportunity.current_discount:.2f}\n"
            f"🚀 <b>Peak</b>          : {opportunity.max_discount:.2f}\n"
            f"🏁 <b>Start</b>          : {opportunity.start_discount:.2f}\n\n"

            f"⏱️ <b>Duration</b>     : {duration:.1f} min\n"
            f"🕒 <b>Updated</b>     : "
            f"{opportunity.last_updated.strftime('%H:%M:%S')}"
        )

        url = (
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        )

        try:

            response = requests.post(
                url,
                json={
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message_body,
                    "parse_mode": "HTML",
                },
                timeout=10,
            )

            response.raise_for_status()

            logger.info(
                "[%s] Telegram %s delivered",
                alert.symbol,
                state.value,
            )

        except Exception:

            logger.exception(
                "[%s] Telegram notification failed",
                alert.symbol,
            )