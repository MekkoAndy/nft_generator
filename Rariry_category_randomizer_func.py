import random as rnd

""" TODO:
import random

# Define the possible traits for each category, along with their weights
trait_categories = {
    "background": [("red", 10), ("green", 5), ("blue", 1)],
    "eyes": [("open", 7), ("closed", 3)],
    "mouth": [("smiling", 5), ("neutral", 3), ("frowning", 2)],
    "accessories": [("hat", 4), ("sunglasses", 3), ("earrings", 2)]
}

# Define the number of NFTs to generate
num_nfts = 10

# Generate the NFTs
for i in range(num_nfts):
    nft = {}
    for category, traits in trait_categories.items():
        # Randomly select a trait from the possible options, based on the weights
        nft[category] = random.choices([trait[0] for trait in traits], [trait[1] for trait in traits])[0]
    print(nft)
"""
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
