import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("5734895775397395", "5734 89** **** 7395"),
        ("6427862748509858", "6427 86** **** 9858")
    ])
def test_get_mask_card_number(card_number, expected):
    """Проверка правильности маскировки, ответ функции на различные длины и отсутствие номера"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "",
        "15968378",
        "642786274850985878077835",
        "573489dddd5397395"
    ]
)
def test_get_mask_card_number_invalid(card_number):
    """Тестирование выброса исключения для некорректного номера карты"""
    with pytest.raises(ValueError) as exc:
        get_mask_card_number(card_number)
    assert str(exc.value) == "Неверный формат данных"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("57348957753973951234", "**1234"),
    ]
)
def test_get_mask_account_valid(account_number, expected):
    """Тестирование корректной маскировки номера счета"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        "",
        "6468",
        "646864736788947795897538548739573",
        "573489dddd539773547539578395",
    ]
)
def test_get_mask_account_invalid(account_number):
    """Тестирование выброса исключения для некорректного номера счета"""
    with pytest.raises(ValueError) as exc:
        get_mask_account(account_number)
    assert str(exc.value) == "Неверный формат данных"
