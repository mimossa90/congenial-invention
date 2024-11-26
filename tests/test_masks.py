import pytest

from src.masks import mask_card_number, mask_account


#Тестирование правильности маскирования номера карты.

@pytest.mark.parametrize("input_data, expected_output", [
    ("Счет 64686473678894779589", "****9589"),
    ("Maestro 1596837868705199", "1596 **** **** 5199"),
    ("MasterCard 1234567890123456", "1234 **** **** 3456"),
    ("Visa Classic 1234567890123456", "**** **** **** 3456"),
    ("Visa Platinum 1234567890123456", "**** **** **** 3456"),
    ("Visa Gold 1234567890123456", "**** **** **** 3456"),
])
def test_mask_card_number(input_data, expected_output):
    assert mask_card_number(input_data) == expected_output


# Проверка работы функции на различных входных форматах номеров
# карт, включая граничные случаи и нестандартные длины номеров.


@pytest.mark.parametrize("input_data", [
    "Некорректные данные",
    "Счет",  # Отсутствует номер
    "Maestro ",  # Отсутствует номер
    "",  # Пустая строка
    None,  # None как входные данные
    "Visa Gold 12345678901234555555555556"
])
def test_mask_card_number_invalid(input_data):
    with pytest.raises(TypeError):
        mask_card_number(input_data)



