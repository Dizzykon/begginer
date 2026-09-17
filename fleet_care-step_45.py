# === Stage 45: Добавь восстановление из резервной копии ===
# Project: FleetCare
def load_backup(file_path):
    """Загружает записи из резервной копии и добавляет их в существующие."""
    backup_data = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(';')
                if len(parts) < 4:
                    continue
                plate, odometer, work, spending = parts[0], float(parts[1]), parts[2], float(parts[3])
                if plate not in backup_data:
                    backup_data[plate] = {'odometer': odometer, 'works': [], 'spending': 0}
                backup_data[plate]['odometer'] = max(backup_data[plate]['odometer'], odometer)
                backup_data[plate]['spending'] += spending
                backup_data[plate]['works'].append(work)
    except FileNotFoundError:
        print(f"Резервная копия не найдена: {file_path}")
        return
    for plate, data in backup_data.items():
        if plate not in fleet:
            fleet[plate] = {'odometer': 0, 'works': [], 'spending': 0}
        fleet[plate]['odometer'] = max(fleet[plate]['odometer'], data['odometer'])
        fleet[plate]['spending'] += data['spending']
        fleet[plate]['works'] = fleet[plate]['works'] + data['works']
    print(f"Записи из резервной копии восстановлены для {len(backup_data)} транспортных средств.")
