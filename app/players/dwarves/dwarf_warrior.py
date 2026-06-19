from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def player_info(self) -> str:
        self.info = (
            f"Dwarf warrior {self.nickname}. {self.nickname} has a "
            f"hummer of the {self.hummer_level} level"
        )
        return self.info

    def get_rating(self) -> str:
        self.rating = self.hummer_level + 4
        return self.rating
