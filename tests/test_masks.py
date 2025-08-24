import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


@pytest.fixture
def test_get_mask_card_number_short() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234")


def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.mark.parametrize("account_number, expected", [
    # Тесты для строковых входных данных
    ("1234567890", "******7890"),
    ("73654108430135874305", "****************4305"),
    ("000012345678", "********5678"),
    ("9999", "9999"),  # Минимальная длина
    # Тесты для числовых входных данных
    (1234567890, "******7890"),
    (73654108430135874305, "****************4305"),
    (9999, "9999"),
])
def test_get_mask_account_valid(account_number: str | int, expected: str) -> None:
    """Тестирование валидных номеров счетов"""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_whitespace() -> None:
    """Тестирование номера счета с пробелами по краям"""
    assert get_mask_account("  12345678  ") == "****5678"


def test_get_mask_account_edge_cases() -> None:
    """Тестирование крайних случаев"""
    # Проверяем, что функция корректно обрабатывает граничные значения
    assert get_mask_account("1234") == "1234"  # Ровно 4 символа


@pytest.fixture
def test_mask_account_card_valid(data: str, expected: str) -> None:
    """Тестирование валидных входных данных"""
    result = mask_account_card(data)
    assert expected == result


@pytest.fixture
def test_get_date_valid_formats(date_str: str, expected: str) -> None:
    """Тестирование валидных форматов дат"""
    result = get_date(date_str)
    assert result == expected
    assert isinstance(result, str)
