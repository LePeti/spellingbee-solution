from flask import abort
from spellingb.spellingb import (
    InvalidLetterCountError,
    InvalidLettersError,
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
    except (
        InvalidLetterCountError,
        InvalidMainLetterError,
        LetterNotFoundError,
        InvalidLettersError,
    ) as err:
        return abort(400, str(err))
    # except InvalidMainLetterError as err:
    #     return abort(400, str(err))
    # except LetterNotFoundError as err:
    #     return abort(400, str(err))
    # except InvalidLettersError as err:
    #     return abort(400, str(err))

    solution: SpellingBeeSolution = SpellingBeeSolution(spellingb_game)

    return {"game": spellingb_game.__str__(), "solutions": list(solution.matches)}, 200
