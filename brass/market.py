from __future__ import annotations
from enum import Enum
from abc import ABC, abstractmethod


class Market(ABC):
    def __init__(self, max_resource:int) -> None:
        self.max_resource = max_resource
        self.current_resource = max_resource

    @abstractmethod
    def calculate_cost(self) -> int:
        raise NotImplementedError
    
    def buy(self) -> int:
        if self.current_resource > 0:
            self.current_resource -= 1

        return self.calculate_cost()
    
    def sell(self) -> int:
        if self.current_resource >= self.max_resource:
            raise ValueError("Cannot sell resource")
        
        self.current_resource += 1
        return self.calculate_cost()

class CoalMarket(Market):
    def __init__(self) -> None:
        super().__init__(max_resource=13)

    def calculate_cost(self) -> int:
        if self.current_resource == 0:
            return 8
        
        return (self.max_resource - self.current_resource + 1) // 2 + 1
        
    
class IronMarket(Market):
    def __init__(self) -> None:
        super().__init__(max_resource=8)

    def calculate_cost(self):
        if self.current_resource == 0:
            return 6
        
        return (self.max_resource - self.current_resource) // 2 + 2
