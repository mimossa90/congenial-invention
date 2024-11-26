from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if len(card_number) == 16:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    else:
        mask_card_number = "Неверный номер карты"

    return mask_card_number


mask_card_number = get_mask_card_number("7000792289606361")


# print(mask_card_number)

def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    return "**" + account_number[-4:]


mask_account = get_mask_account("Счет 64686473678894779589")
#print(mask_account)
