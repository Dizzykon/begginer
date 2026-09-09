# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: FleetCare
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="FleetCare CLI")
    sub = parser.add_subparsers(dest="command")

    p_log = sub.add_parser("log", help="Записать запись в журнал")
    p_log.add_argument("--type", required=True, choices=["mileage", "work", "expense", "reminder"],
                       help="Тип записи")
    p_log.add_argument("--date", required=True, help="Дата (YYYY-MM-DD)")
    p_log.add_argument("--plate", required=True, help="Госномер")
    p_log.add_argument("--detail", help="Детали записи")

    p_view = sub.add_parser("view", help="Показать записи")
    p_view.add_argument("--type", choices=["mileage", "work", "expense", "reminder"],
                        help="Фильтр по типу")
    p_view.add_argument("--plate", help="Фильтр по госномеру")
    p_view.add_argument("--date", help="Фильтр по дате")

    p_stats = sub.add_parser("stats", help="Статистика")
    p_stats.add_argument("--plate", help="По госномеру")

    p_export = sub.add_parser("export", help="Экспорт JSON")
    p_export.add_argument("--type", choices=["mileage", "work", "expense", "reminder"],
                          help="Тип для экспорта")
    p_export.add_argument("--plate", help="По госномеру")

    args = parser.parse_args()

    try:
        if args.command == "log":
            log_entry(args)
        elif args.command == "view":
            print_entries(args)
        elif args.command == "stats":
            print_stats(args)
        elif args.command == "export":
            export_data(args)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
