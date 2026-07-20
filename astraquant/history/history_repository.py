class HistoryRepository:

    def __init__(self):

        self._history = []

    def add(self, summary):

        self._history.append(summary)

    @property
    def history(self):

        return self._history