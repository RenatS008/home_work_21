from typing import Dict

from classes.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        self.__items[name] -= amount
        if self.__items == 0:
            self.__items.pop(name)

    def get_free_space(self):
        free_space = 0
        for value in self.__items.values():
            free_space += value
        return self.__capacity - free_space

    def get_items(self) -> Dict[str, int]:
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
