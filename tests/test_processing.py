import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize('list_date, state, expected',
                         [([], "EXECUTED", []),
                          ([], "CANCELED", []),
                          ([], "None", [])
                          ])


def test_filter_by_state_without_list(list_date, state, expected):
    assert filter_by_state(list_date, state) == expected



def test_filter_by_state(list_date: list, state: str = "EXECUTED"):
    if state == "EXECUTED":
        assert filter_by_state(list_date) == [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
        ]
    elif state == "CANCELED":
        assert filter_by_state(list_date) == [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]


def test_sort_by_date(list_date: list, reverse: bool = True):
    if reverse == reverse:
        assert sort_by_date(list_date) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                           {'id': 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                           {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
                                           ]
    elif reverse != reverse:
        assert sort_by_date(list_date) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                           {'id': 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                           {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                           {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}

                                           ]
