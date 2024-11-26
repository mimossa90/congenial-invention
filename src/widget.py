from typing import Union

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(masked_data: Union[str]) -> Union[str]:
    '''Функция маскировки счета и номера банковской карты'''
    masked_account = str(get_mask_account(masked_data.split()[-1]))
    masked_number = str(get_mask_card_number(masked_data.split()[-1]))
    if "Счет" in masked_data:
        return "Счет " + masked_account
    elif "Maestro" in masked_data:
        return "Maestro " + masked_number
    elif "MasterCard" in masked_data:
        return "MasterCard " + masked_number
    elif "Visa Classic" in masked_data:
        return "Visa Classic " + masked_number
    elif "Visa Platinum" in masked_data:
        return "Visa Platinum " + masked_number
    elif "Visa Gold" in masked_data:
        return "Visa Gold " + masked_number
    else:
        return "Неизвестный тип данных"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Счет 73654108430135874305"))




def get_date(date_format):
    """Функция преобразования формата даты с 'YYYY-MM-DD' в 'DD.MM.YYYY'"""
    return f"{date_format[8:10]}.{date_format[5:7]}.{date_format[0:4]}"

#print(get_date("2024-03-11T02:26:18.671407"))
