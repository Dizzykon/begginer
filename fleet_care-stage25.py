# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: FleetCare
def parse_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Неизвестный формат даты: {date_str!r}. Используйте YYYY-MM-DD или DD.MM.YYYY.")
