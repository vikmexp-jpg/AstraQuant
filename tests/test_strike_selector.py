from astraquant.pricing.strike_selector import StrikeSelector


def test_call():

    strike = StrikeSelector.deep_itm_call(
        24072,
        500,
    )

    assert strike == 23550


def test_put():

    strike = StrikeSelector.deep_itm_put(
        24072,
        500,
    )

    assert strike == 24550