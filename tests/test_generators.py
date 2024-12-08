import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator

transactions = [
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
]


def test_filter_by_currency_usd():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_empty_list():
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Нет требуемых транзанкций."
    # with pytest.raises(StopIteration):
    #     next(generator)


def test_filter_by_currency_mixed():
    mixed_transactions = transactions + [
        {
            "id": 999999999,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Invalid currency transaction",
            "from": "Счет 1234567890",
            "to": "Счет 0987654321"
        }
    ]
    generator = filter_by_currency(mixed_transactions, "USD")
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]
    with pytest.raises(StopIteration):
        next(generator)


# Тест: Корректные описания транзакций
def test_transaction_descriptions():
    transactions = [
        {
            "id": 1,
            "description": "Перевод организации"
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет"
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту"
        },
    ]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест: Пустой список транзакций
def test_transaction_descriptions_empty():
    transactions = []
    descriptions = transaction_descriptions(transactions)
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест: Транзакции без описаний
def test_transaction_descriptions_missing_descriptions():
    transactions = [
        {
            "id": 1,
            "amount": 1000
        },
        {
            "id": 2,
            "amount": 2000,
            "description": "Перевод со счета на счет"
        },
        {
            "id": 3,
        },
    ]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест: Смешанные данные
def test_transaction_descriptions_mixed():
    transactions = [
        {
            "id": 1,
            "description": "Операция 1"
        },
        {
            "id": 2,
            "amount": 2000
        },
        {
            "id": 3,
            "description": "Операция 3"
        },
    ]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Операция 1"
    assert next(descriptions) == "Операция 3"
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест: Генерация корректных номеров карт
@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (12, 15, [
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015",
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001",
    ]),
])
def test_card_number_generator_correctness(start, stop, expected):
    generator = card_number_generator(start, stop)
    generated_numbers = list(generator)
    assert generated_numbers == expected


# Тест: Проверка завершения генерации на больших диапазонах
def test_card_number_generator_large_range():
    start, stop = 1, 100
    generator = card_number_generator(start, stop)
    generated_numbers = list(generator)
    assert len(generated_numbers) == 100
    assert generated_numbers[0] == "0000 0000 0000 0001"
    assert generated_numbers[-1] == "0000 0000 0000 0100"


# Тест: Генерация с крайними значениями
def test_card_number_generator_edge_cases():
    start, stop = 0, 0
    generator = card_number_generator(start, stop)
    assert list(generator) == ["0000 0000 0000 0000"]


def test_card_number_generator_empty_range():
    start, stop = 5, 4
    generator = card_number_generator(start, stop)
    assert list(generator) == []


# Тест: Форматирование номеров карт
@pytest.mark.parametrize("start, expected", [
    (1, "0000 0000 0000 0001"),
    (12345678, "0000 0000 1234 5678"),
    (9999999999999999, "9999 9999 9999 9999"),
])
def test_card_number_generator_format(start, expected):
    generator = card_number_generator(start, start)
    assert next(generator) == expected
