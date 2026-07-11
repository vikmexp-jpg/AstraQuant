from enum import Enum


class MarketSession(Enum):

    PRE_OPEN = "PRE_OPEN"

    MARKET = "MARKET"

    POST_MARKET = "POST_MARKET"

    CLOSED = "CLOSED"