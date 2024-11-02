from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    """переводим в строку"""
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    """скрываем номер"""

    return mask_card_number


mask_card_number = get_mask_card_number("1596837868705199")



def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    """переводим в строку"""
    mask_account = "**" + account_number[-4:]
    """'скрываем номер"""
    return mask_account


mask_account = get_mask_account("Счет 64686473678894779589")
