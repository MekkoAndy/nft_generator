from dataclasses import dataclass
from pathlib import Path
import enum


class RarityType(enum.Enum):
    standart = ("Common", "Mythic", "Legendary")
    extended = ("Common", "Uncommon", "Rare", "Mythic", "Legendary")


class MetadataType(enum.Enum):
    standart: str = "json"
    self_hosted: str = "php"


@dataclass
class ExcludeCombinations:
    asset_layer: str
    asset_layer_part: str


@dataclass
class MessModule:
    cases_amount: int = 0


@dataclass
class RarityScoreExtendedMode:
    asset_layer: str
    asset_layer_part: str
    full_random: bool = True
    

@dataclass
class GifMetadata:
    frame_rate: int = 0
    loop: bool = False
    duration: int = 0


@dataclass
class ContentAttributes:
    widht: int
    height: int
    gif_data: GifMetadata
    total_generation_amount: int = 0
    compress: int = 0
    optimize: bool = False


@dataclass
class Rarity:
    type: RarityType
    score_extented_mode: RarityScoreExtendedMode
    score_in_metadata: bool = False


@dataclass
class Metadata:
    type: MetadataType


@dataclass
class ProjectMetadada():
    name: str
    path: Path
    asset_path: Path
    rarity: Rarity
    metadata: Metadata
    mess_module: MessModule
    content_attributes: ContentAttributes


@dataclass
class Messenger:
    rarity_score_in_metadata = "Include rarity score in nft's metadata? "
    rarity_type = "Choose rarity hierarchy: "
    rarity_score_full_random = "Include rarity score in nft's metadata? "
    metadata_type = "Choose metadata format: "
    mess_module_cases_amount = "Отвечает за упорядочивание сложной структуры проекта. Если есть исключающие друг друга слои или итемы, нужно модуль включить и заполнить. Inter Amount of mess-cases to proceed"
    content_attributes_widht = "NFT's widht. Input 0 for no changes: "
    content_attributes_height = "NFT's height. Input 0 for no changes: "
    content_attributes_compression = "NFT's compression in %. Input 0 for no changes: "
    content_attributes_total_amount = "NFT's total amount to generate: "
    content_attributes_optimization = "NFT's optimization: "
    content_attributes_gif_duration = "GIF duration"
    content_attributes_gif_framerate = "GIF framerate"
    content_attributes_gif_loop = "GIF looping"
