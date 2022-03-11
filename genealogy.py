from tkinter import *
from tkinter import messagebox
from breedingforgui import Breed
from PIL import Image, ImageTk, ImageDraw
from familytreedata import Family, FamilyCat
import random
from resize import resize

family = Family()
root = Tk()
root.geometry("600x400")
root.title("Breed Cats")
root.configure(bg="pink")
windows = []
litters = []

breeding_windows = []
parentpassed = []

var1 = StringVar()
var2 = StringVar()

potentialparentnew = FamilyCat(0, 0, 0, 0, 1)
potentialparentnew.make_cat()
potentialparentnew.get_phenotype()
potentialparentnew.get_my_colors()
potentialparentnew.draw_me()

potentialparent1 = FamilyCat(0, 0, 0, 0, 1)
potentialparent1.make_cat()
potentialparent1.get_phenotype()
potentialparent1.get_my_colors()
potentialparent1.draw_me()

potentialparent2 = FamilyCat(0, 0, 0, 0, 1)
potentialparent2.make_cat()
potentialparent2.get_phenotype()
potentialparent2.get_my_colors()
potentialparent2.draw_me()
breed = Breed()

pic1 = potentialparent1.resizedimage
tkpic1 = ImageTk.PhotoImage(pic1)
var1.set(potentialparent1.sex)

pic2 = potentialparent2.resizedimage
tkpic2 = ImageTk.PhotoImage(pic2)
var2.set(potentialparent2.sex)


def breedcats(breed):
    if breed.parent1 is not None and breed.parent2 is not None:
        if breed.parent1.sex == breed.parent2.sex:
            messagebox.showwarning("Warning", "These two cats cannot breed")
        else:
            if breed.parent2 not in breed.parent1.mates:
                breed.parent1.mates.append(breed.parent2)
                breed.parent2.mates.append(breed.parent1)
                if breed.parent1.ifparent == 0 and breed.parent2.ifparent == 0:
                    family.generations.append([[]])
                    family.generations[0][0].append(breed.parent1)
                    family.generations[0][0].append(breed.parent2)
                else:
                    parent1indexes = family.check_cat_index(breed.parent1)
                    index = family.generations[parent1indexes[0]][parent1indexes[1]].index(breed.parent1)
                    family.generations[parent1indexes[0]][parent1indexes[1]].insert(index + 1, breed.parent2)
            breed.calculate_litter_size()
            breed.calculate_chances()
            breed.create_litter()
            if len(family.generations) < breed.parent1.generation + 1:
                family.generations.append([])
            if family.check_if_litters(breed.parent1):
                litterposition = family.determine_litter_position(breed.parent1)
            else:
                litterposition = 0
            family.generations[breed.parent1.generation].insert(litterposition, breed.litter.kittens)
            for i in range(0, breed.size):
                if breed.size == 1:
                    image1 = breed.litter.kittens[0].resizedbabyimage
                    image1.save("kittens.png")
                else:
                    if i == 1:
                        image1 = breed.litter.kittens[0].resizedbabyimage
                    else:
                        image1 = Image.open("kittens.png")
                    image2 = breed.litter.kittens[i].resizedbabyimage

                    (width1, height1) = image1.size
                    (width2, height2) = image2.size

                    result_width = width1 + width2
                    result_height = height1

                    result = Image.new('RGBA', (result_width, result_height))
                    result.paste(im=image1, box=(0, 0))
                    result.paste(im=image2, box=(width1, 0))
                    result.save("kittens.png")
            newWindow = Toplevel(root)
            newWindow.title("Litter")
            newWindow.configure(bg="pink")
            babies = Image.open("kittens.png")
            babies = ImageTk.PhotoImage(babies)
            babycats = Button(newWindow, image=babies, bg="light goldenrod",
                              command=lambda: breeding_passdata(newWindow.frame()))
            babycats.image = babies
            babycats.grid()
            windows.append(newWindow)
            litters.append(breed.litter)


