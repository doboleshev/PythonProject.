def get_mask_card_number(card_number: str | int) -> str:
    """
    Маскирует номер банковской карты, оставляя только первые 4 и последние 4 цифры.
    Остальные цифры заменяются на звездочки (*).
    """

    str_card = str(card_number).strip()  # Преобразуем в строку и убираем пробелы

    if len(str_card) < 8:
        raise ValueError("Номер карты слишком короткий для маскировки!")

    # Оставляем первые 4 и последние 4 цифры, остальное заменяем *
    masked_part = '*' * (len(str_card) - 8)
    return f"{str_card[:4]}{masked_part}{str_card[-4:]}"


def get_mask_account(account_number: str | int) -> str:
    """
    Маскирует номер банковского счета, оставляя только последние 4 цифры.
    Первые цифры заменяются на звездочки (*).
    """
    str_account = str(account_number).strip()

    if len(str_account) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    # Оставляем последние 4 цифры, остальное заменяем *
    masked_part = '*' * (len(str_account) - 4)
    return f"{masked_part}{str_account[-4:]}"
