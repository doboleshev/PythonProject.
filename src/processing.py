from typing import List, Dict, Any, Optional

def filter_by_state(
    transactions: List[Dict[str, Any]],
    state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями/операциями
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список словарей
    """
    return [tx for tx in transactions if tx.get('state') == state]

# Пример использования
transactions = [
    {"id": 1, "state": "EXECUTED", "amount": "100.00"},
    {"id": 2, "state": "PENDING", "amount": "200.00"},
    {"id": 3, "state": "EXECUTED", "amount": "300.00"},
    {"id": 4, "state": "CANCELED", "amount": "400.00"},
]

# Фильтрация по умолчанию (EXECUTED)
print(filter_by_state(transactions))
# [{'id': 1, 'state': 'EXECUTED', 'amount': '100.00'},
#  {'id': 3, 'state': 'EXECUTED', 'amount': '300.00'}]

# Фильтрация по другому состоянию
print(filter_by_state(transactions, state="CANCELED"))
# [{'id': 4, 'state': 'CANCELED', 'amount': '400.00'}]

from typing import List, Dict, Any
from datetime import datetime

def sort_by_date(
    transactions: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с ключом 'date' в формате строки
    :param reverse: Если True (по умолчанию) — сортировка по убыванию, иначе — по возрастанию
    :return: Отсортированный список
    """
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse
    )

# Пример использования
transactions = [
    {"id": 1, "date": "2024-03-11T02:26:18.671407", "state": "EXECUTED"},
    {"id": 2, "date": "2023-12-28T14:10:22.120011", "state": "PENDING"},
    {"id": 3, "date": "2024-01-05T08:30:45.983221", "state": "EXECUTED"},
]

# Сортировка по убыванию (новые -> старые)
print(sort_by_date(transactions))
# [{'id': 1, 'date': '2024-03-11T02:26:18.671407', 'state': 'EXECUTED'},
#  {'id': 3, 'date': '2024-01-05T08:30:45.983221', 'state': 'EXECUTED'},
#  {'id': 2, 'date': '2023-12-28T14:10:22.120011', 'state': 'PENDING'}]

# Сортировка по возрастанию (старые -> новые)
print(sort_by_date(transactions, reverse=False))
# [{'id': 2, 'date': '2023-12-28T14:10:22.120011', 'state': 'PENDING'},
#  {'id': 3, 'date': '2024-01-05T08:30:45.983221', 'state': 'EXECUTED'},
#  {'id': 1, 'date': '2024-03-11T02:26:18.671407', 'state': 'EXECUTED'}]
