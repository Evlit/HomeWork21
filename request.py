# Класс обработки пользовательского ввода
from typing import Dict

from abstract import Storage
from exeption import UnknownRequestError, UnknownStorageError


class Request:
    def __init__(self, request_str, storages: Dict[str, Storage]):
        list_req = request_str.lower().split(' ')
        if len(list_req) != 7 or not list_req[1].isdigit():
            raise UnknownRequestError

        self.quantity = int(list_req[1])
        self.product = list_req[2]
        self.to_ = list_req[6]
        self.from_ = list_req[4]

        if self.to_ not in storages or self.from_ not in storages:
            raise UnknownStorageError
