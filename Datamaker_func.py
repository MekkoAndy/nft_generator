import glob
from PIL import Image, ImageSequence


def get_folder_list(project_path):
    return [folder+'/' for folder in sorted(glob.glob(project_path+'*'))]


def data_maker(project_path):
    data_dict, random_limits = [], []
    folders = get_folder_list(project_path)
    for folder in folders:
        data_dict.append([])
        for img_counter, img in enumerate(sorted(glob.glob(folder + '*.*'))):
            image = Image.open(img)
            match image.format:
                case 'PNG':
                    new_image = image.convert('RGBA').resize((750, 750))
                    new_image = new_image
                    data_dict[-1].append([new_image for _ in range(60)])
                case 'GIF':
                    data_dict[-1].append([frame.convert('RGBA').resize((750, 750)) for frame in ImageSequence.Iterator(image)])
        random_limits.append(img_counter)

    return data_dict, folders, random_limits
