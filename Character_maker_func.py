from PIL import Image


# scil - some_character_items_list one random item for each category
def character_maker(s_c_i_l):
    layer = s_c_i_l[0]
    for idx in range(len(s_c_i_l)-1):
        layer = layer_compositer(layer, s_c_i_l[idx+1])
    
    return layer


def layer_compositer(base_layer, top_layer):
    return [Image.alpha_composite(base_layer[frame_idx], top_layer[frame_idx]) for frame_idx in range(60)]

