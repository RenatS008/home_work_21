from classes.courier import Courier
from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from exceptions import InvalidRequests, BaseError

store = Store(items={
    "Печеньки": 25,
    "Собачки": 25,
    "Елка": 25
})

shop = Shop(items={
    "Печеньки": 2,
    "Собачки": 2,
    "Елка": 2
})

storages = {
    "Магазин": shop,
    "Склад": store
}


def main():

    while True:
        """
        Вывод информации о товаре и его местонахождение
        """
        for storage_name in storages:
            print(f"Место нахождение товара:\n{storage_name}\n"
                  f"Наименование/количество товара: \n{storages[storage_name].get_items()}")

        """
        Ввод запроса
        """
        user_input = input(
            'Введите запрос: \n'
            '(Пример: Доставить 3 печеньки из склада в магазин)\n'
            'Введите "закончить", для завершения запросов\n'
        )

        """
        Проверка остановки запросов 
        """
        if user_input.lower() in "закончить":
            break

        """
        Проверка на корректность запроса
        """
        try:
            request = Request(request=user_input)
        except InvalidRequests as e:
            print(e.message)
            continue

        """
        Формирование запроса
        """
        courier = Courier(
            request=request,
            storages=storages,
        )

        """
        Проверка запроса на ошибки
        """
        try:
            courier.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
