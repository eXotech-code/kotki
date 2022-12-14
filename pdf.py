import copy
from reportlab.lib.pagesizes import A4, inch
from reportlab.lib.utils import ImageReader
from PIL import Image as IMG
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

size_w, size_h = A4
size = (int(size_w * 1.5), int(size_h * 1.5))

# Fonts
pdfmetrics.registerFont(TTFont("fontLight", "Roboto-Light.ttf"))
pdfmetrics.registerFont(TTFont("fontRegular", "Roboto-Regular.ttf"))


def trait_table_pdf(generations):
    elements = []
    img = ImageReader("smalltree.png")
    img_h, img_w = img.getSize()
    w, h = size
    if check_if_fits(img_h, img_w, h, w) == 1:
        elements.append(Image("smalltree.png"))
    elif check_if_fits(img_w, img_h, h, w) == 1:
        im = IMG.open("smalltree.png")
        angle = 90
        out = im.rotate(angle, expand=True)
        out.save("smalltree_rotated.png")
        elements.append(Image("smalltree_rotated.png"))
    else:
        print("unable to add image: tree too large")
    traits = [["ID", "PŁEĆ", "EU", "PH", "DEN", "DMOD", "AG", "TAB", "WH", "TYR", "FL"]]
    for gen in generations:
        for litter in gen:
            for cat in litter:
                temp = copy.deepcopy([",".join(sorted(x)) for x in cat.traits])
                temp.insert(0, cat.id)
                traits.append(temp)
    doc = SimpleDocTemplate("tree_doc.pdf", pagesize=size)

    # container for the 'Flowable' objects
    data = traits
    t = Table(data, len(data[0]) * [0.7 * inch], len(data) * [0.4 * inch])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "fontRegular"),
        ("FONTNAME", (1, 1), (-1, -1), "fontLight"),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.pink),
        ("LINEABOVE", (0, 1), (-1, 1), 1, colors.black),
        ("BOX", (0, 0), (-1, -1), 1, colors.black)
    ]))
    space = Spacer(100, 50)
    elements.append(space)
    elements.append(t)
    # write the document to disk
    doc.build(elements)


def check_if_fits(height, width, ph, pw):
    ph *= 0.75
    pw *= 0.75
    result = 0
    if height <= ph and width <= pw:
        result = 1
    elif height <= pw and width <= ph:
        result = 2
    return result
