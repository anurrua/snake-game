"""Главный модуль запуска игры."""

import argparse
import time

from snakegame.controls import Controls
from snakegame.game import Game
from snakegame.renderer import Renderer


def main() -> None:
    """Запускает игру и управляет игровым процессом."""
    parser = argparse.ArgumentParser(description="Console Snake game")
    parser.add_argument("--width", type=int, default=20)
    parser.add_argument("--height", type=int, default=12)
    parser.add_argument("--speed", type=int, default=4)

    args = parser.parse_args()

    renderer = Renderer()
    controls = Controls()
    print("Управление: стрелки — движение")
    print("P — пауза, Q — выход")
    print("R — начать заново после проигрыша")
    time.sleep(2)
    while True:
        game = Game(args.width, args.height, args.speed)
        paused = False
        next_move = time.monotonic()
        while not game.is_over:
            key = controls.get_key()
            if key == "q":
                return
            if key == "p":
                paused = not paused
                if not paused:
                    next_move = time.monotonic()
                else:
                    print("PAUSED — press P to continue")
            elif isinstance(key, tuple):
                current = game.snake.direction
                if key != (-current[0], -current[1]):
                    game.snake.direction = key
            now = time.monotonic()
            if not paused and now >= next_move:
                game.step(game.snake.direction)
                renderer.render(game)
                next_move = now + 1 / game.speed
            time.sleep(0.01)
        print("\nGAME OVER!")
        print(f"Your score: {game.score}")
        print("Press R to play again or Q to quit")
        while True:
            key = controls.get_key()
            if key == "r":
                break
            if key == "q":
                return
            time.sleep(0.1)


if __name__ == "__main__":
    main()
