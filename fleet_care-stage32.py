# === Stage 32: Добавь журнал действий пользователя ===
# Project: FleetCare
class JournalEntry:
    def __init__(self, timestamp, user, action):
        self.timestamp = timestamp
        self.user = user
        self.action = action

    def __repr__(self):
        return (f"JournalEntry(timestamp={self.timestamp}, user={self.user}, "
                f"action={self.action})")
