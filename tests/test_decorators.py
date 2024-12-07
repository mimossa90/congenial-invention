import pytest
from src.decorators import log


@log()
def add(x, y):
    return x + y


@log()
def multiply(x, y):
    if x == 0 or y == 0:
        raise ValueError("Умножение на ноль")
    return x * y


@log(filename="my_log.txt")
def add_to_file(x, y):
    return x + y


@log(filename="my_log.txt")
def multiply_to_file(x, y):
    if x == 0 or y == 0:
        raise ValueError("Умножение на ноль")
    return x * y


def test_success_console(capsys):
    """Успешное выполнение функции в консоль"""
    result = add(3, 2)
    captured = capsys.readouterr()
    assert result == 5
    assert "'add' ok." in captured.out
    assert "Execution time:" in captured.out


def test_error_console(capsys):
    """Вывод ошибки в консоль"""
    with pytest.raises(ValueError, match="Умножение на ноль"):
        multiply(0, 5)
    captured = capsys.readouterr()
    assert "'multiply' error: Умножение на ноль" in captured.out
    assert "Inputs: (0, 5), {}" in captured.out
