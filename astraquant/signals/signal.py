from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Signal:

    action: str
    reason: str