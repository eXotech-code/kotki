from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from PIL import Image


def check_if_fits(height, width, ph, pw):
    result = 0
    if height <= ph and width <= pw:
        result = 1
    elif height <= pw and width <= ph:
        result = 2
    return result


def create_pdf():
    w, h = A4
    c = canvas.Canvas("tree.pdf", pagesize=A4)
    # Place the logo in the upper left corner.
    img = ImageReader("smalltree.png")
    # Get the width and height of the image.
    img_w, img_h = img.getSize()
    if check_if_fits(img_h, img_w, h, w) == 1:
        c.drawImage(img, 0, h - img_h)
    elif check_if_fits(img_h, img_w, h, w) == 2:
        im = Image.open("smalltree.png")
        angle = 90
        out = im.rotate(angle, expand=True)
        out.save("smalltree_rotated.png")
        img = ImageReader("smalltree_rotated.png")
        c.drawImage(img, 50, 50)
    else:
        print("unable to create pdf: tree too large")
    c.showPage()
    c.save()
