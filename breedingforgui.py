from newcat import NewCat
from litterclass import Litter


class Breed:
    def __init__(self):
        self.parent1 = None
        self.parent2 = None
        self.chances = None
        self.size = None
        self.litter = None
        self.kitten = None

    def set_parent1(self, catforparent):
        self.parent1 = catforparent

    def set_parent2(self, catforparent):
        self.parent2 = catforparent

    def remove_parent_1(self):
        self.parent1 = None

    def remove_parent_2(self):
        self.parent2 = None

    def calculate_chances(self):
        import copy
        parent1traits = self.parent1.traits
        parent2traits = self.parent2.traits
        allpossible = []
        if self.parent1.sex == "male":
            for a in range(len(parent1traits)):
                allpossible.append([])
                for i in parent2traits[a]:
                    for n in parent1traits[a]:
                        allpossible[a].append(''.join(sorted(i + n)))
        if self.parent1.sex == "female":
            for a in range(len(parent1traits)):
                allpossible.append([])
                for i in parent1traits[a]:
                    for n in parent2traits[a]:
                        allpossible[a].append(''.join(sorted(i + n)))

        for i in range(len(allpossible)):
            allpossible[i] = sorted(allpossible[i])

        correctedpossible = copy.deepcopy(allpossible)
        for i in range(len(allpossible)):
            for n in range(len(allpossible[i]) - 1):

                if allpossible[i][n] == allpossible[i][n + 1]:
                    correctedpossible[i].remove(allpossible[i][n])

        def fix_list(lista):
            slownik = {"Bb": "Bb", "'Bb": "Bb'", "BB": "BB", "bb": "bb", "'bb": "bb'", "''bb": "b'b'", "DDmm": "DmDm",
                       "Ddmm": "Dmdm", "ddmm": "dmdm", "TTam": "TaTm", "TTaa": "TaTa",
                       "TTmm": "TmTm", "Tabt": "Tatb", "Tbmt": "Tmtb", "bbtt": "tbtb", "WWdd": "WdWd", "WWds": "WdWs",
                       "Wdgw": "Wdwg", "WWss": "WsWs", "Wsw": "Wsw", "Wdw": "Wdw",
                       "Wgsw": "Wswg", "ww": "ww", "gww": "wgw", "ggww": "wgwg", "CC": "CC", "Ccs": "Ccs", "Cbc": "Ccb",
                       "Cac": "Cca", "Cc": "Cc", "ccss": "cscs", "bccs": "cscb", "accs": "csca",
                       "ccs": "csc", "bbcc": "cbcb", "abcc": "cbca", "bcc": "cbc", "aacc": "caca", "acc": "cac",
                       "cc": "cc"}

            naprawa1 = lista[1]
            for i in range(len(lista[1])):
                naprawa1[i] = slownik[naprawa1[i]]
            lista[1] = naprawa1

            naprawa4 = lista[4]
            for i in range(len(lista[4])):
                naprawa4[i] = slownik[naprawa4[i]]
            lista[4] = naprawa4

            naprawa6 = lista[6]
            for i in range(len(lista[6])):
                naprawa6[i] = slownik[naprawa6[i]]
            lista[6] = naprawa6

            naprawa7 = lista[7]
            for i in range(len(lista[7])):
                naprawa7[i] = slownik[naprawa7[i]]
            lista[7] = naprawa7

            naprawa8 = lista[8]
            for i in range(len(lista[8])):
                naprawa8[i] = slownik[naprawa8[i]]
            lista[8] = naprawa8

            return lista

        correctedpossible = fix_list(correctedpossible)

        possiblewithpercentages = []

        for i in range(10):
            possiblewithpercentages.append([])
            templist = []
            for n in correctedpossible[i]:
                templist.append([n, 100 / len(correctedpossible[i])])
            possiblewithpercentages[i] = templist
        self.chances = possiblewithpercentages

    def calculate_litter_size(self):
        import random
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        weights = [0.155, 0.183, 0.212, 0.199, 0.127, 0.059, 0.021, 0.006, 0.001, 0.0003, 0.00005, 0.00001]
        self.size = random.choices(numbers, weights)
        self.size = self.size[0]

    def show_chances(self):
        for i in range(len(self.chances)):
            print(self.chances[i])

    def create_litter(self):
        self.litter = Litter(self.size)
        for i in range(self.size):
            traits = get_kitten_traits(self.chances)
            self.litter.kittens[i].make_cat_from_passed(traits)
            self.litter.kittens[i].get_phenotype()
            self.litter.kittens[i].get_my_colors()
            self.litter.kittens[i].draw_me()
            self.litter.kittens[i].draw_baby()
            self.litter.kittens[i].ifparent = 1
            if self.parent1.sex == "female":
                self.litter.kittens[i].mom = self.parent1
                self.litter.kittens[i].dad = self.parent2
            else:
                self.litter.kittens[i].mom = self.parent2
                self.litter.kittens[i].dad = self.parent1
            self.litter.kittens[i].generation = self.parent1.generation+1


    def show_parents(self):
        return self.parent1.resizedimage, self.parent2.resizedimage


def get_kitten_traits(possible):
    import random
    traits = []
    for i in possible:
        pick = random.choice(i)
        pick = pick[0]
        traits.append(pick)
    if traits[0] == "XY":
        mod = traits[2]
        mod = mod[1:]
        traits[2] = mod
    for i in range(len(traits)):
        if len(traits[i]) == 2:
            string = traits[i]
            n = 1
            out = [(string[i:i + n]) for i in range(0, len(string), n)]
            traits[i] = out
        if len(traits[i]) == 3:
            aaa = traits[i]
            if aaa[1] == "'":
                string = traits[i]
                n = 2
                out = [(string[i:i + n]) for i in range(0, len(string), n)]
                traits[i] = out
            elif aaa[2] == "'":
                string = traits[i]
                n = 1
                out = [(string[i:i + n]) for i in range(0, len(string), n)]
                out[1] = out[1] + out[2]
                out.pop(2)
                traits[i] = out
            else:
                if "C" not in traits[i][0]:
                    string = traits[i]
                    n = 2
                    out = [(string[i:i + n]) for i in range(0, len(string), n)]
                    traits[i] = out
                else:
                    string = traits[i]
                    n = 1
                    out = [(string[i:i + n]) for i in range(0, len(string), n)]
                    out[1] = out[1] + out[2]
                    out.pop(2)
                    traits[i] = out
        if len(traits[i]) == 4:
            string = traits[i]
            n = 2
            out = [(string[i:i + n]) for i in range(0, len(string), n)]
            traits[i] = out
    return traits
