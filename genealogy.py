#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from breedingforgui import Breed
from PIL import Image, ImageTk, ImageDraw
from familytreedata import Family, FamilyCat, bundle_litters
import random
from resize import resize
from pdf import create_pdf

family = Family()
litters = []
parentpassed = []


# Create root window and setup functions for creating and manipulating
# other windows.

# Class repsonsible for controlling all currently open windows.
class WindowSpace:
    def __init__(self):
        self.root_window = Window(self, 0)
        self.windows = []
        self.litter_windows = []

    def start(self):
        self.get_root_window_obj().mainloop()

    # Create a new window and add it to the list.
    # 0 is root window, 1 is normal window and 2 is litter window.
    def instantiate(self, win_type=1):
        win_list = self.windows

        # Create a new window and append it to the list of windows.
        # Return its address in the corresponding list.
        if win_type == 2:
            win_list = self.litter_windows
        win_list.append(Window(self, win_type))
        return len(win_list) - 1

    # Closes specified window and removes it from the list.
    def close(self, window):
        # Check if this is the litter window or normal and remove
        if window.get_type() == 1:
            self.windows.remove(window)
        elif window.get_type() == 2:
            self.litter_windows.remove(window)

        window.get_win_obj().destroy()

    def get_root_window_obj(self):
        return self.root_window.get_win_obj()

    def get_n_windows(self):
        return self.windows

    def get_l_windows(self):
        return self.litter_windows

    # Get window frame at index.
    def get_n_frame_at_i(self, i):
        return self.windows[i].get_frame()

    def get_l_frame_at_i(self, i):
        return self.litter_windows[i].get_frame()


# A window class responsible for litter windows and parent windows.
class Window:
    def __init__(self, parent, win_type):
        self.parent = parent

        # Definitions of attributes for different types of windows.
        at_lst = [
            ["Breed Cats", "pink", "600x400"],  # Root window
            ["Next Generation", "SkyBlue", "600x400"],  # Parent windows (normal)
            ["Litter", "pink"]  # Litter windows
        ]

        self.ty = win_type
        self.win = self.create(*at_lst[win_type])
        self.win.protocol("WM_DELETE_WINDOW", lambda window=self: parent.close(window))

    def create(self, title, color, size=0):
        # If this is the root window, instantiate it via Tk class.
        if self.ty == 0:
            win = Tk()
        else:
            win = Toplevel(self.parent.get_root_window_obj())

        win.title(title)
        win.configure(bg=color)
        if size:
            win.geometry(size)

        return win

    def get_frame(self):
        return self.win.frame()

    def get_win_obj(self):
        return self.win

    def get_type(self):
        return self.ty


window_space = WindowSpace()

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
    im = Image.new("RGBA", (0, 0))
    if breed.parent1 is not None and breed.parent2 is not None:
        if breed.parent1.sex == breed.parent2.sex:
            messagebox.showwarning("Warning", "These two cats cannot breed")
        else:
            if breed.parent2 not in breed.parent1.mates:
                breed.parent1.mates.append(breed.parent2)
                breed.parent2.mates.append(breed.parent1)
                if breed.parent1.ifparent == 0 and breed.parent2.ifparent == 0:
                    if len(breed.parent1.mates) == 1 and len(breed.parent2.mates) == 1:
                        family.generations.append([[]])
                        family.generations[0][0].append(breed.parent1)
                        family.generations[0][0].append(breed.parent2)
                    elif len(breed.parent1.mates) != 1:
                        family.generations[0][0].append(breed.parent2)
                    else:
                        family.generations[0][0].append(breed.parent1)
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
            family.generations[breed.parent1.generation].insert(litterposition + 1, breed.litter.kittens)
            if breed.size == 1:
                image1 = breed.litter.kittens[0].resizedbabyimage
                image1.save("kittens.png")
            else:
                for i in range(0, breed.size):
                    if i == 0:
                        image1 = breed.litter.kittens[0].resizedbabyimage
                        image1.save("kittens.png")
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
            # Create a new window and save the index in list.
            new_window_i = window_space.instantiate(2)
            new_window = window_space.get_l_windows()[new_window_i].get_win_obj()
            babies = Image.open("kittens.png")
            babies = ImageTk.PhotoImage(babies)
            babycats = Button(new_window, image=babies, bg="light goldenrod",
                              command=lambda: breeding_passdata(window_space.get_l_frame_at_i(new_window_i)))
            babycats.image = babies
            babycats.grid()
            litters.append(breed.litter)


