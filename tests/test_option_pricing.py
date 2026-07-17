
from astraquant.pricing.intrinsic import OptionPricing


def test_ce_intrinsic():

    assert (
        OptionPricing.intrinsic_value(
            24120,
            24000,
            "CE",
        )
        == 120
    )


def test_pe_intrinsic():

    assert (
        OptionPricing.intrinsic_value(
            23900,
            24000,
            "PE",
        )
        == 100
    )


def test_discount():

    discount = OptionPricing.discount(
        spot=24120,
        strike=24000,
        option_price=95,
        option_type="CE",
    )

    assert discount == 25