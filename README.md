# Проект 'PythonProject'
## Описание: 
Проект PythonProject включает в себя домашние задания 9.1, 9.2 и 9.3.
В домашнем задании 9.3 создан модуль 'processing.py', в котором есть 2 функции 'filter_by_state' и 'sort_by_date'

## Установка:
```
https://github.com/doboleshev/PythonProject.git
```

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](https://github.com/doboleshev/PythonProject.).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

# Банковский проект

Проект для работы с банковскими операциями, маскированием данных и форматированием.

## Функциональность

### Маскирование данных
- `mask_account_card(data: str) -> str` - маскирует номера карт и счетов
- `get_mask_card_number(card_number: str) -> str` - маскирует номер карты
- `get_mask_account(account_number: str | int) -> str` - маскирует номер счета

### Форматирование дат
- `get_date(date_str: str) -> Optional[str]` - преобразует дату из ISO формата в русский

## Тестирование

Проект включает комплексные тесты для всех основных функций.

### Запуск тестов

```bash
# Все тесты
pytest

# Конкретный тестовый файл
pytest tests/test_masks.py
# С подробным выводом
pytest -v
