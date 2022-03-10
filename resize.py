def resize(image):
    import numpy as np
    from PIL import Image

    im = image
    width, height = im.size
    im = im.resize((width*4, height*4), resample=Image.NEAREST)
    return im
