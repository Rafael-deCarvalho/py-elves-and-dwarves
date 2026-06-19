from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    sum_rating = 0
    for player in team:
        sum_rating += player.get_rating()
    return sum_rating


def elves_concert(singers: list[Elf]) -> None:
    for elf in singers:
        elf.play_elf_song()


def feast_of_the_dwarves(feasters: list[Dwarf]) -> None:
    for dwarf in feasters:
        dwarf.eat_favourite_dish()
