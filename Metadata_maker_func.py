from Rariry_category_randomizer_func import rarity_randomizer
from Picture_item_generator_func import item_generator
from Rarityscore_maker_func import rarity_score_checker
from Metadata_saver_func import log_writer
import random as rnd


def meta_maker(
        project_name,
        project_save_path,
        random_limits,
        picture_limit,
        rare_picture_limit,
        legendary_picture_limit,
        random_items_list,
        mess_module
):
    random_limits_for_count = [limit+1 for limit in random_limits]
    limiter_list = list(range(picture_limit))
    validating_list, rarity_list, names_list = [], [], []
    print(random_limits_for_count)
    print(sum(random_limits_for_count))

    rarity_list = rarity_randomizer(
        pic_limit=picture_limit,
        limit_rare=rare_picture_limit,
        limit_legendary=legendary_picture_limit
    )

    while len(limiter_list) > 0:
        freeze_random = item_generator(
            r_i_l=random_items_list,
            lori=[rnd.randint(1, i) for i in random_limits_for_count],
            name=limiter_list[0],
            rarity_list=rarity_list,
            mess_module=mess_module
        )

        if freeze_random not in validating_list:
            validating_list.append(freeze_random)
            names_list.append(limiter_list[0])
            limiter_list.remove(limiter_list[0])

    categorized_items_rarity_score, rarity_score = rarity_score_checker(
        limits=random_limits_for_count,
        validating_list=validating_list,
        pic_limit=picture_limit
    )

    log_writer(
        items_list=validating_list,
        project_name=project_name,
        project_save_path=project_save_path,
        limiter=range(picture_limit),
        names_list=names_list,
        rarity_list=rarity_list,
        rarity_score=rarity_score,
        categorized_items_rarity_score=categorized_items_rarity_score
    )

    return validating_list
