from astraquant.utils import StrikeSelector


def test_atm():

    assert StrikeSelector.atm_strike(24162) == 24150
    assert StrikeSelector.atm_strike(24176) == 24200


def test_offset():

    assert (
        StrikeSelector.strike(
            24162,
            -500,
        )
        == 23650
    )

    assert (
        StrikeSelector.strike(
            24162,
            500,
        )
        == 24650
    )