from abc import ABC, abstractmethod
from astraquant.core.models.strategy_context import StrategyContext
from astraquant.core.models.strategy_result import StrategyResult

class Strategy(ABC):
    @abstractmethod
    def execute(self, context: StrategyContext) -> StrategyResult:
        ...
