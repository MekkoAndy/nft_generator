from Mess_module_func import mess_func


def item_generator(r_i_l, lori, name, rarity_list, mess_module):  # list_of_random_items
    if mess_module:
        lori = mess_func(lori)

    return sub_worker_for_item_generator(lori, r_i_l[rarity_list[name]])


def sub_worker_for_item_generator(lori, list_of_zeros):
    return [0 if i in list_of_zeros else lori[i] for i in range(len(lori))] if list_of_zeros else lori
