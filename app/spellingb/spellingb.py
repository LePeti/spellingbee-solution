from collections import Counter
from random import choice, sample
from string import ascii_lowercase
from typing import Iterable, Literal, Optional

from english_words import get_english_words_set  # type: ignore


class LetterNotFoundError(Exception):
    pass


class InvalidLetterCountError(Exception):
    pass


class InvalidMainLetterError(Exception):
    pass


class SpellingBeeGame:
    """A Game of Spelling Bee that consists of 7 distinct letters and one of those is
    the main letter. You need to create words that are at least 3 letters long,
    consists of the selected letters and contain the main letter.
    """

    def __init__(
        self, letters: Optional[Iterable[str]] = None, main_letter: Optional[str] = None
    ) -> None:
        self.letters: set[str] = (
            set([letter.lower() for letter in letters])
            if letters
            else self._provide_7_random_letters()
        )

        if len(self.letters) != 7:
            raise InvalidLetterCountError(
                f"7 distinct letters needed. {len(self.letters)} provided: "
                f"{self.letters}"
            )
        self.main_letter: str = (
            main_letter.lower()
            if main_letter
            else self._pick_random_letter(self.letters)
        )

        if len(self.main_letter) != 1 or self.main_letter not in list(ascii_lowercase):
            raise InvalidMainLetterError(
                "Main letter must be a single letter from the English alphabet. "
                f"'{self.main_letter}' provided"
            )

        if self.main_letter not in self.letters:
            raise LetterNotFoundError(
                f"Letter '{self.main_letter}' not in '{self.letters}'"
            )

    @classmethod
    def from_string(
        cls, letters: str, main_letter: Optional[str] = None
    ) -> "SpellingBeeGame":
        return cls(set(letters.lower()), main_letter)

    def _provide_7_random_letters(self) -> set[str]:
        return set(sample(list(ascii_lowercase), k=7))

    def _pick_random_letter(self, letters: set[str]) -> str:
        return choice(list(letters))

    def __str__(self) -> str:
        return f"'{'-'.join(sorted(self.letters))}' <{self.main_letter}>"


class SpellingBeeSolution:
    """_summary_"""

    MIN_WORD_LENGTH: Literal[3] = 3

    def __init__(self, game: Optional[SpellingBeeGame] = None) -> None:
        self.game: SpellingBeeGame = game if game else SpellingBeeGame()
        self.english_words: set[str] = get_english_words_set(["web2"], lower=True)
        self.word_set: set[str] = {
            word for word in self.english_words if len(word) > self.MIN_WORD_LENGTH
        }
        self.matches: list[str] = self._find_matching_words()
        self.num_matches: int = len(self.matches)

    def _find_matching_words(self) -> list[str]:
        matches: set[str] = {
            word
            for word in self.word_set
            if self.game.main_letter in word
            and set(word).issubset(set(self.game.letters))
        }
        return sorted(matches)

    def get_longest_words(self, n: int = 3) -> list[str]:
        return sorted(self.matches, key=len, reverse=True)[:n]

    def get_first_letter_counts(self) -> Counter[str]:
        return Counter(word[0] for word in self.matches)

    def get_letter_counts(self) -> Counter[str]:
        return Counter("".join(self.matches))

    def plot_ascii_histogram(
        self, item_counts: list[tuple[str, int]], symbol: str = "+"
    ) -> None:
        for item, frequency in item_counts:
            print(f"{item} |{symbol * frequency} {frequency} ")

        return None

    def bar_chart_of_letter_counts(self) -> None:
        letter_counts: list[tuple[str, int]] = self.get_letter_counts().most_common()
        self.plot_ascii_histogram(letter_counts)
        return None

    def bar_chart_of_first_letter_counts(self, symbol="+") -> None:
        first_letter_counts: list[
            tuple[str, int]
        ] = self.get_first_letter_counts().most_common()
        self.plot_ascii_histogram(first_letter_counts)
        return None


if __name__ == "__main__":
    game: SpellingBeeGame = SpellingBeeGame.from_string("CKEAOLB", "E")
    solution = SpellingBeeSolution(game=game)
    print("\n")
    print(f"game: {game}")
    print("\n")
    print(f"total matches: {solution.num_matches}")
    first_letter_counts: Counter = solution.get_first_letter_counts()
    print("\n")
    print("First letter counts:")
    print("\n")
    solution.bar_chart_of_first_letter_counts()
    print("\n")
    print(f"Letter counts:\n")
    letter_counts: Counter = solution.get_letter_counts()
    print(letter_counts.most_common())
    print("\n")
    solution.bar_chart_of_letter_counts()
    print("\n")
    print(f"3 longest words: {solution.get_longest_words(10)}")
    print("\n")
    print(f"20 examples:\n{sample(list(solution.matches), 20)}")
