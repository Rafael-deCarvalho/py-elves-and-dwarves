from app.players.elves.elf import Elf


class Druid(Elf):

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def player_info(self) -> str:
        self.info = (
            f"Druid {self.nickname}. {self.nickname} has a "
            f"favourite spell: {self.favourite_spell}"
        )
        return self.info

    def get_rating(self) -> str:
        self.rating = len(self.favourite_spell)
        return self.rating
