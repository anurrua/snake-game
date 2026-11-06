"""Модуль обработки нажатий клавиш."""

import msvcrt


class Controls:
    """Класс управления клавишами."""

    def get_key(self) -> tuple[int, int] | str | None:
        if msvcrt.kbhit():
            key = msvcrt.getwch()

            if key in ("\x00", "\xe0"):
                key = msvcrt.getwch()
                if key == "H":
                    return (0, -1)
                elif key == "P":
                    return (0, 1)
                elif key == "K":
                    return (-1, 0)
                elif key == "M":
                    return (1, 0)
            else:
                key = key.lower()
                if key == "к":
                    return "r"
                elif key == "й":
                    return "q"
                elif key == "з":
                    return "p"
                return key

        return None
