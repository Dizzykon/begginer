# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: FleetCare
import time
from typing import Optional

class ActionRevert:
    def __init__(self, action: 'BaseAction', fleet_manager: 'FleetManager'):
        self.action = action
        self.fleet_manager = fleet_manager
        self._reverted = False

    def revert(self) -> bool:
        if self._reverted:
            return False
        try:
            if isinstance(self.action, MileageAction):
                self.fleet_manager.mileage -= self.action.value
            elif isinstance(self.action, WorkOrderAction):
                self.fleet_manager.work_orders.remove(self.action)
                if self.action.notes:
                    self.fleet_manager.notes.append(self.action.notes)
                self.fleet_manager.work_orders.append(self.action)
            elif isinstance(self.action, ExpenseAction):
                self.fleet_manager.expenses.remove(self.action)
                self.fleet_manager.expenses.append(self.action)
            elif isinstance(self.action, ReminderAction):
                self.fleet_manager.reminders.remove(self.action)
                self.fleet_manager.reminders.append(self.action)
            elif isinstance(self.action, NotificationAction):
                self.fleet_manager.notifications.remove(self.action)
                self.fleet_manager.notifications.append(self.action)
            else:
                return False
            self._reverted = True
            return True
        except Exception:
            return False

    def __repr__(self):
        status = "reverted" if self._reverted else "pending"
        return f"<ActionRevert action={self.action.__class__.__name__} status={status}>"
