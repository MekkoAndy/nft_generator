import click
import os

from pathlib import Path
from tqdm import tqdm

from Datamaker import ContentMaker
from Metadata_maker_func import meta_maker
from Character_maker_func import character_maker
from Classes import *
from ClickWrappers import *


def path_exist(path: Path) -> bool:
    if path.exists():
        return path
    print(f"Intered path \n{path} \nis not found\n")
    breakpoint

def project_init() -> Project:
    # Greetings
    print("Welcome to Andy's Content Generator v.0.1.0")

    # don't forget about logs
    project = Project()
    

    ################
    # this name will be used for logs and folders creations
    project.name = str(input("Project name: "))

    # where the project should be saved
    project.path.main = path_exist(Path(input("Project path: ")))

    # where to get the asset for generation
    project.path.asset = path_exist(Path(input("Asset path: ")))

    # запустить инициализацию ассета
    project.content.attributes.layer_order: list[str] = ContentMaker(project).init()


    # content_attributes_asset_layering reordering
    project.content.attributes.layer_order: list[str] = ContentMaker(project).reorder(
        inquirer_prompt(
            Messenger.content_attributes_asset_layering
        )
    )


    ################
    # rarity data
    project.rarity.score_in_metadata: bool = inquirer_prompt_bool(Messenger.rarity_score_in_metadata)
    
    # rarity type
    project.rarity.type: RarityType = inquirer_prompt([type.value for type in RarityType], Messenger.rarity_type)

    # rarity extended mode
    project.rarity.score_extented_mode.full_random: bool = inquirer_prompt_bool(Messenger.rarity_score_full_random)


    ###############
    # rarity type
    project.metadata.type: MetadataType = inquirer_prompt([type.value for type in MetadataType], Messenger.metadata_type)


    ##############
    # messmodule cases amount
    project.mess_module.cases_amount: int = int(input(Messenger.mess_module_cases_amount))


    ##############
    # content_attributes_widht
    project.content.attributes.width: int = int(input(Messenger.content_attributes_width))

    # content_attributes_height
    project.content.attributes.height: int = int(input(Messenger.content_attributes_height))

    # content_attributes_compression
    project.content.attributes.compress: int = int(input(Messenger.content_attributes_compression))

    # content_attributes_total_amount
    project.content.attributes.total_generation_amount: int = int(input(Messenger.content_attributes_total_amount))

    # content_attributes_optimization
    project.content.attributes.optimize: bool = inquirer_prompt_bool(Messenger.content_attributes_optimization)


    # gif_attributes
    # if asset.type == "gif":
    project.content.attributes.gif_data.duration: int = int(input(Messenger.content_attributes_gif_duration))

    project.content.attributes.gif_data.frame_rate: int = int(input(Messenger.content_attributes_gif_framerate))

    project.content.attributes.gif_data.loop: bool = inquirer_prompt_bool(Messenger.content_attributes_gif_loop)


    return project

def generate_nft():
    project = project_init()

    make_directories(project=project)
    ContentMaker(project=project).prepare()

    validating_list = meta_maker(
        project_name=project.name,
        project_save_path=project.path.metadata,
        random_limits=project.content.asset.randomizer_limits,
        picture_limit=project.content.attributes.total_generation_amount,
        rare_picture_limit=rare_picture_limit,
        legendary_picture_limit=legendary_picture_limit,
        random_items_list=random_items_list,
        mess_module=True
    )

    for image_name, item_image_log in enumerate(tqdm(
                validating_list,
                ncols=100,
                desc="Generation progress")
    ):
        new_data_base = [
            data[i][item_image_log[i]-1]
            for i in range(len(folders_list))
            if item_image_log[i] != 0
        ]

        generated_nft = character_maker(new_data_base)
        generated_nft[0].save(
            project.path.generated+str(image_name)+'.gif',
            save_all=True,
            append_images=generated_nft,
            optimize=project.content_attributes.optimize,
            loop=project.content_attributes.gif_data.loop,
            duration=project.content_attributes.gif_data.duration
        )


def make_directories(project: Project) -> None:
    # TODO: rework this logic
    for _path in ["Generated/", "Metadata/"]:
        if not path_exist(_path):
            os.mkdir(os.path.join(project.path.main, _path))
    print("Folders created")
    project.path.metadata = os.path.join(project.path.main, "Metadata/")
    project.path.generated = os.path.join(project.path.main, "Generated/")
