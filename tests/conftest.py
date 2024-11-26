import pytest

@pytest.fixture()
def list_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


@pytest.fixture()
def card_number() -> list[str]:
    return [
        '7000 79** **** 6361',
        'Неверный номер карты'
        'Введите номер карты'
    ]




@pytest.fixture()
def date_format() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture()
def masked_data() -> str:
    return 'Maestro 1596 83** **** 5199'


