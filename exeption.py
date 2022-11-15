# Обработка ошибок
class BaseError(Exception):
    message = 'Неизвестная ошибка'


class ToManyProductError(BaseError):
    message = 'Слишком много разных товаров'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class UnknownRequestError(BaseError):
    message = 'Некорректный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестное хранилище товаров'
