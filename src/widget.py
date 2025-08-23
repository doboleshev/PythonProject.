import re
from datetime import datetime
from typing import Optional


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счёта.

    :param data: Строка вида "Visa Platinum 1234567890123456" или "Счёт 12345678901234567890"
    :return: Маскированная строка или сообщение об ошибке
    """
    # Ищем тип (слово) и номер (только цифры)
    match = re.match(r'^(\D+)(\d+)$', data.strip())
    if not match:
        return "Неверный формат данных"

    name = match.group(1).strip()
    number = match.group(2)

    if 16 <= len(number) <= 19:  # Карта
        masked = number[:6] + '*' * (len(number) - 10) + number[-4:]
        # Форматируем номер карты группами по 4 цифры
        formatted_masked = ' '.join([masked[i:i + 4] for i in range(0, len(masked), 4)])
        return f"{name} {formatted_masked}"

    elif len(number) >= 20:  # Счёт
        masked = '**' + number[-4:]
        return f"{name} {masked}"

    else:
        return "Некорректная длина номера"


def get_date(date_str: str) -> Optional[str]:
    """
    Преобразует дату из формата ISO в русский формат.

    :rtype: Optional[str]
    :param date_str: Дата в формате "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024" или None при ошибке
    """
    try:
        # Парсим дату (обрабатываем разные варианты формата)
        if '.' in date_str.split('T')[1]:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, AttributeError):
        return None


# Примеры использования
if __name__ == "__main__":
    # Тестирование mask_account_card
    test_cases = [
        "Visa Platinum 1234567890123456",
        "Счёт 12345678901234567890",
        "MasterCard 123456789012",
        "МИР 1234567890123456",
        "Неверный формат"
    ]

    for test in test_cases:
        print(f"{test} -> {mask_account_card(test)}")

    print("\n" + "=" * 50 + "\n")

    # Тестирование get_date
    date_test_cases = [
        "2024-03-11T02:26:18.671407",
        "2023-12-28T14:10:22.120011",
        "неверная дата",
        "2024-01-05T08:30:45"
    ]

    for date_test in date_test_cases:
        result = get_date(date_test)
        print(f"{date_test} -> {result if result else 'Ошибка формата'}")
