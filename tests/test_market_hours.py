from datetime import datetime

from astraquant.calendar.market_hours import MarketHours


def test_market_open_includes_open_time():
    now = datetime(2026, 7, 20, 9, 15)

    assert MarketHours.is_market_open(now)


def test_market_open_excludes_close_time():
    now = datetime(2026, 7, 20, 15, 30)

    assert not MarketHours.is_market_open(now)


def test_market_open_returns_false_on_saturday():
    now = datetime(2026, 7, 18, 10, 0)

    assert not MarketHours.is_market_open(now)


def test_market_open_returns_false_on_sunday():
    now = datetime(2026, 7, 19, 10, 0)

    assert not MarketHours.is_market_open(now)


def test_next_market_open_before_open_same_day():
    now = datetime(2026, 7, 20, 8, 45)

    assert MarketHours.next_market_open(now) == datetime(2026, 7, 20, 9, 15)


def test_next_market_open_after_close_skips_weekend():
    now = datetime(2026, 7, 17, 15, 45)

    assert MarketHours.next_market_open(now) == datetime(2026, 7, 20, 9, 15)
