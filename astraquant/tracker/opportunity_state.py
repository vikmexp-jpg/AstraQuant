from enum import Enum


class OpportunityState(Enum):

    NEW = "NEW"

    IMPROVING = "IMPROVING"

    STABLE = "STABLE"

    WEAKENING = "WEAKENING"

    RECOVERED = "RECOVERED"