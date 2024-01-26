import random as rnd

# заменить на словарь, чтобы обращаться по ключу
def rarity_randomizer(pic_limit, limit_rare, limit_legendary):
    limiter = range(pic_limit)
    common_list = [c for c in limiter]
    leg_list = []
    r_t = sorted(rnd.sample(limiter, limit_rare + limit_legendary))
    [common_list.remove(i) for i in r_t]
    l_t = sorted(rnd.sample(range(len(r_t)), limit_legendary))
    [leg_list.append(r_t[i]) for i in l_t]
    [r_t.remove(i) for i in leg_list]
    rarity_list = []
    for name in limiter:
        if name in common_list: rarity_cat = 0
        elif name in r_t: rarity_cat = 1
        else: rarity_cat=2
        rarity_list.append(rarity_cat)

    return rarity_list
