# Создайте функцию filter_by_currency, которая принимает на вход список
# словарей, представляющих транзакции.
# Функция должна возвращать итератор, который поочередно выдает транзакции,
# где валюта операции соответствует заданной (например, USD).
from typing import Generator, Union, Dict, List


def filter_by_currency(list_data: list[dict], code: str) -> Generator[Union[Dict, str], None, None]:
    filtered_result = filter(lambda x: x['operationAmount']['currency']['code'] == code, list_data)
    item = next(filtered_result, None)
    if item is None:
        yield "Нет требуемых транзанкций."
    yield item
    yield from filtered_result


transactions = filter_by_currency([
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    # {
    #     "id": 895315941,
    #     "state": "EXECUTED",
    #     "date": "2018-08-19T04:27:37.904916",
    #     "operationAmount": {
    #         "amount": "56883.54",
    #         "currency": {
    #             "name": "USD",
    #             "code": "USD"
    #         }
    #     },
    #     "description": "Перевод с карты на карту",
    #     "from": "Visa Classic 6831982476737658",
    #     "to": "Visa Platinum 8990922113665229"
    # },
    # {
    #     "id": 594226727,
    #     "state": "CANCELED",
    #     "date": "2018-09-12T21:27:25.241689",
    #     "operationAmount": {
    #         "amount": "67314.70",
    #         "currency": {
    #             "name": "руб.",
    #             "code": "RUB"
    #         }
    #     },
    #     "description": "Перевод организации",
    #     "from": "Visa Platinum 1246377376343588",
    #     "to": "Счет 14211924144426031657"
    # }
], "USD")

try:
    print(next(transactions))
    print(next(transactions))
    print(next(transactions))
except StopIteration:
    print("Нет транзанкций для вывода на экран")


# Напишите генератор transaction_descriptions, который принимает список словарей с
# транзакциями и возвращает описание каждой операции по очереди.

def transaction_descriptions(list_data: List[dict]) -> Generator[str]:
    """генератор transaction_descriptions, который принимает список словарей с
       транзакциями и возвращает описание каждой операции по очереди"""
    for data in list_data:
        if "description" in data:
            yield data.get("description")


descriptions = transaction_descriptions([
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
])

print(next(descriptions))
print(next(descriptions))
print(next(descriptions))


# Создайте генератор  card_number_generator, который выдает номера банковских карт в
# #формате  XXXX XXXX XXXX XXXX, где X — цифра номера карты.
# #Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
# Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор выдает номера банковский карт"""
    for number in range(start, stop + 1):
        # if len(str(number)) <= 16:
        #     numbers = "0" * (16 - len(str(number))) + str(number)
        numbers = f"{number:016}"
        formated_number = f'{numbers[:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:]}'
        yield formated_number


card_number = card_number_generator(1, 10000000000000000)
print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))
