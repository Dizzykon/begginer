# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: FleetCare
def archive_old_records(db: dict, days_threshold=365):
    """Архивирует записи старше указанного количества дней."""
    cutoff = datetime.now().date() - timedelta(days=days_threshold)
    archived_ids = []
    for key in db:
        try:
            record_date = datetime.strptime(db[key]["timestamp"], "%Y-%m-%d").date()
            if record_date < cutoff and "archived" not in db[key]:
                db[key].update({"status": "archived", "archive_date": str(cutoff)})
                archived_ids.append(key)
        except Exception:
            pass
    print(f"[Archive] {len(archived_ids)} записей архивированы старше {days_threshold} дней.")