def breeding_passdata(frame):
    windows = window_space.get_l_windows()
    for i in range(len(windows)):
        if windows[i].get_frame() == frame:
            breedingnextgen(litters[i])


# Root window
def setparent1():
    breed.set_parent1(potentialparent1)


# Breed window
def setparent2():
    breed.set_parent2(potentialparent2)


def setparentnew(breednext):
    breednext.set_parent2(potentialparentnew)


def newparentnext(breednext, imglbl, txtlbl, parent2sex):
    breednext.remove_parent_2()
    newvar1 = StringVar()
    global potentialparentnew
    potentialparentnew = FamilyCat(0, 0, 0, 0, 1)
    potentialparentnew.make_cat_set_sex(parent2sex)
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


# LINE CALCULATIONS ----------------------
def calculate_line_up(cat):
    start = (cat.x_pos, cat.y_pos - 33)
    end = (cat.x_pos, cat.y_pos - 48)
    result = (start, end)
    return result


class LineSpace:
    def __init__(self, base_img):
        self.lines = []
        self.base_img = base_img
        self.draw = ImageDraw.Draw(base_img).line

    # Based on if if you pass mates or bundle to this function
    # it will create lines connecting bundles or mates.
    def add_line(self, new_line):
        new_line.set_draw_func(self.draw)
        self.lines.append(new_line)
        return new_line.get_coords()  # This is used by ConnectsAll class.

    def draw_lines(self):
        for line in self.lines:
            line.draw()


# Class that respresents one line. It has properties responsible for
# values that get passed to the Pillow line drawing function.
class Line:
    def __init__(self, color, beg=(0, 0), end=(0, 0)):
        self.beg = beg  # (x, y)
        self.end = end  # (x, y)
        self.color = color  # (r, g, b, a)
        print(self.color)
        self.pill_draw = None  # The draw line function from pillow

    def set_draw_func(self, func):
        self.pill_draw = func

    def get_coords(self):
        return self.beg, self.end

    def draw(self):
        self.pill_draw(self.beg, self.end, 4, self.color)


