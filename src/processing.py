


def filter_by_state(list_date: list, state: str="EXECUTED") -> list:
    """функция сортировки по статусу"""
    result = []
    for date in list_date:
        if date.get("state") == state:
            result.append(date)
    return result


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state="EXECUTED",
    )
)


def sort_by_date(list_date: list, reverse: bool=True) -> list:
    """функция сортировки по дате"""
    list_date.sort(key=lambda date: date.get("date"), reverse=reverse)
    return list_date


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]
    )
)
