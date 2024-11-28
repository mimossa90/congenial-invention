def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    # card_number = str(card_number)
    if len(card_number) == 16 and card_number.isdigit():
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    else:
        return "Неверный тип данных"


mask_card_number = get_mask_card_number("7000792289606361")


#print(mask_card_number)

def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if account_number and len(account_number) == 20 and account_number.isdigit():
        return "**" + account_number[-4:]
    else:
        return "Неверный тип данных"


mask_account = get_mask_account("64686473678894779589")
# print(mask_account)
