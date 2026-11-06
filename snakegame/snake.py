"""Модуль для управления змейкой."""


class Snake:
    """Класс змейки."""

    def __init__(
        self,
        start_pos: tuple[int, int],
        direction: tuple[int, int],
    ) -> None:
        self.body: list[tuple[int, int]] = [start_pos]
        self.direction: tuple[int, int] = direction
        self.growth: int = 0

    def head(self) -> tuple[int, int]:
        return self.body[0]

    def move(self, dx: int, dy: int) -> None:
        new_head = (self.body[0][0] + dx, self.body[0][1] + dy)
        self.body.insert(0, new_head)
        if self.growth > 0:
            self.growth -= 1
        else:
            self.body.pop()

    def grow(self) -> None:
        self.growth += 1

    def collides_self(self) -> bool:
        return self.head() in self.body[1:]
