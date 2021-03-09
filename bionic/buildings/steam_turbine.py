"""Steam turbine class"""
from typing import Dict

from bionic.dataclasses import Element
from bionic.dataclasses.entity import Entity

STEAM = Element("Steam", 4.179)
WATER = Element("Water", 4.179)


class SteamTurbine:
    """Steam turbine class"""

    name: str = "Steam Turbine"
    heat: float = 4

    def process(self, entity_dict: Dict[str, Entity]):
        """Process elements"""
        steam_key = "steam"
        water_key = "water"
        max_amount = 2000
        if steam_key not in entity_dict:
            return
        steam_entity = entity_dict[steam_key]
        if steam_entity.temperature < 125:
            return
        if water_key not in entity_dict:
            entity_dict[water_key] = Entity(WATER, 0, 95)
        if steam_entity.mass <= max_amount:
            entity_dict[water_key].mass += steam_entity.mass
            entity_dict.pop(steam_key)
        else:
            entity_dict[water_key].mass += max_amount
            entity_dict[steam_key].mass -= max_amount
