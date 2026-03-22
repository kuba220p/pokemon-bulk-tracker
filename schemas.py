class PokemonCard:
    def __init__(self, name: str, card_no: int, count: int, parent_set: str, is_reverse: bool):
        self._name = name
        self._card_no = card_no
        self._count = count
        self._parent_set = parent_set
 
    def name(self) -> str:
        return self._name
    
    def card_no(self) -> int:
        return self._card_no
    
    def count(self) -> int:
        return self._count

    def parent_set(self) -> str:
        return self._parent_set
    
    def __str__(self) -> str:
        return f'Pokemon: {self.name()}, Set: {self.parent_set()}, Card No.: {self.card_no()}'
    
class ReverseHolo(PokemonCard):
    def __init__(self, reverse_type: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._reverse_type = reverse_type
        
    def reverse_type(self) -> str:
        return self._reverse_type
    
    def __str__(self) -> str:
        return super().__str__() + f' Reverse Type: {self.reverse_type()}'
