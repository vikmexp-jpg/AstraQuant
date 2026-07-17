from __future__ import annotations

from .signal import Signal


class DidrsSignal:

    @staticmethod
    def generate(
        current_discount: float,
        threshold: float,
    ) -> Signal:

        if current_discount >= threshold:

            return Signal(
                action="BUY",
                reason="Discount above threshold",
            )

        return Signal(
            action="WAIT",
            reason="Discount below threshold",
        )