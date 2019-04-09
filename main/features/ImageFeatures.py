from utils import utils


def image_presence(post):
    """
    Checks if the post contains an image
    :param post: the current post
    :return: 1 if the post contains an image, else 0
    """
    im = utils.img(post)

    if im is None:
        return 0
    else:
        return 1
