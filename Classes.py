import enum

from dataclasses import dataclass
from pathlib import Path
from PIL import Image


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
    width: int
    height: int
    gif_data: GifMetadata
    layer_order: list[str]
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
class ProjectHierarchy:
    main: Path
    asset: Path
    generated: Path
    metadata: Path


@dataclass
class AssetImage:
    name: str
    data: Image
    rarity_idx: int

@dataclass
class AssetFolder:
    name: str
    data: [AssetImage]
    exclude_combination: list[int]

@dataclass
class AssetData:
    data: list[AssetFolder]
    randomizer_limits: list[int]

@dataclass
class Content:
    asset: AssetData
    attributes: ContentAttributes


@dataclass
class Project:
    name: str
    path: ProjectHierarchy
    rarity: Rarity
    metadata: Metadata
    mess_module: MessModule
    content: Content


@dataclass
class Messenger:
    rarity_score_in_metadata = "Include rarity score in nft's metadata? "
    rarity_type = "Choose rarity hierarchy: "
    rarity_score_full_random = "Include rarity score in nft's metadata? "
    metadata_type = "Choose metadata format: "
    mess_module_cases_amount = "Отвечает за упорядочивание сложной структуры проекта. Если есть исключающие друг друга слои или итемы, нужно модуль включить и заполнить. Inter Amount of mess-cases to proceed"
    content_attributes_width = "NFT's width. Input 0 for no changes: "
    content_attributes_height = "NFT's height. Input 0 for no changes: "
    content_attributes_compression = "NFT's compression in %. Input 0 for no changes: "
    content_attributes_total_amount = "NFT's total amount to generate: "
    content_attributes_optimization = "NFT's optimization: "
    content_attributes_gif_duration = "GIF duration"
    content_attributes_gif_framerate = "GIF framerate"
    content_attributes_gif_loop = "GIF looping"
    content_attributes_asset_layering = f"Inter a sequence of asset layers wich will be used in image composing. New assets layer order:"
