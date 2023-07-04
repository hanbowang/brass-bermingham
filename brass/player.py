from __future__ import annotations
from enum import Enum

class Player:
    def __init__(self, name:str) -> None:
        self.name = name
        self.tiles = None
        self.money = 17
        self.remaining_link_tiles = 14
        self._vp = 0
        self._income = 10
    
    def get_income_level(self) -> int:
        if self._income < 10:
            return -(10 - self._income)

        if self._income == 10:
            return 0
        
        if self._income > 10 and self._income <= 30:
            return (self._income - 11) // 2 + 1
        
        if self._income > 30 and self._income <= 60:
            return (self._income - 31) // 3 + 11
        
        if self._income > 60:
            return (self._income - 61) // 4 + 21

    def adjust_income(self, amount:int) -> None:
        if self._income + amount < 0:
            self._income = 0
        elif self._income + amount > 99:
            self._income = 99
        else:
            self._income += amount
    
    def adjust_vp(self, amount:int) -> None:
        if self._vp + amount < 0:
            self._vp = 0
        else:
            self._vp += amount 