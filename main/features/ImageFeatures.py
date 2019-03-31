from main.utils import utils
# TODO: maybe change that to a module


class ImageFeatures:

    def __init__(self):
        print("Image related features")

    def image_presence(self, post):

        im = utils.img(post)

        if im is None:
            return 0
        else:
            return 1
