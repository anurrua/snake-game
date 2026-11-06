"""Тесты игровой логики."""

from snakegame.game import Game


def test_wall_collision() -> None:
    game = Game(10, 10, 8)
    game.snake.body = [(9, 5)]
    game.step((1, 0))
    assert game.is_over is True


def test_eating_food() -> None:
    game = Game(10, 10, 8)
    game.snake.body = [(5, 5)]
    game.food = (6, 5)
    game.step((1, 0))
    assert game.score == 1
    assert len(game.snake.body) == 2


def test_food_not_on_snake() -> None:
    game = Game(10, 10, 8)
    game.spawn_food()
    assert game.food not in game.snake.body


def test_game_over_when_no_free_cells() -> None:
    game = Game(2, 1, 4)
    game.snake.body = [(0, 0), (1, 0)]
    game.spawn_food()
    assert game.food is None
    assert game.is_over is True
