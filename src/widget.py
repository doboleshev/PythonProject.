from datetime import datetime_CAPI

def mask_account_card(data: str, re=None) -> str:
    # Ищем тип (слово) и номер (только цифры)
    match = re.match(r'^(\D+)(\d+)$', data.strip())
    if not match:
        return "Неверный формат данных"

    name = match.group(1).strip()
    number = match.group(2)

    if 16 <= len(number) <= 19:  # Карта
        masked = number[:6] + '*' * (len(number) - 10) + number[-4:]
    elif len(number) >= 20:  # Счёт
        masked = '*' * (len(number) - 4) + number[-4:]
    else:
        return "Некорректная длина номера"

    return f"{name} {masked}"


from datetime import datetime

def get_date(date_str: str) -> str:
    try:
        # перевод исходной строки в объект datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        # Форматируем в нужный вид "ДД.ММ.ГГГГ"
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"