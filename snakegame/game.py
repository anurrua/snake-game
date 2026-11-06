"""Модуль управления игровой логикой."""

import random

from snakegame.snake import Snake


class Game:
    """Класс игровой логики."""

    def __init__(self, w: int, h: int, speed: int) -> None:
        self.w: int = w
        self.h: int = h
        self.speed: int = speed
        self.snake: Snake = Snake((w // 2, h // 2), (1, 0))
        self.food: tuple[int, int] | None = None
        self.score: int = 0
        self.is_over: bool = False
        self.level: int = 1
        self.food_per_level: int = 5
        self.spawn_food()

    def spawn_food(self) -> None:
        free_cells: list[tuple[int, int]] = []

        for x in range(self.w):
            for y in range(self.h):
                if (x, y) not in self.snake.body:
                    free_cells.append((x, y))

        if not free_cells:
            self.food = None
            self.is_over = True
            return

        self.food = random.choice(free_cells)

    def step(self, direction: tuple[int, int]) -> None:
        if self.is_over:
            return

        dx, dy = direction
        self.snake.direction = direction
        new_head = (
            self.snake.head()[0] + dx,
            self.snake.head()[1] + dy,
        )

        if new_head == self.food:
            self.snake.grow()
            self.score += 1
            self.level = self.score // self.food_per_level + 1
            self.speed = 4 + (self.level - 1) * 2

        self.snake.move(dx, dy)
        x, y = self.snake.head()

        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            self.is_over = True

        if self.snake.collides_self():
            self.is_over = True

        if new_head == self.food and not self.is_over:
            self.spawn_food()
