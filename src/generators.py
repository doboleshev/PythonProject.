from typing import Dict, Iterator


def filter_by_currency(transactions: list[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по указанной валюте.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, 'USD')

    Returns:
        Итератор, который выдает транзакции с указанной валютой
    """
    transaction: dict
    for transaction in transactions:
        if transaction.get('currency') == currency:
            yield transaction


def transaction_descriptions(transactions: list[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции по очереди.

    Args:
        transactions: Список словарей с транзакциями

    Returns:
        Итератор, который поочередно выдает описания транзакций
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """
    Генератор номеров банковских карт в заданном диапазоне.

    Args:
        start: Начальный номер карты (целое число от 1 до 9999999999999999)
        end: Конечный номер карты (целое число от start до 9999999999999999)

    Returns:
        Итератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX
    """
    # Проверка корректности диапазона
    if not (1 <= start <= end <= 9999999999999999):
        raise ValueError("Некорректный диапазон. Допустимые значения: 1-9999999999999999")

    for number in range(start, end + 1):
        # Форматируем число в 16-значную строку с ведущими нулями
        card_str = str(number).zfill(16)

        # Разбиваем на группы по 4 цифры
        formatted_card: str = ' '.join([card_str[i:i + 4] for i in range(0, 16, 4)])

        yield formatted_card
