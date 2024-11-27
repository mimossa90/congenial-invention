import pytest

from src.masks import mask_card_number, mask_account


# Тестирование правильности маскирования номера карты.

@pytest.mark.parametrize('card_number, expected',
                         [
                             ('"1596837868705199"', '"1596 83** **** 5199"'),
                             ('"1234567890123456"', '"1234 56** **** 3456"'),
                             ('"7000792289606361"', '"7000 79** **** 6361"'),
                             ('"5734895775397395"', '"5734 89** **** 7395"'),
                             ('"6427862748509858"', '"6427 86** **** 9858"')
                         ])
def test_get_mask_card_number(card_number, expected):
    assert mask_card_number(card_number) == expected


# Проверка работы функции на различных входных форматах номеров
# карт, включая граничные случаи и нестандартные длины номеров.


@pytest.mark.parametrize("card_number, expected",
                         [
                        ("''", "Некорректные данные"),  # Пустая строка
                        ("12345678901234555555555556", "Некорректные данные")
                        ])


def test_mask_card_number_invalid(card_number):
    with pytest.raises(ValueError)  as exc_info:
        mask_card_number('')
        mask_card_number("12345678901234555555555556")
        mask_card_number("1234567")
    assert str(exc_info.value) == "Некорректные данные"
