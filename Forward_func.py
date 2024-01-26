from Datamaker_func import data_maker
from Metadata_maker_func import meta_maker
from Character_maker_func import character_maker
from tqdm import tqdm
import os


def forward(
        project_name,
        main_path,
        random_items_list,
        picture_limit,
        rare_picture_limit,
        legendary_picture_limit,
        make_dirs,
        process_data,
        prepare_metadata,
        launch_generation,
        mess_module
):
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
