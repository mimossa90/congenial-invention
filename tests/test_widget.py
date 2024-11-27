import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "date_format, expected",
    [
        ('2024-11-26', '26.11.2024'),
        ('2000-01-01', '01.01.2000'),
        ('2024-02-29', '29.02.2024'),
        ("2024|02|31", "Неверный формат данных"),
        ("2024.02.31", "Неверный формат данных"),
        ("", "Неверный формат данных"),
        ("оодлывоавыд", "Неверный формат данных"),
        ("2024.T.31", "Неверный формат данных")
    ]
)
def test_get_date(date_format, expected):
    """Тестируем корректные преобразования дат"""
    assert get_date(date_format) == expected


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
    "account_card_invalid, expected",
    [
        ("Счет ", "Неверный тип данных"),
        ("Maestro ", "Неверный тип данных"),
        ("", "Неверный тип данных"),
        ("859438509845", "Неверный тип данных"),

    ])
def test_mask_account_card_invalid(account_card_invalid, expected):
    assert mask_account_card(account_card_invalid) == expected

# @pytest.mark.parametrize(
#     "account_card_invalid",
#     [
#         ("1596837868705199"),
#         ("Счет 646779589"),
#         ("Mad 71583007758"),
#         ("eddfdf3538556"),
#         ("Vis 68354511321511982476737658"),
#         ("inum"),
#         ("dfgvb465745"),
#         (""),
#     ],
# )
# def test_mask_account_card_invalid(account_card_invalid):
#     """Тест на корректность входных данных."""
#     with pytest.raises(ValueError):
#         mask_account_card(account_card_invalid)
