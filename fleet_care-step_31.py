# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: FleetCare
def switch_profile(self, profile_name):
        """Переключить активный профиль пользователя"""
        if profile_name not in self.profiles:
            print(f"Профиль '{profile_name}' не найден")
            return
        self.active_profile = profile_name
        self.active_user = self.profiles[profile_name]
        print(f"Переключен на профиль: {profile_name} (ID: {self.active_user.id})")
