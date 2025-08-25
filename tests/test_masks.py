import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
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


transactions = [{"id": 1, "amount": 100, "currency": "USD", "description": "Purchase"},]

print("=== Тестирование filter_by_currency ===")

# Тест 1: Фильтрация USD транзакций
print("\n1. Фильтрация USD транзакций:")
usd_transactions = list(filter_by_currency(transactions, "USD"))
print(f"Найдено {len(usd_transactions)} USD транзакций:")
for transaction in usd_transactions:
    print(f"  ID: {transaction['id']}, Amount: {transaction['amount']}")


transactions = [{"id": 1, "amount": 100, "currency": "USD", "description": "Покупка в магазине"},]

print("=== Тестирование transaction_descriptions ===")

print("\n1. Все описания транзакций:")
descriptions = list(transaction_descriptions(transactions))
print(f"Получено {len(descriptions)} описаний:")
for i, desc in enumerate(descriptions, 1):
    print(f"  {i}. '{desc}'")


print("=== Тестирование card_number_generator ===")

# Тест 1: Генерация первых 5 номеров
print("\n1. Первые 5 номеров карт:")
generator = card_number_generator(1, 5)
first_five = list(generator)
for i, card in enumerate(first_five, 1):
    print(f"  {i}: {card}")

expected_first_five = [
    "0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
    "0000 0000 0000 0004",
    "0000 0000 0000 0005"
]

if first_five == expected_first_five:
    print("✓ Первые 5 номеров корректны")
else:
    print("✗ Ошибка в первых 5 номерах")
