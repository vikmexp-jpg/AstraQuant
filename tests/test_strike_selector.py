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
    


def test_atm_round_down():
    assert StrikeSelector.atm_strike(24002) == 24000


def test_atm_round_up():
    assert StrikeSelector.atm_strike(24026) == 24050


def test_deep_itm_offset():
    assert (
        StrikeSelector.strike(
            24026,
            -500,
        )
        == 23550
    )


def test_otm_offset():
    assert (
        StrikeSelector.strike(
            24026,
            500,
        )
        == 24550
    )


def test_custom_interval():
    assert (
        StrikeSelector.strike(
            24112,
            -200,
            interval=100,
        )
        == 23900
    )