from __future__ import annotations


class OptionPricing:
    """
    Basic option pricing utilities.
    """

    @staticmethod
    def intrinsic_value(
        spot: float,
        strike: float,
        option_type: str,
    ) -> float:

        option_type = option_type.upper()

        if option_type == "CE":
            return max(0.0, spot - strike)

        if option_type == "PE":
            return max(0.0, strike - spot)

        raise ValueError("Invalid option type")

    @staticmethod
    def discount(
        spot: float,
        strike: float,
        option_price: float,
        option_type: str,
    ) -> float:

        intrinsic = OptionPricing.intrinsic_value(
            spot,
            strike,
            option_type,
        )

        return intrinsic - option_price