# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: FleetCare
def search(self, term: str) -> list[Entry]:
        """Поиск записей по нескольким полям без учёта регистра."""
        lower = term.lower()
        matches = []
        for entry in self.entries:
            if (lower in entry.title.lower() or
                    lower in entry.description.lower()):
                matches.append(entry)
            elif any(lower == w.lower() for w in entry.work_list):
                matches.append(entry)
            elif any(lower == w.lower() for w in entry.maintenance_log):
                matches.append(entry)
        return matches