def breeding_passdata(frame):
    for i in range(len(windows)):
        if windows[i].frame() == frame:
            breedingnextgen(litters[i])


def setparent1():
    breed.set_parent1(potentialparent1)


def setparent2():
    breed.set_parent2(potentialparent2)


def setparentnew(breednext):
    breednext.set_parent2(potentialparentnew)


def newparentnext(breednext, imglbl, txtlbl):
    breednext.remove_parent_2()
    newvar1 = StringVar()
    global potentialparentnew
    potentialparentnew = FamilyCat(0, 0, 0, 0, 1)
    potentialparentnew.make_cat()
    potentialparentnew.get_phenotype()
    potentialparentnew.get_my_colors()
    potentialparentnew.draw_me()
    newpic1 = potentialparentnew.resizedimage
    newtkpic1 = ImageTk.PhotoImage(newpic1)
    newvar1.set(potentialparentnew.sex)
    imglbl.configure(image=newtkpic1)
    imglbl.image = newtkpic1
    txtlbl.configure(textvariable=newvar1)


def newparent1():
    breed.remove_parent_1()
    newvar1 = StringVar()
    global potentialparent1
    potentialparent1 = FamilyCat(0, 0, 0, 0, 1)
    potentialparent1.make_cat()
    potentialparent1.get_phenotype()
    potentialparent1.get_my_colors()
    potentialparent1.draw_me()
    newpic1 = potentialparent1.resizedimage
    newtkpic1 = ImageTk.PhotoImage(newpic1)
    newvar1.set(potentialparent1.sex)
    label1.configure(image=newtkpic1)
    label1.image = newtkpic1
    label1a.configure(textvariable=newvar1)


def newparent2():
    breed.remove_parent_2()
    newvar2 = StringVar()
    global potentialparent2
    potentialparent2 = FamilyCat(0, 0, 0, 0, 1)
    potentialparent2.make_cat()
    potentialparent2.get_phenotype()
    potentialparent2.get_my_colors()
    potentialparent2.draw_me()
    newpic2 = potentialparent2.resizedimage
    newtkpic2 = ImageTk.PhotoImage(newpic2)
    newvar2.set(potentialparent2.sex)
    label2.configure(image=newtkpic2)
    label2.image = newtkpic2
    label2a.configure(textvariable=newvar2)


def create_image_test():
    size_y = 100 * (len(family.generations))
    biggestgen = 0
    for gen in family.generations:
        size = sum([len(x) for x in gen])
        if size > biggestgen:
            biggestgen = size
    size_x = 100 * biggestgen
    base = Image.new("RGBA", (size_x, size_y), (255, 255, 255, 0))
    height = 10
    omit = 0
    for generation in family.generations:
        width = 75 * (sum([len(x) for x in generation]))
        width += 15 * len(generation) - 1
        gaps = int((size_x - width) / 2)
        start = 3 + gaps
        for litter in generation:
            linestart = 0
            lineheight = 0
            for cat in litter:
                if litter.index(cat) == 0:
                    linestart = start + 32
                    lineheight = height - 15
                if generation == family.generations[-1]:
                    catimg = cat.babyimage
                    position = (19, 23)
                else:
                    catimg = cat.image
                    position = (0, 0)
                if cat.sex == "female" and cat.ifparent == 1:
                    background = Image.new("RGBA", (64, 64), (240, 120, 190, 255))
                elif cat.sex == "female" and cat.ifparent == 0:
                    background = Image.new("RGBA", (64, 64), (240, 180, 215, 255))
                elif cat.sex == "male" and cat.ifparent == 1:
                    background = Image.new("RGBA", (64, 64), (135, 185, 240, 255))
                else:
                    background = Image.new("RGBA", (64, 64), (180, 210, 240, 255))
                background.paste(catimg, position, mask=catimg)
                base.paste(im=background, box=(start, height))
                draw = ImageDraw.Draw(base)
                if cat.ifparent:
                    draw.line([(start + 32, height - 1), (start + 32, height - 15)], width=4, fill=(0, 0, 0, 255))
                else:
                    if not (generation == family.generations[0] and litter == generation[0] and litter.index(cat) == 0):
                        draw.line([(start - 10, height + 32), (start - 1, height + 32)], width=4, fill=(0, 0, 0, 255))

                start += 74
            start += 15
            draw = ImageDraw.Draw(base)
            parented = [x.ifparent for x in generation[-1]]
            parented = parented[::-1]
            for x in parented:
                if x:
                    break
                else:
                    omit += 1
            draw.line([(linestart - 2, lineheight), (start - 56 - (74 * omit), lineheight)], width=4,
                      fill=(0, 0, 0, 255))
            linestart2 = ((linestart - 2) + (start - 56 - (74 * omit))) / 2
            draw.line([(linestart2, lineheight - 15), (linestart2, lineheight)], width=4, fill=(0, 0, 0, 255))
            omit = 0
        height += 100
    base = resize(base)
    base.save("tree.png")
    base.show()


