# Clogger/Clog.py

import logging
import time
import re
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """Кастомный форматтер для добавления цвета и формата вывода."""

    def format(self, record):
        # Запоминаем исходное сообщение
        original_msg = super().format(record)

        # Определяем цвет и формат вывода на основе уровня логирования
        if record.levelno == logging.INFO:
            color = Fore.GREEN
            status = "Успех ✓"
        elif record.levelno == logging.WARNING:
            color = Fore.YELLOW
            status = "Предупреждение ⚠"
        elif record.levelno == logging.ERROR:
            color = Fore.RED
            status = "Ошибка 𐄂"
        else:
            color = Fore.WHITE
            status = "Лог"

        # Подсветка путей в сообщении
        original_msg = self.highlight_paths(original_msg)

        # Получаем прошедшее время с начала работы программы
        elapsed_time = time.time() - record.created

        # Форматируем финальное сообщение
        formatted_msg = f"[{color}{status}{Style.RESET_ALL} | {elapsed_time:.2f} секунд] | {original_msg}"
        return formatted_msg

    @staticmethod
    def highlight_paths(message):
        """Подсвечивает пути в сообщении жёлтым цветом."""
        # Регулярное выражение для поиска путей
        path_pattern = re.compile(
            r'([A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*)|'
            r'(/(?:[^/ ]*/)*[^/ ]*)'
        )
        
        # Замена путей на подсвеченные жёлтым цветом
        return path_pattern.sub(lambda match: Fore.YELLOW + match.group(0) + Style.RESET_ALL, message)

def setup_custom_logger(name):
    """Настраивает кастомный логгер с цветным форматированием."""
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем консольный хендлер
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Устанавливаем кастомный форматтер для хендлера
    formatter = ColoredFormatter('%(message)s')
    console_handler.setFormatter(formatter)

    # Добавляем хендлер к логгеру
    logger.addHandler(console_handler)

    return logger