class ConnectsBundle(Line):
    def __init__(self, bundle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bundle = bundle
        self.beg, self.end = self.calculate_line_st_en()

    def calculate_line_st_en(self):
        if self.bundle[0][0].generation == 1:
            result = ((0, 0), (0, 0))
        else:
            first_cat = self.bundle[0][0]
            last_litter = self.bundle[-1]
            last_litter_parented = [x.ifparent for x in last_litter]
            last_litter_parented = last_litter_parented[::-1]
            omit = 0
            for i in last_litter_parented:
                if not i:
                    omit += 1
                else:
                    break
            last_cat = last_litter[-1 - omit]
            start = (first_cat.x_pos, first_cat.y_pos - 48)
            end = (last_cat.x_pos, last_cat.y_pos - 48)
            result = (start, end)
        return result


class ConnectsMates(Line):
    def __init__(self, cat1, cat2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent1 = cat1
        self.parent2 = cat2
        self.beg, self.end = self.calculate_line_st_en()

    def calculate_line_st_en(self):
        direction = family.compare_cat_indexes(self.parent1, self.parent2)
        if direction == "left":
            start = (self.parent2.x_pos - 32, self.parent2.y_pos)
            end = (self.parent2.x_pos - 62, self.parent2.y_pos)
        else:
            start = (self.parent1.x_pos - 32, self.parent1.y_pos)
            end = (self.parent1.x_pos - 62, self.parent1.y_pos)
        result = (start, end)
        return result


# Makes a composite of three lines that together connect
# parents to a bundle.
class ParentsOffspringCn:
    def __init__(self, line_space, coords):
        self.line_space = line_space
        self.coords = coords
        self.lines = []
        self.make()

    def make(self):
        for coord in self.coords:
            line = Line((0, 0, 0, 255), *coord)
            self.lines.push(line)
            # Push a line to line_space
            self.line_space.add_line(line)


class ConnectsAll:
    def __init__(self, line_space, bundle):
        self.bundle = bundle
        self.line_space = line_space
        # Create lines and save their coords
        self.bundle_coords = line_space.add_line(ConnectsBundle(self.bundle, (0, 0, 0, 255)))
        self.mate_coords = line_space.add_line(ConnectsMates(self.bundle[0][0].dad, self.bundle[0][0].mom, (0, 0, 0, 255)))
        self.gen_connecting_line()

    def calculate_conn_line(self):
        bundle_horizontal_start, bundle_horizontal_end = self.bundle_coords
        mate_line_start, mate_line_end = self.mate_coords
        bundle_line_start, height1 = bundle_horizontal_start
        bundle_line_end, *rest = bundle_horizontal_end
        bundle_middle = int((bundle_line_start, bundle_line_end) / 2)
        mate_start, height2 = mate_line_start
        mate_end, *rest = mate_line_end
        mate_middle = int((mate_start, mate_end) / 2)
        first_vertical_line = ((bundle_middle, height1), (bundle_middle, height1 - 15))
        horizontal_line = ((bundle_middle, height1 - 15), (mate_middle, height1 - 15))
        second_vertical_line = ((mate_middle, height1 - 15), (mate_middle, height2))
        result = (first_vertical_line, horizontal_line, second_vertical_line)
        return result

    def gen_connecting_line(self):
        coords = self.calculate_conn_line()
        connecting_line = ParentsOffspringCn(self.line_space, coords)
        connecting_line.make()


def create_image_cats():
    family.bundle()
    size_y = 150 * (len(family.generations))
    lengths = []
    for gen in family.generations:
        size = sum([len(x) for x in gen])
        lengths.append(size)
    biggestgen = max(lengths)
    longestgens = [x for x in family.generations if lengths[family.generations.index(x)] == biggestgen]
    secondary_sizing = []
    for longgen in longestgens:
        bundled_gen = bundle_litters(longgen)
        secondary_sizing.append(len(bundled_gen))
    bundlesinbiggestgen = max(secondary_sizing)
    biggestgen += int(bundlesinbiggestgen / 4)
    size_x = 100 * biggestgen
    base = Image.new("RGBA", (size_x, size_y), (255, 255, 200, 255))
    line_space = LineSpace(base)
    height = 10
    omit = 0
    for generation in family.generations:
        catnumber = (sum([len(x) for x in generation]))
        litternumber = len(generation)
        width = 64 * catnumber
        width += 30 * (catnumber - 1)
        width += 15 * (litternumber - 1)
        generation_bundled = bundle_litters(generation)
        width += 25 * (len(generation_bundled) - 1)  # +15 For each bundle gap.
        gaps = int((size_x - width) / 2)
        start = gaps
        for bundle in generation_bundled:
            for litter in bundle:
                # lineheight = 0
                # linestart = 0
                for cat in litter:
                    cat.x_pos = start + 32
                    cat.y_pos = height + 32
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
                    # else:
                    #     if not (generation == family.generations[0] and litter == generation[0] and litter.index(
                    #             cat) == 0):
                    #         draw.line([(start - 26, height + 32), (start - 1, height + 32)], width=4,
                    #                   fill=(0, 0, 0, 255))

                    start += 94
                start += 15
                # draw = ImageDraw.Draw(base)
                # parented = [x.ifparent for x in litter]
                # parented = parented[::-1]
                # for x in parented:
                #     if x:
                #         break
                #     else:
                #         omit += 1
                # draw.line([(linestart - 2, lineheight), (start - 72 - (90 * omit), lineheight)], width=4,
                #           fill=(0, 0, 0, 255))
                # linestart2 = ((linestart - 2) + (start - 72 - (90 * omit))) / 2
                # draw.line([(linestart2, lineheight - 15), (linestart2, lineheight)], width=4, fill=(0, 0, 0, 255))
                # omit = 0
            ConnectsAll(line_space, bundle)
            start += 25
        height += 150
    base.save("smalltree.png")
    base = resize(base)
    base.save("tree.png")
    base.show()
    create_pdf()


def breedcats_topass(frame):
    breeding_windows = window_space.get_n_windows()

    for i in range(len(breeding_windows)):
        if breeding_windows[i].get_frame() == frame:
            breedcats(parentpassed[i])


def breedingnextgen(litter):
    parentfixed = random.choice(litter.kittens)
    breednext = Breed()
    breednext.set_parent1(parentfixed)
    parent2sex = []
    if parentfixed.sex == "female":
        parent2sex = ["X", "Y"]
    else:
        parent2sex = ["X", "X"]

    new_window_i = window_space.instantiate(1)
    new_window = window_space.get_n_windows()[new_window_i].get_win_obj()

    img1 = parentfixed.resizedimage
    img1 = ImageTk.PhotoImage(img1)
    global potentialparentnew
    potentialparentnew = FamilyCat(0, 0, 0, 0, parentfixed.generation)
    potentialparentnew.make_cat_set_sex(parent2sex)
    potentialparentnew.get_phenotype()
    potentialparentnew.get_my_colors()
    potentialparentnew.draw_me()
    breednext.set_parent2(potentialparentnew)

    parentfixedimage = Label(new_window, image=img1, bg="SkyBlue")
    parentfixedimage.image = img1
    var1 = StringVar()
    var1.set(parentfixed.sex)
    parentfixedsexlabel = Label(new_window, textvariable=var1)
    tkpic2 = ImageTk.PhotoImage(potentialparentnew.resizedimage)
    var2 = StringVar()
    var2.set(potentialparentnew.sex)
    label2 = Label(new_window, image=tkpic2, bg="SkyBlue")
    label2.image = tkpic2
    label2a = Label(new_window, textvariable=var2)

    B2 = Button(new_window, text="set parent", command=lambda: setparentnew(breednext))
    B2a = Button(new_window, text="new", command=lambda: newparentnext(breednext, label2, label2a, parent2sex))
    parentpassed.append(breednext)
    breedbutton = Button(new_window, text="breed",
                         command=lambda: breedcats_topass(window_space.get_n_frame_at_i(new_window_i)))

    parentfixedimage.grid(row=0)
    parentfixedsexlabel.grid(row=1)

    breedbutton.grid(column=1)

    label2.grid(row=0, column=2)
    label2a.grid(row=1, column=2)
    B2.grid(row=2, column=2)
    B2a.grid(row=3, column=2)


label1 = Label(window_space.get_root_window_obj(), image=tkpic1, bg="pink")
label1a = Label(window_space.get_root_window_obj(), textvariable=var1)
B1 = Button(window_space.get_root_window_obj(), text="set parent", command=setparent1)
B1a = Button(window_space.get_root_window_obj(), text="new", command=newparent1)

label2 = Label(window_space.get_root_window_obj(), image=tkpic2, bg="pink")
label2a = Label(window_space.get_root_window_obj(), textvariable=var2)
B2 = Button(window_space.get_root_window_obj(), text="set parent", command=setparent2)
B2a = Button(window_space.get_root_window_obj(), text="new", command=newparent2)

breedbutton = Button(window_space.get_root_window_obj(), text="breed", command=lambda: breedcats(breed))
treebutton = Button(window_space.get_root_window_obj(), text="tree", command=lambda: create_image_cats())

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

window_space.start()
