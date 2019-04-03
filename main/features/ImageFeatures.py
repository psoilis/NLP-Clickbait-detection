from utils import utils


def image_presence(post):
    im = utils.img(post)

    if im is None:
        return 0
    else:
        return 1