def breedcats_topass(frame):
    for i in range(len(breeding_windows)):
        if breeding_windows[i].frame() == frame:
            breedcats(parentpassed[i])


def breedingnextgen(litter):
    parentfixed = random.choice(litter.kittens)
    breednext = Breed()
    breednext.set_parent1(parentfixed)
    newWindow2 = Toplevel(root)
    newWindow2.title("Next Generation")
    newWindow2.configure(bg="SkyBlue")
    newWindow2.geometry("600x400")
    img1 = parentfixed.resizedimage
    img1 = ImageTk.PhotoImage(img1)
    parentfixedimage = Label(newWindow2, image=img1, bg="SkyBlue")
    parentfixedimage.image = img1
    var1 = StringVar()
    var1.set(parentfixed.sex)
    parentfixedsexlabel = Label(newWindow2, textvariable=var1)
    tkpic2 = ImageTk.PhotoImage(potentialparentnew.resizedimage)
    var2 = StringVar()
    var2.set(potentialparentnew.sex)
    label2 = Label(newWindow2, image=tkpic2, bg="SkyBlue")
    label2.image = tkpic2
    label2a = Label(newWindow2, textvariable=var2)

    B2 = Button(newWindow2, text="set parent", command=lambda: setparentnew(breednext))
    B2a = Button(newWindow2, text="new", command=lambda: newparentnext(breednext, label2, label2a))
    breeding_windows.append(newWindow2)
    parentpassed.append(breednext)
    breedbutton = Button(newWindow2, text="breed", command=lambda: breedcats_topass(newWindow2.frame()))

    parentfixedimage.grid(row=0)
    parentfixedsexlabel.grid(row=1)

    breedbutton.grid(column=1)

    label2.grid(row=0, column=2)
    label2a.grid(row=1, column=2)
    B2.grid(row=2, column=2)
    B2a.grid(row=3, column=2)


label1 = Label(root, image=tkpic1, bg="pink")
label1a = Label(root, textvariable=var1)
B1 = Button(root, text="set parent", command=setparent1)
B1a = Button(root, text="new", command=newparent1)

label2 = Label(root, image=tkpic2, bg="pink")
label2a = Label(root, textvariable=var2)
B2 = Button(root, text="set parent", command=setparent2)
B2a = Button(root, text="new", command=newparent2)

breedbutton = Button(root, text="breed", command=lambda: breedcats(breed))
treebutton = Button(root, text="tree", command=lambda: create_image_test())

label1.grid(row=0)
label1a.grid(row=1)
B1.grid(row=2)
B1a.grid(row=3)

breedbutton.grid(row=1, column=1)
treebutton.grid(row=2, column=1)

label2.grid(row=0, column=2)
label2a.grid(row=1, column=2)
B2.grid(row=2, column=2)
B2a.grid(row=3, column=2)

root.mainloop()
