# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: FleetCare
def migrate_to_v46(conn):
    """Переход на новую версию структуры данных: добавление поля is_reminder в таблицу maintenance."""
    conn.execute("ALTER TABLE maintenance ADD COLUMN is_reminder BOOLEAN DEFAULT FALSE")
    conn.commit()
