"""
C - количество категорий --> [0, ..., C]
A - asset folder
P - item inside A
w - weight
T - text config for metadata

M = {
    "A": [("P", w), ..., ("P", w)], 
    ...,
    "A": [("P", w), ..., ("P", w)]
}

for category in C[1:]:
    for A in assets:
        _ = int(input([P, ..., P]))
        for inputed_item in _:
            M["A"] = 

{
    1:
        {
        "background": ["bg_1", "bg_2", "bg_9"],
        "eyes": ["open", "closed"],
        "mouth": ["smiling", "neutral", "frowning"],
        "accessories": ["hat", "sunglasses", "earrings"]
        },
    2:
        {
        "background": ["bg_1", "bg_2", "bg_9"],
        "eyes": ["open", "closed"],
        "mouth": ["smiling", "neutral", "frowning"],
        "accessories": ["hat", "sunglasses", "earrings"]
        },
        
}

def prepare_metadata(total_to_generate, categories_amount, assets_amount, part_amount):

"""

import random
"""
# Define the possible traits for each category, along with their weights
trait_categories = {
    "background": [("red", 10), ("green", 5), ("blue", 1)],
    "eyes": [("open", 7), ("closed", 3)],
    "mouth": [("smiling", 5), ("neutral", 3), ("frowning", 2)],
    "accessories": [("hat", 4), ("sunglasses", 3), ("earrings", 2)]
}

# Define the number of NFTs to generate
num_nfts = 30

# Generate the NFTs
for i in range(num_nfts):
    nft = {}
    for category, traits in trait_categories.items():
        # Randomly select a trait from the possible options, based on the weights
        nft[category] = random.choices([trait[0] for trait in traits], [trait[1] for trait in traits])[0]

    print(nft)
"""

def generate_rarity_list(pic_limit, rare_count, legendary_count):
    # Generate the list of all possible picture names
    all_names = list(range(pic_limit))

    # Generate the list of rare and legendary picture names
    rare_names = random.sample(all_names, rare_count + legendary_count)
    legendary_names = random.sample(rare_names, legendary_count)
    rare_names = [name for name in rare_names if name not in legendary_names]

    # Generate the rarity list
    rarity_list = []
    for name in all_names:
        rarity_list.append(get_rarity_category(name, rare_names))

    return rarity_list

def get_rarity_category(name, rare_names):
    if name in rare_names:
        return 1
    else:
        return 0

print(generate_rarity_list(1000, 50, 10))