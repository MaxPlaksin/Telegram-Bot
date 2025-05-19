import psutil
import time
import ctypes
from datetime import datetime

LOG_FILE = "activity_log.txt"

# --- Функция логирования ---
def log_activity(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        file.write(f"{timestamp} {message}\n")

# --- Время бездействия (Windows) ---
def get_idle_time():
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)):
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0  # в секундах
    else:
        return 0

# --- Время работы компьютера ---
def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = now - boot_time
    uptime_formatted = datetime.utcfromtimestamp(uptime_seconds).strftime('%H:%M:%S')
    return uptime_formatted

# --- Топ-
