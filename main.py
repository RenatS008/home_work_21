from classes.courier import Courier
from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from exceptions import InvalidRequests, BaseError

store = Store(items={
    "печеньки": 25,
    "собачки": 25,
    "елка": 25
})

shop = Shop(items={
    "печеньки": 2,
    "собачки": 2,
    "елка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    while True:  # Вывод информации о товаре и его местонахождение

        for storage_name in storages:
            print(f"Место нахождение товара:\n{storage_name}\n"
                  f"Наименование/количество товара: \n{storages[storage_name].get_items()}")

        user_input = input(
            'Введите запрос: \n'
            '(Пример: Доставить 3 печеньки из склад в магазин)\n'
            'Введите "закончить", для завершения запросов\n'
        )

        if user_input.lower() in "закончить":
            break

        try:  # Проверка на корректность запроса
            request = Request(request=user_input)
        except InvalidRequests as e:
            print(e.message)
            continue

        courier = Courier(  # Формирование запроса
            request=request,
            storages=storages,
        )

        try:  # Проверка запроса на ошибки
            courier.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
