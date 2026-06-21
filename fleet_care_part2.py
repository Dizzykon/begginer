# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: FleetCare
class FleetRecord:
    def __init__(self, mileage: int, work_type: str, cost: float | None = None):
        self.mileage = mileage
        self.work_type = work_type.lower() if work_type else ""
        self.cost = cost or 0.0

    @property
    def is_valid(self) -> bool:
        return (self.mileage >= 0 and 
                len(self.work_type) <= 50 and 
                not self.cost < -1e9 and 
                not self.cost > 1e9)

def validate_input(mileage_str: str, work_type: str, cost_str: str | None = None):
    try:
        mileage = int(mileage_str.strip()) if mileage_str else 0
        cost = float(cost_str.strip()) if cost_str is not None and cost_str.strip() else 0.0
        return FleetRecord(mileage=abs(mileage), work_type=work_type, cost=max(0.0, min(abs(cost), 1e9)))
    except ValueError:
        raise ValueError("Некорректный формат ввода данных.")
