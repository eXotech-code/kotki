from newcat import NewCat


class Family:
    def __init__(self):
        self.generations = []
        self.gennumber = 0


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
