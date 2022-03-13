from newcat import NewCat


class Family:
    def __init__(self):
        self.generations = []

    def check_cat_index(self, cat):
        indexes = []
        for gen in range(len(self.generations)):
            for litter in range(len(self.generations[gen])):
                if cat in self.generations[gen][litter]:
                    indexes = [gen, litter]
        return indexes

    def check_if_litters(self, parent):
        result = 0
        if not self.generations[parent.generation]:
            result = 1
        return result

    def compare_cat_indexes(self, cat1, cat2):
        result = 0
        indexes = self.check_cat_index(cat1)
        if cat2 in self.generations[indexes[0]][indexes[1]]:
            index1 = self.generations[indexes[0]][indexes[1]].index(cat1)
            index2 = self.generations[indexes[0]][indexes[1]].index(cat2)
            if index1 < index2:
                result = "left"
            else:
                result = "right"
        return result

    def determine_litter_position(self, parent):
        position = 'start'
        generation = self.generations[parent.generation]
        for litter in generation:
            if litter:
                if litter[0].ifparent:
                    cat2 = litter[0].dad
                    check = self.compare_cat_indexes(parent, cat2)
                    if check == "left":
                        position = generation.index(litter)
                        break
            else:
                position = generation.index(litter)
        if position == 'start':
            position = len(generation)
        return position


class FamilyCat(NewCat):
    def __init__(self, ifparent, mom, dad, mate, generation):
        self.ifparent = ifparent
        self.mom = mom
        self.dad = dad
        if mate != 0:
            self.mates = [mate]
        else:
            self.mates = []
        self.generation = generation
        self.id = 0
        self.traits = []
        self.sex = 0
        self.eumelanin = 0
        self.phaeomelanin = 0
        self.dense = 0
        self.dilutionmod = 0
        self.agouti = 0
        self.tabby = 0
        self.white = 0
        self.tyrosine = 0
        self.furlength = 0
        self.phenotype = 0
        self.basecolor = []
        self.shadowcolor1 = []
        self.shadowcolor2 = []
        self.eyecolor1 = []
        self.eyecolor2 = []
        self.nosecolor = []
        self.mouthcolor = []
        self.whiskercolor = []
        self.tabbycolor = []
        self.tortiecolor = []
        self.spotscolor = []
        self.whichspots = []
        self.whichareas = []
        self.pointcolor = []
        self.coatpattern = ""
        self.coatcolor = ""
        self.image = None
        self.babyimage = None
        self.babyeyes = []
        self.resizedimage = None
        self.resizedbabyimage = None
