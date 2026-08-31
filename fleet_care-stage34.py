# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: FleetCare
class Template:
    def __init__(self, name, record_type, default_values):
        self.name = name
        self.record_type = record_type
        self.default_values = default_values

    def create_record(self):
        record = Record(self.record_type)
        record.id = str(len(record._all_records) + 1)
        for key, value in self.default_values.items():
            if hasattr(record, key):
                setattr(record, key, value)
        record._all_records.append(record)
        return record

    def __repr__(self):
        return f"Template({self.name}, {self.record_type}, {self.default_values})"
