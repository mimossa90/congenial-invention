import pytest

from src.widget import mask_account_card, get_date


def test_get_date(date_format):
    """Тестируем корректные преобразования дат"""
    assert get_date(date_format) == "11.03.2024"


@pytest.mark.parametrize(
    "invalid_date_format",
    [
        ("2024|02|31T"),
        ("2024.02.31T"),
        (""),
        ("оодлывоавыд"),
        ("2024.T.31")
    ]
)

def test_get_date_invalid(invalid_date_format):
    """Тестируем некорректные вводные"""
    with pytest.raises(ValueError) as e:
        get_date(invalid_date_format)
    assert str(e.value) == "Неверный формат данных"



@pytest.mark.parametrize(
    "data_test, correct_data",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro 8315967868705199", "Maestro 8315 96** **** 5199"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Visa Gold 1234567890123456", "Visa Gold 1234 56** **** 3456"),
    ])

def test_mask_account_card(data_test, correct_data):
    assert mask_account_card(data_test) == correct_data


@pytest.mark.parametrize(
    "account_card_invalid",
    [
        ("1596837868705199"),
        ("Счет 646779589"),
        ("Mad 71583007758"),
        ("eddfdf3538556"),
        ("Vis 68354511321511982476737658"),
        ("inum"),
        ("dfgvb465745"),
        (""),
    ]
)


def test_mask_account_card_invalid(account_card_invalid):
    """Тест на корректность входных данных."""
    with pytest.raises(ValueError):
        mask_account_card(account_card_invalid)
