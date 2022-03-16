from PIL import Image


def resize(image):
    im = image
    width, height = im.size
    im = im.resize((width * 4, height * 4), resample=Image.NEAREST)
    return im


def resizetwice(image):
    im = image
    width, height = im.size
    im = im.resize((width * 2, height * 2), resample=Image.NEAREST)
    return im
