import csv
import numpy as np


def log_writer(
        items_list,
        project_name,
        project_save_path,
        limiter,
        names_list,
        rarity_list,
        rarity_score,
        categorized_items_rarity_score
        ):
    list_for_save = [
        items_list,
        names_list,
        rarity_list,
        rarity_score,
        categorized_items_rarity_score
    ]

    rarity_types = [
        'common',
        'rare',
        'legendary'
    ]

    name_list_for_save = [
        'validating_list',
        'names_list',
        'rarity_list',
        'rarity_score',
        'categorized_items_rarity_score'
    ]

    with open(project_save_path+'items_log_'+project_name+'.csv', 'w', newline='') as csv_file:
        fieldnames = [
            'img-name',
            'rarity_mode',
            'items',
            'rarity_scores',
            'total_rarity_score'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for img_name in limiter:
            writer.writerow(
                {
                'img-name': names_list[img_name],
                'rarity_mode': rarity_types[rarity_list[img_name]],
                'items': items_list[img_name],
                'rarity_scores': rarity_score[img_name],
                'total_rarity_score': sum(rarity_score[img_name])
                }
            )

    with open(project_save_path+'categorized_rarity_scores'+project_name+'.csv', 'w', newline='') as csv_file:
        fieldnames = ['categorized_rarity_score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for category in categorized_items_rarity_score:
            writer.writerow({'categorized_rarity_score': category})

    [np.save(project_save_path+project_name+'_'+str(name_list_for_save[name])+'.npy',
             np.asarray(array_, dtype='object')) for name, array_ in enumerate(list_for_save)]
