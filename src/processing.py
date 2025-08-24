from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(
        transactions: List[Dict[str, Any]],
        state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [tx for tx in transactions if tx.get('state') == state]


def sort_by_date(
        transactions: List[Dict[str, Any]],
        reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с ключом 'date' в формате строки
    :param reverse: Если True (по умолчанию) — сортировка по убыванию, иначе — по возрастанию
    :return: Отсортированный список
    :raises KeyError: Если отсутствует ключ 'date'
    :raises ValueError: Если неверный формат даты
    """

    def get_date(txn: Dict[str, Any]) -> datetime:
        """Вспомогательная функция для извлечения даты."""
        return datetime.strptime(txn['date'], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(transactions, key=get_date, reverse=reverse)


if __name__ == '__main__':
    # Пример данных для тестирования
    sample_transactions = [
        {"id": 1, "date": "2024-03-11T02:26:18.671407", "state": "EXECUTED"},
        {"id": 2, "date": "2023-12-28T14:10:22.120011", "state": "PENDING"},
        {"id": 3, "date": "2024-01-05T08:30:45.983221", "state": "EXECUTED"},
        {"id": 4, "state": "CANCELED"},  # Транзакция без даты для теста
    ]

    # Фильтрация
    print("EXECUTED transactions:")
    print(filter_by_state(sample_transactions))

    # Сортировка с обработкой ошибок
    try:
        print("\nSorted transactions:")
        print(sort_by_date([tx for tx in sample_transactions if 'date' in tx]))
    except (KeyError, ValueError) as e:
        print(f"Error during sorting: {e}")


def get_date():
    return None
