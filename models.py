from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Flavor:
    id: Optional[int] = None
    name: str = ''
    description: str = ''
    is_seasonal: bool = False
    price: float = 0.0

@dataclass
class Ingredient:
    id: Optional[int] = None
    name: str = ''
    quantity: int = 0
    unit: str = ''

@dataclass
class Allergen:
    id: Optional[int] = None
    name: str = ''

@dataclass
class Cart:
    items: List[Flavor] = field(default_factory=list)
    total_price: float = 0.0

    def add_item(self, flavor: Flavor):
        self.items.append(flavor)
        self.total_price += flavor.price

    def remove_item(self, flavor: Flavor):
        if flavor in self.items:
            self.items.remove(flavor)
            self.total_price -= flavor.price

    def clear(self):
        self.items.clear()
        self.total_price = 0.0