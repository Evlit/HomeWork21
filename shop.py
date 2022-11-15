# Класс магазин
from typing import Dict

from abstract import Storage
from exeption import ToManyProductError, NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class Shop(Storage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title, quantity):
        if self.get_unique_items_count() >= 5:
            raise ToManyProductError

        if self.get_free_space() < quantity:
            raise NotEnoughSpaceError

        if title in self._items:
            self._items[title] += quantity
        else:
            self._items[title] = quantity

    def remove(self, title, quantity):
        if title not in self._items:
            raise UnknownProductError

        if self._items[title] < quantity:
            raise NotEnoughProductError

        self._items[title] -= quantity
        if self._items[title] == 0:
            self._items.pop(title)

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        str_itms = ''
        for item in self._items:
            str_itms += f"{self._items[item]} {item}\n"
        return str_itms

    def get_unique_items_count(self):
        return len(self._items)
