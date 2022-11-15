# Домашка 21
from exeption import BaseError
from request import Request
from shop import Shop
from store import Store

# Cоздаём экземпляры класса
shop = Shop(
    items={
        'печеньки': 3,
        'ноутбук': 2,
    }
)

store = Store(
    items={
        'печеньки': 10,
        'ноутбук': 20,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        # Вывод товаров в хранилищах
        for storage in storages:
            print(f"В {storage} хранится:\n{storages[storage].get_items()}")
        # Пользовательский ввод
        user_input = input(
            "Введите строку в формате: Доставить 3 печеньки из склад в магазин\n"
            "Введите стоп или stop для выхода из программы\n"
        )
        if user_input in ('stop', 'стоп'):
            break
        # Обработка пользовательского ввода
        try:
            request = Request(request_str=user_input, storages=storages)
            print(f"Курьер забирает {request.quantity} {request.product} из {request.from_}")
            print(f"Курьер везет {request.quantity} {request.product} в {request.to_}")
            # Движение товара
            storages[request.from_].remove(request.product, request.quantity)
            storages[request.to_].add(request.product, request.quantity)
            print(f"Курьер доставил {request.quantity} {request.product} в {request.to_}")
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
