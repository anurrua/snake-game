"""Модуль отображения игрового поля."""

import sys

from snakegame.game import Game


class Renderer:
    """Класс отображения игры."""

    def render(self, game: Game) -> None:
        sys.stdout.write("\033[H\033[J")

        lines = []
        lines.append("+" + "-" * game.w + "+")

        for y in range(game.h):
            row = ""
            for x in range(game.w):
                pos = (x, y)
                if pos == game.snake.head():
                    row += "O"
                elif pos in game.snake.body:
                    row += "o"
                elif pos == game.food:
                    row += "*"
                else:
                    row += " "
            lines.append("|" + row + "|")

        lines.append("+" + "-" * game.w + "+")
        lines.append(f"Score: {game.score} | Level: {game.level}")

        sys.stdout.write("\r\n".join(lines))
        sys.stdout.flush()
