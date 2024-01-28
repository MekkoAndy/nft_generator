from Datamaker import data_maker
from Metadata_maker_func import meta_maker
from Character_maker_func import character_maker
from Classes import *
from ClickWrappers import *

from pathlib import Path
from tqdm import tqdm
import click
import os


def path_exist(hint: str) -> Path:
    path_to_check = Path(input(hint))
    if path_to_check.exists():
        return path_to_check
    print("Intered path not found\n")
    path_exist(hint)

def project_init() -> ProjectMetadada:
    # Greetings
    print("Welcome to Andy's Content Generator v.0.1.0")

    # don't forget about logs
    project = ProjectMetadada()
    

    ################
    # this name will be used for logs and folders creations
    project.name = str(input("Project name: "))

    # where the project should be saved
    project.path = path_exist("Project path: ")

    # where to get the asset for generation
    project.asset_path = path_exist("Asset path: ")

    # запустить инициализацию ассета

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
    project.content_attributes.widht: int = int(input(Messenger.content_attributes_widht))

    # content_attributes_height
    project.content_attributes.height: int = int(input(Messenger.content_attributes_height))

    # content_attributes_compression
    project.content_attributes.compress: int = int(input(Messenger.content_attributes_compression))

    # content_attributes_total_amount
    project.content_attributes.total_generation_amount: int = int(input(Messenger.content_attributes_total_amount))

    # content_attributes_optimization
    project.content_attributes.optimize: bool = inquirer_prompt_bool(Messenger.content_attributes_optimization)

    # gif_attributes
    # if asset.type == "gif":
    project.content_attributes.gif_data.duration: int = int(input(Messenger.content_attributes_gif_duration))

    project.content_attributes.gif_data.frame_rate: int = int(input(Messenger.content_attributes_gif_framerate))

    project.content_attributes.gif_data.loop: bool = inquirer_prompt_bool(Messenger.content_attributes_gif_loop)

    return project

def generate_nft():
    project = project_init()
    project_items_path, save_picture_path, save_metadata_path = dir_maker(
        project_name=project_name,
        path=main_path,
        make_dirs=make_dirs
    )

    data, folders_list, random_limits = data_maker(
        project_path=project_items_path
        )if process_data else breakpoint()

    validating_list = meta_maker(
        project_name=project_name,
        project_save_path=save_metadata_path,
        random_limits=random_limits,
        picture_limit=picture_limit,
        rare_picture_limit=rare_picture_limit,
        legendary_picture_limit=legendary_picture_limit,
        random_items_list=random_items_list,
        mess_module=mess_module
    ) if prepare_metadata else breakpoint()

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

        char_done = character_maker(new_data_base) if launch_generation else breakpoint()
        char_done[0].save(
            save_picture_path+str(image_name)+'.gif',
            save_all=True,
            append_images=char_done,
            optimize=False,
            loop=0,
            duration=84
        )


def dir_maker(project_name, path, make_dirs):
    project_path = os.path.join(path, project_name)
    project_items_path = os.path.join(project_path, 'Parts/')
    save_picture_path = os.path.join(project_path, 'Generated/')
    save_metadata_path = os.path.join(project_path, 'Metadata/')
    if make_dirs:
        [os.mkdir(folder) for folder in [
            project_path,
            project_items_path,
            save_picture_path,
            save_metadata_path]]

    return project_items_path, save_picture_path, save_metadata_path
