import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "data_test, correct_data",
    [
        ('2024-11-26', '26.11.2024'),  # Стандартный формат
        ('2000-01-01', '01.01.2000'),  # Минимальная дата
        ('2024-02-29', '29.02.2024'),  # Високосный год
    ]
)
def test_get_date(data_test, correct_data):
    """Тестируем корректные преобразования дат"""
    assert get_date(data_test) == correct_data


def test_get_date_invalid_format():
    """Тестируем некорректный формат даты, длину или пустую строку"""
    with pytest.raises(ValueError) as exc_info:
        get_date('2024/11/260000')
        get_date('2024|02|31')
        get_date('2024.02.31')
        get_date('')
        get_date('2024-11-2')
        get_date('оодлывоавыд')
    assert str(exc_info.value) == "Неверный тип строки"


@pytest.mark.parametrize(
    "data_test, correct_data",
    [
    ("Счет 64686473678894779589", "Счет ****9589"),
    ("Maestro 1596837868705199", "Maestro 1596 **** **** 5199"),
    ("MasterCard 1234567890123456", "MasterCard 1234 **** **** 3456"),
    ("Visa Classic 1234567890123456", "Visa Classic **** **** **** 3456"),
    ("Visa Platinum 1234567890123456", "Visa Platinum **** **** **** 3456"),
    ("Visa Gold 1234567890123456", "Visa Gold **** **** **** 3456"),
])
def test_mask_account_card(data_test, correct_data):
    assert mask_account_card(data_test) == correct_data



def test_mask_account_card_invalid():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет ")
        mask_account_card("Maestro ")
        mask_account_card("")
    assert str(exc_info.value) == "Неверный тип данных"

