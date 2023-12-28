from flask import abort

from spellingb.spellingb import (
    InvalidLetterCountError,
    InvalidMainLetterError,
    LetterNotFoundError,
    SpellingBeeGame,
    SpellingBeeSolution,
)


def solution(puzzle: dict[str, str]) -> tuple[list[str], int]:
    letters: str = puzzle["letters"]
    main_letter: str = puzzle["main_letter"]

    try:
        spellingb_game: SpellingBeeGame = SpellingBeeGame.from_string(
            letters, main_letter
        )
    except InvalidLetterCountError as err:
        return abort(400, str(err))
    except InvalidMainLetterError as err:
        return abort(400, str(err))
    except LetterNotFoundError as err:
        return abort(400, str(err))

    solution: SpellingBeeSolution = SpellingBeeSolution(spellingb_game)

    return list(solution.matches), 200
