import json
from schemas import PokemonCard, ReverseHolo
from errors import InvalidSetName
     
class CardData:
    def __init__(self, data: dict) -> None:
        self._data = data
 
    @classmethod
    def load(cls, filepath: str) -> "CardData":
        
        json_dict: dict = {}
        set_dict: dict = {}
        
        with open(filepath, 'r', encoding='utf-8') as json_file:
            json_dict = json.load(json_file)
            
        for set_name, cards in json_dict.items():
            set_dict[set_name] = []      
            for card in cards:
                if card['is_reverse']:
                    pokecard = ReverseHolo(**card)
                else:   
                    pokecard = PokemonCard(**card)
                    
                set_dict[set_name].append(pokecard)
                
        return cls(set_dict)
        
    def all_cards(self) -> dict:
        return self._data
    
    def search_by_set(self, set_name: str) -> list[PokemonCard]:
        cards = self.all_cards().get(set_name.upper(), None)
        if cards is None:
            raise InvalidSetName("No cards from this set registered to database.")
        
        return cards
    
    def set_names(self) -> list:
        return list(self._data.keys())
        
    def search_by_name(self, pokemon_name: str) -> list:     
        valid_cards = []
        for set_name in self.set_names():
            cards = self.search_by_set(set_name)
            for card in cards:
                if pokemon_name.lower() not in card.name().lower():
                    continue
                
                valid_cards.append(card)
                
        return valid_cards
    
    def search(self, search_type: str, search_filter: str) -> list:
        return self.search_by_name(search_filter) if search_type == "NAME" else self.search_by_set(search_filter)
    
cards = CardData.load('C:/projects/pokemon-bulk-tracker/source_file.json')
