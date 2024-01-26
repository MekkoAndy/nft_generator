import numpy as np


def rarity_score_checker(limits, validating_list, pic_limit):
    categories = [[] for _ in range(len(limits))]
    categorized_items_rarity_score, rarity_score = [], []

    for image_log in validating_list:
        for number, category in enumerate(image_log):
            categories[number].append(category)

    for category_num, each_category in enumerate(categories):
        categorized_items_rarity_score.append([])
        for each_unique_item in np.unique(each_category):
            categorized_items_rarity_score[category_num].append(
                [each_category.count(each_unique_item),
                 round(1/(each_category.count(each_unique_item)/pic_limit))]
            )

    for picture in validating_list:
        rarity_score.append([])
        for category, item in enumerate(picture):
            score_value = categorized_items_rarity_score[category][item - 1][1] \
                if len(categorized_items_rarity_score[category]) == limits[category] \
                else categorized_items_rarity_score[category][item][1]
            rarity_score[-1].append(score_value)

    return categorized_items_rarity_score, rarity_score
