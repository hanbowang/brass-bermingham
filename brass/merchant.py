from __future__ import annotations
from enum import Enum

from brass.common import Industry

class Merchant:
    def __init__(self, industries:set[Industry]) -> None:
        self.industries = industries
        self.beer = False