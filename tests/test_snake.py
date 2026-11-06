"""Тесты класса змейки."""

from snakegame.snake import Snake


def test_snake_head() -> None:
    snake = Snake((5, 5), (1, 0))
    assert snake.head() == (5, 5)


def test_snake_move() -> None:
    snake = Snake((5, 5), (1, 0))
    snake.move(1, 0)
    assert snake.head() == (6, 5)


def test_snake_grow() -> None:
    snake = Snake((5, 5), (1, 0))
    snake.grow()
    snake.move(1, 0)
    assert len(snake.body) == 2
