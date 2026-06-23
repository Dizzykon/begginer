# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: FleetCare
class FleetCare:
    def __init__(self):
        self.records = []
    
    def add_record(self, vehicle_id, mileage, work_type, cost=None, reminder_date=None):
        record = {
            'id': len(self.records) + 1,
            'vehicle_id': vehicle_id,
            'mileage': mileage,
            'work_type': work_type,
            'cost': cost or 0.0,
            'reminder_date': reminder_date,
            'timestamp': self._get_timestamp()
        }
        self.records.append(record)
        return record
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

fleet = FleetCare()
