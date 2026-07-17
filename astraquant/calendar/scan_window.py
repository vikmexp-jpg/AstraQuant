from datetime import datetime

class ScanWindow:

    def __init__(
        self,
        start: datetime,
        end: datetime,
    ):
        self.start = start
        self.end = end