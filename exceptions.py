class BaseError(Exception):
    message = 'Произошла ошибка.'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места на диске.'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара на складе.'


class TooManyDifferentProducts(BaseError):
    message = 'Невозможно добавить товар, лимит ассортимента.'


class InvalidRequests(BaseError):
    message = 'Неверный запрос. Повторите запрос.'
