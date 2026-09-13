# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: FleetCare
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "underline": "\033[4m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
}

def colorize(text: str, color: str) -> str:
    if not color or color == "none":
        return text
    return ANSI.get(color, "") + text + ANSI["reset"]

def info(msg: str) -> str:
    return colorize(msg, "cyan")

def success(msg: str) -> str:
    return colorize(msg, "green")

def warn(msg: str) -> str:
    return colorize(msg, "yellow")

def error(msg: str) -> str:
    return colorize(msg, "red")

def bold(msg: str) -> str:
    return colorize(msg, "bold")

def dim(msg: str) -> str:
    return colorize(msg, "dim")

def header(text: str) -> str:
    return colorize(f"\n{'━' * 60}\n{text}\n{'━' * 60}", "bold")

def subheader(text: str) -> str:
    return colorize(f"\n── {text} ──", "bold")
