import glob

from PIL import Image, ImageSequence

from ClickWrappers import *
from Classes import *


class ContentMaker:
    def __init__(self, project: Project):
        self.project = project

    def init(self) -> list[str]:
        folders = []
        
        for folder in sorted(glob.glob(self.project.path.asset+'*')):
            folders.append(folder+"/")

        print("Current sorted asset layers:")
        print(folders, sep="\n")
        
        return folders
        
    def reorder(self, asset_layer_order: list[int]) -> list[str]:
        new_asset_layers = []
        
        for idx in asset_layer_order:
            new_asset_layers.append(self.project.content.attributes.layer_order[idx])
        
        print(new_asset_layers, sep="\n")
        
        return new_asset_layers
    
    def prepare(self) -> None:
        
        resize = tuple(self.project.content.attributes.width, self.project.content.attributes.height)

        for folder in glob.glob(self.project.content.attributes.layer_order + '*'):
                
            for img_counter, img_data in enumerate(glob.glob(f'{self.project.path.asset}/{folder}"*.*"')):
                
                image = Image.open(img_data)
                _asset_image = AssetImage
                
                if hasattr(image, 'filename'):
                    # save just a tailname, not fullpath name
                    _asset_image.name = image.filename
                else:
                    _asset_image.name = img_counter

                match image.format:
                    case 'PNG':
                        _asset_image.data = image.convert('RGBA').resize(size=resize)
                    case 'GIF':
                        _asset_image.data = [frame.convert('RGBA').resize(size=resize) for frame in ImageSequence.Iterator(image)]
                    case _:
                        print(f'Not supported picture format {image.format}. Please, contact the developer @mdasdot')
                        breakpoint

                self.project.content.asset.data.append(_asset_image)

            self.project.content.asset.randomizer_limits.append(img_counter)


    def compose(self):
        pass


    def save(self):
        pass
