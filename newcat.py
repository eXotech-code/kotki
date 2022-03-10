class NewCat:
    def __init__(self):
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

    def make_cat_from_passed(self, traits):
        self.traits = traits
        self.sex = traits[0]
        self.eumelanin = traits[1]
        self.phaeomelanin = traits[2]
        self.dense = traits[3]
        self.dilutionmod = traits[4]
        self.agouti = traits[5]
        self.tabby = traits[6]
        self.white = traits[7]
        self.tyrosine = traits[8]
        self.furlength = traits[9]

    def make_cat(self):
        import random
        sex = ["X", "Y"]
        sex_picked = ["X"]
        eumelanin = ["B", "b", "b'"]
        eumelanin_picked = []
        phaeomelanin = ["O", "o"]
        phaeomelanin_picked = []
        dense = ["D", "d"]
        dense_picked = []
        dilutionmodifier = ["Dm", "dm", "dm", "dm", "dm", "dm"]
        dilutionmodifier_picked = []
        agouti = ["A", "a"]
        agouti_picked = []
        tabby = ["Ta", "Tm", "tb"]
        tabby_picked = []
        white = ["Wd", "Ws", "w", "wg"]
        white_picked = []
        tyrosine = ["C", "cb", "cs", "ca", "c"]
        tyrosine_picked = []
        furlength = ["L", "l"]
        furlength_picked = []
        traits = []
        randomnumber = random.randint(0, 1)
        sex_picked.append(sex[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 2)
            eumelanin_picked.append(eumelanin[randomnumber])
        if "Y" in sex_picked:
            randomnumber = random.randint(0, 1)
            phaeomelanin_picked.append(phaeomelanin[randomnumber])
        else:
            for i in range(2):
                randomnumber = random.randint(0, 1)
                phaeomelanin_picked.append(phaeomelanin[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 1)
            dense_picked.append(dense[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 5)
            dilutionmodifier_picked.append(dilutionmodifier[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 1)
            agouti_picked.append(agouti[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 2)
            tabby_picked.append(tabby[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 3)
            if randomnumber == 0:
                randomnumber = random.randint(0, 3)
            white_picked.append(white[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 4)
            tyrosine_picked.append(tyrosine[randomnumber])
        for i in range(2):
            randomnumber = random.randint(0, 1)
            furlength_picked.append(furlength[randomnumber])
        traits.append(sex_picked)
        traits.append(eumelanin_picked)
        traits.append(phaeomelanin_picked)
        traits.append(dense_picked)
        traits.append(dilutionmodifier_picked)
        traits.append(agouti_picked)
        traits.append(tabby_picked)
        traits.append(white_picked)
        traits.append(tyrosine_picked)
        traits.append(furlength_picked)
        self.traits = traits
        self.sex = traits[0]
        self.eumelanin = traits[1]
        self.phaeomelanin = traits[2]
        self.dense = traits[3]
        self.dilutionmod = traits[4]
        self.agouti = traits[5]
        self.tabby = traits[6]
        self.white = traits[7]
        self.tyrosine = traits[8]
        self.furlength = traits[9]

    def get_phenotype(self):
        self.coatpattern = ""
        if "Y" in self.sex:
            self.sex = "male"
        else:
            self.sex = "female"
        if "Wd" in self.white or self.tyrosine == ["ca", "ca"] or self.tyrosine == ["c", "c"]:
            self.coatcolor = "white"
        else:
            # not white
            if self.sex == "male" and "O" in self.phaeomelanin:
                self.coatcolor = "red"
            else:
                if self.sex == "female" and "O" in self.phaeomelanin:
                    if "B" in self.eumelanin:
                        self.coatcolor = "red and black"
                    else:
                        if "b" in self.phaeomelanin:
                            self.coatcolor = "red and chocolate"
                        else:
                            self.coatcolor = "red and cinnamon"
                else:
                    # not red
                    if "B" in self.eumelanin:
                        self.coatcolor = "black"
                    else:
                        if "b" in self.eumelanin:
                            self.coatcolor = "chocolate"
                        else:
                            self.coatcolor = "cinnamon"
                # modifiers - density, dilution mod
                if self.dense == ["d", "d"]:
                    if self.coatcolor == "black":
                        self.coatcolor = "blue"
                    if self.coatcolor == "chocolate":
                        self.coatcolor = "lilac"
                    if self.coatcolor == "cinnamon":
                        self.coatcolor = "fawn"
                    if self.coatcolor == "red":
                        self.coatcolor = "cream"
                    if "Dm" in self.dilutionmod:
                        if self.coatcolor == "blue":
                            self.coatcolor = "blue based caramel"
                        if self.coatcolor == "lilac":
                            self.coatcolor = "lilac based caramel"
                        if self.coatcolor == "fawn":
                            self.coatcolor = "fawn based caramel"
                        if self.coatcolor == "cream":
                            self.coatcolor = "apricot"
                if self.tyrosine == ["cb", "cb"]:
                    self.coatcolor = self.coatcolor + " sepia"
                if self.tyrosine == ["cs", "cb"] or self.tyrosine == ["cb", "cs"]:
                    self.coatcolor = self.coatcolor + " mink"
                if self.tyrosine == ["cs", "cs"]:
                    self.coatcolor = self.coatcolor + " colorpoint"
        # get pattern
        if self.coatcolor == "White" or (("and" not in self.coatcolor) and (
                self.coatcolor not in ["Red", "Cream", "Apricot", "Red sepia", "Red mink", "Red colorpoint",
                                       "Cream sepia",
                                       "Cream mink", "Cream colorpoint", "Apricot sepia", "Apricot mink",
                                       "Apricot colorpoint"]) and self.agouti == ["a", "a"]):
            self.coatpattern = "solid"
        else:
            if "and" in self.coatcolor:
                self.coatpattern = " tortoiseshell"
            if "Tm" in self.tabby or "Ta" in self.tabby:
                if self.tabby == ["Ta", "Ta"] or ("Ta" in self.tabby and "tb" in self.tabby):
                    self.coatpattern = self.coatpattern + "tabby (ticked)"
                if self.tabby == ["Ta", "Tm"] or self.tabby == ["Tm", "Ta"]:
                    self.coatpattern = self.coatpattern + "tabby (ticked, mackerel)"
                if self.tabby == ["Tm", "Tm"] or ("Tm" in self.tabby and "tb" in self.tabby):
                    self.coatpattern = self.coatpattern + "tabby (mackerel)"
            else:
                self.coatpattern = self.coatpattern + "tabby( classic)"
        # get info about white
        if "Ws" in self.white and self.coatcolor != "White":
            if self.white == ["Ws", "Ws"]:
                self.white = [50, 100]
            else:
                self.white = [0, 50]
        if self.white == ["w", "w"] or self.white == ["w", "wg"] or self.white == ["wg", "w"]:
            self.white = [0]
        if self.white == ["wg", "wg"]:
            self.white = [200]
        # fur length
        if self.furlength == ["l", "l"]:
            self.furlength = "long"
        else:
            self.furlength = "short"
        self.phenotype = [self.coatcolor, self.coatpattern, self.white, self.furlength]

    def get_my_colors(self):
        import random
        if self.basecolor == []:
            black = [[[28], [52]], [[21], [21]], [[19], [19]]]
            chocolate = [[[81], [105]], [[36], [50]], [[26], [26]]]
            cinnamon = [[[153], [156]], [[69], [89]], [[24], [24]]]
            blue = [[[81], [144]], [[64], [139]], [[81], [139]]]
            lilac = [[[119], [197]], [[114], [190]], [[126], [182]]]
            fawn = [[[205], [220]], [[190], [211]], [[173], [198]]]
            bluecaramel = [[[107], [186]], [[74], [161]], [[61], [161]]]
            lilaccaramel = [[[133], [206]], [[109], [190]], [[96], [171]]]
            fawncaramel = [[[217], [231]], [[191], [213]], [[161], [188]]]
            red = [[[207], [235]], [[77], [184]], [[2], [30]]]
            cream = [[[243], [254]], [[200], [228]], [[169], [180]]]
            apricot = [[[238], [241]], [[161], [210]], [[68], [95]]]
            white = [[[240], [250]], [[238], [238]], [[238], [251]]]
            blueeyes = [[24, 196, 195], [94, 236, 235], [67, 153, 153], [45, 79, 175], [77, 188, 253], [77, 122, 253],
                        [45, 79, 175]]
            yelloweyes = [[191, 218, 2], [232, 253, 77], [232, 193, 77], [240, 226, 12], [240, 247, 12], [233, 194, 12],
                          [233, 161, 72]]
            coppereyes = [[253, 209, 77], [253, 143, 77], [236, 147, 94], [236, 147, 31], [236, 168, 31],
                          [216, 137, 31],
                          [216, 101, 31]]
            browneyes = [[109, 41, 1], [163, 60, 1], [163, 101, 52], [132, 64, 72], [98, 44, 12], [87, 47, 23],
                         [50, 47, 23]]
            greeneyes = [[94, 236, 129], [2, 21, 36], [100, 253, 77], [2, 218, 55], [1, 109, 27], [45, 175, 77],
                         [62, 175, 45]]
            redeyes = [[200, 130, 157], [218, 112, 114], [200, 130, 131], [236, 94, 96], [253, 77, 79]]
            nosecolors = [[14, 21, 19], [60, 21, 19], [158, 69, 24], [189, 117, 81], [241, 199, 200], [242, 146, 103]]

            sepia = 0
            mink = 0
            colorpoint = 0
            color = self.coatcolor

            if "sepia" in color:
                sepia = 1
                color = color.replace(" sepia", "")
            if "mink" in color:
                mink = 1
                color = color.replace(" mink", "")
            if "colorpoint" in color:
                colorpoint = 1
                color = color.replace(" colorpoint", "")
            if "and" in color:
                color = color.split(" ")
                color = color[2]
            if color == "black":
                if "tabby" in self.coatpattern:
                    color = "blue based caramel"
                else:
                    color = "black"
            if color == "black":
                color = black
            if color == "chocolate":
                color = chocolate
            if color == "cinnamon":
                color = cinnamon
            if color == "blue":
                color = blue
            if color == "lilac":
                color = lilac
            if color == "fawn":
                color = fawn
            if color == "blue based caramel":
                color = bluecaramel
            if color == "lilac based caramel":
                color = lilaccaramel
            if color == "fawn based caramel":
                color = fawncaramel
            if color == "red":
                color = red
            if color == "cream":
                color = cream
            if color == "apricot":
                color = apricot
            if color == "white":
                color = white
            if colorpoint == 1:
                colorsaved = color
                color = fawn
            startRange = color[0][0][0]
            endRange = color[0][1][0]
            randomnumber = random.randint(startRange, endRange)
            redbase = randomnumber
            distanceinred = color[0][1][0] - color[0][0][0]
            distanceingreen = color[1][1][0] - color[1][0][0]
            distanceinblue = color[2][1][0] - color[2][0][0]
            newdistancered = redbase - color[0][0][0]
            if distanceinred == 0:
                distanceinred = 1
            factorofdistance = newdistancered / distanceinred
            newdistancegreen = int(distanceingreen * factorofdistance)
            greenbase = color[1][0][0] + newdistancegreen
            newdistanceblue = int(distanceinblue * factorofdistance)
            bluebase = color[2][0][0] + newdistanceblue
            if sepia == 1:
                redbase = redbase + 20
                greenbase = greenbase + 20
                bluebase = bluebase + 20
                if redbase > 255:
                    redbase = 255
                if greenbase > 255:
                    greenbase = 255
                if bluebase > 255:
                    bluebase = 255
            if mink == 1:
                fawndistancered = (fawn[0][1][0] - redbase) / 2
                fawndistancered = int(fawndistancered)
                redbasesaved = redbase
                redbase = redbase + fawndistancered
                fawndistancegreen = (fawn[1][1][0] - greenbase) / 2
                fawndistancegreen = int(fawndistancegreen)
                greenbasesaved = greenbase
                greenbase = greenbase + fawndistancegreen
                fawndistanceblue = (fawn[2][1][0] - bluebase) / 2
                fawndistanceblue = int(fawndistanceblue)
                bluebasesaved = bluebase
                bluebase = bluebase + fawndistanceblue
                if redbase > 255:
                    redbase = 255
                if greenbase > 255:
                    greenbase = 255
                if bluebase > 255:
                    bluebase = 255

            colorforbase = [redbase, greenbase, bluebase]
            colorforshadow1 = [int(redbase * 0.8), int(bluebase * 0.8), int(greenbase * 0.8)]
            colorforshadow2 = [int(redbase * 0.5), int(bluebase * 0.5), int(greenbase * 0.5)]
            # eye 1 and 2
            randomnumber2 = random.randint(0, 6)
            eye2color = yelloweyes[randomnumber2]
            babyeye = blueeyes[randomnumber2]
            self.babyeyes = babyeye
            if colorpoint == 1:
                randomnumber2 = random.randint(0, 6)
                eye2color = blueeyes[randomnumber2]
            else:
                if color == white:
                    randomnumber1 = random.randint(0, 10)
                    if randomnumber1 == 0:
                        randomnumber2 = random.randint(0, 4)
                        eye2color = redeyes[randomnumber2]
                    else:
                        randomnumber3 = random.randint(0, 5)
                        if randomnumber3 == 0 or randomnumber3 == 1:
                            randomnumber2 = random.randint(0, 6)
                            eye2color = blueeyes[randomnumber2]
                        if randomnumber3 == 2:
                            randomnumber2 = random.randint(0, 6)
                            eye2color = yelloweyes[randomnumber2]
                        if randomnumber3 == 3:
                            randomnumber2 = random.randint(0, 6)
                            eye2color = coppereyes[randomnumber2]
                        if randomnumber3 == 4:
                            randomnumber2 = random.randint(0, 6)
                            eye2color = greeneyes[randomnumber2]
                        if randomnumber3 == 5:
                            randomnumber2 = random.randint(0, 6)
                            eye2color = browneyes[randomnumber2]
                else:
                    randomnumber1 = random.randint(0, 5)
                    if randomnumber1 == 0 or randomnumber1 == 1:
                        randomnumber2 = random.randint(0, 6)
                        eye2color = yelloweyes[randomnumber2]
                    if randomnumber1 == 2 or randomnumber1 == 3:
                        randomnumber2 = random.randint(0, 6)
                        eye2color = greeneyes[randomnumber2]
                    if randomnumber1 == 4:
                        randomnumber2 = random.randint(0, 6)
                        eye2color = coppereyes[randomnumber2]
                    if randomnumber1 == 5:
                        randomnumber2 = random.randint(0, 6)
                        eye2color = browneyes[randomnumber2]

            if color == black or color == chocolate or color == cinnamon or color == blue:
                randomnum = random.randint(0, 1)
                nosecolor = nosecolors[randomnum]
            if color == bluecaramel or color == lilaccaramel or color == lilac or color == red or color == apricot:
                randomnum = random.randint(0, 5)
                nosecolor = nosecolors[randomnum]
            if color == white or color == cream or color == fawn or color == fawncaramel:
                randomnum = random.randint(4, 5)
                nosecolor = nosecolors[randomnum]
            mouthcolor = nosecolor
            if color == black or color == chocolate or color == cinnamon or color == blue or color == red or color == bluecaramel:
                whiskercolor = [14, 21, 19]
            else:
                whiskercolor = [253, 252, 247]
            eye1color = [eye2color[0] + 40, eye2color[1] + 40, eye2color[2] + 40]
            if eye1color[0] > 255:
                eye1color[0] = 255
            if eye1color[1] > 255:
                eye1color[1] = 255
            if eye1color[2] > 255:
                eye1color[2] = 255
            # getting colors for patterns that get passed
            tortiecolorreturn1 = [0]
            if "tortoiseshell" in self.coatpattern:
                if "caramel" in self.coatcolor:
                    randomnumber = random.randint(apricot[0][0][0], apricot[0][1][0])
                    redbase1 = randomnumber
                    distanceinred1 = apricot[0][1][0] - apricot[0][0][0]
                    distanceingreen1 = apricot[1][1][0] - apricot[1][0][0]
                    distanceinblue1 = apricot[2][1][0] - apricot[2][0][0]
                    newdistancered1 = redbase1 - apricot[0][0][0]
                    if distanceinred1 == 0:
                        distanceinred1 = 1
                    factorofdistance1 = newdistancered1 / distanceinred1
                    factorofdistance1 = abs(factorofdistance1)
                    newdistancegreen1 = int(distanceingreen1 * factorofdistance1)
                    greenbase1 = apricot[1][0][0] + newdistancegreen1
                    newdistanceblue1 = int(distanceinblue1 * factorofdistance1)
                    bluebase1 = apricot[2][0][0] + newdistanceblue1
                    tortiecolorreturn1 = [redbase1 + 20, greenbase1, bluebase1]
                    if redbase1 + 20 > 255:
                        tortiecolorreturn1[0] = 255
                if "blue" in self.coatcolor or "lilac" in self.coatcolor or "fawn" in self.coatcolor:
                    randomnumber = random.randint(cream[0][0][0], cream[0][1][0])
                    redbase1 = randomnumber
                    distanceinred1 = cream[0][1][0] - cream[0][0][0]
                    distanceinred1 = abs(distanceinred1)
                    distanceingreen1 = cream[1][1][0] - cream[1][0][0]
                    distanceingreen1 = abs(distanceingreen1)
                    distanceinblue1 = cream[2][1][0] - cream[2][0][0]
                    distanceinblue1 = abs(distanceinblue1)
                    newdistancered1 = redbase1 - cream[0][0][0]
                    if distanceinred1 == 0:
                        distanceinred1 = 1
                    factorofdistance1 = newdistancered1 / distanceinred1
                    factorofdistance1 = abs(factorofdistance1)
                    newdistancegreen1 = int(distanceingreen1 * factorofdistance1)
                    greenbase1 = cream[1][0][0] + newdistancegreen1
                    newdistanceblue1 = int(distanceinblue1 * factorofdistance1)
                    bluebase1 = cream[2][0][0] + newdistanceblue1
                    tortiecolorreturn1 = [redbase1 + 20, greenbase1, bluebase1]
                    if redbase1 + 20 > 255:
                        tortiecolorreturn1[0] = 255
                if "black" in self.coatcolor or "chocolate" in self.coatcolor or "cinnamon" in self.coatcolor:
                    randomnumber = random.randint(red[0][0][0], red[0][1][0])
                    redbase1 = randomnumber
                    distanceinred1 = red[0][1][0] - red[0][0][0]
                    distanceinred1 = abs(distanceinred1)
                    distanceingreen1 = red[1][1][0] - red[1][0][0]
                    distanceingreen1 = abs(distanceingreen1)
                    distanceinblue1 = red[2][1][0] - red[2][0][0]
                    distanceinblue1 = abs(distanceinblue1)
                    newdistancered1 = redbase1 - red[0][0][0]
                    if distanceinred1 == 0:
                        distanceinred1 = 1
                    factorofdistance1 = newdistancered1 / distanceinred1
                    factorofdistance1 = abs(factorofdistance1)
                    newdistancegreen1 = int(distanceingreen1 * factorofdistance1)
                    greenbase1 = red[1][0][0] + newdistancegreen1
                    newdistanceblue1 = int(distanceinblue1 * factorofdistance1)
                    bluebase1 = red[2][0][0] + newdistanceblue1
                    tortiecolorreturn1 = [redbase1 + 20, greenbase1, bluebase1]
                    if redbase1 + 20 > 255:
                        tortiecolorreturn1[0] = 255
            else:
                tortiecolorreturn1 = [0]
            # tabby stripes color
            if "tabby" in self.coatpattern:
                reddis = int(abs((colorforbase[0] - 14) / 4))
                newred = 14 + reddis
                greendis = int(abs((colorforbase[1] - 21) / 4))
                newgreen = 21 + greendis
                bluedis = int(abs((colorforbase[2] - 19) / 4))
                newblue = 19 + bluedis
                tabbycolorreturn = [newred, newgreen, newblue]
            else:
                tabbycolorreturn = [0]

            if self.white != [0]:
                randomnumber = random.randint(white[0][0][0], white[0][1][0])
                redbase1 = randomnumber
                distanceinred1 = white[0][1][0] - white[0][0][0]
                distanceinred1 = abs(distanceinred1)
                distanceingreen1 = white[1][1][0] - white[1][0][0]
                distanceingreen1 = abs(distanceingreen1)
                distanceinblue1 = white[2][1][0] - white[2][0][0]
                distanceinblue1 = abs(distanceinblue1)
                newdistancered1 = redbase - white[0][0][0]
                if distanceinred1 == 0:
                    distanceinred1 = 1
                factorofdistance1 = abs(newdistancered1 / distanceinred1)
                newdistancegreen1 = int(distanceingreen1 * factorofdistance1)
                greenbase1 = white[1][0][0] + newdistancegreen1
                newdistanceblue1 = int(distanceinblue1 * factorofdistance1)
                bluebase1 = white[2][0][0] + newdistanceblue1
                if redbase1 + 20 > 255:
                    redbase1 = 255
                else:
                    redbase1 = redbase1 + 20
                if greenbase1 + 5 > 255:
                    greenbase1 = 255
                else:
                    greenbase1 = greenbase1 + 5
                if bluebase1 + 30 > 255:
                    bluebase1 = 255
                else:
                    bluebase1 = bluebase1 + 30
                whitespotscolor = [redbase1, greenbase1, bluebase1]
            else:
                whitespotscolor = [0]

            # get point colors
            pointcolors = [0]
            if sepia == 1:
                pointcolor1red = colorforbase[0] - 20
                pointcolor1green = colorforbase[1] - 20
                pointcolor1blue = colorforbase[2] - 20
                if pointcolor1red < 0:
                    pointcolor1red = 0
                if pointcolor1green < 0:
                    pointcolor1green = 0
                if pointcolor1blue < 0:
                    pointcolor1blue = 0
                pointcolor1 = [pointcolor1red, pointcolor1green, pointcolor1blue]

                distancered = colorforbase[0] - pointcolor1red
                distancegreen = colorforbase[1] - pointcolor1green
                distanceblue = colorforbase[2] - pointcolor1blue

                distancered = int(distancered / 5)
                distancegreen = int(distancegreen / 5)
                distanceblue = int(distanceblue / 5)

                pointcolor2 = [pointcolor1[0] + distancered, pointcolor1[1] + distancegreen,
                               pointcolor1[2] + distanceblue]
                pointcolor3 = [pointcolor2[0] + distancered, pointcolor2[1] + distancegreen,
                               pointcolor2[2] + distanceblue]
                pointcolor4 = [pointcolor3[0] + distancered, pointcolor3[1] + distancegreen,
                               pointcolor3[2] + distanceblue]
                pointcolor5 = [pointcolor4[0] + distancered, pointcolor4[1] + distancegreen,
                               pointcolor4[2] + distanceblue]

                pointcolors = [pointcolor1, pointcolor2, pointcolor3, pointcolor4, pointcolor5]

            if mink == 1:
                pointcolor1red = redbasesaved
                pointcolor1green = greenbasesaved
                pointcolor1blue = bluebasesaved

                pointcolor1 = [pointcolor1red, pointcolor1green, pointcolor1blue]

                distancered = colorforbase[0] - pointcolor1red
                distancegreen = colorforbase[1] - pointcolor1green
                distanceblue = colorforbase[2] - pointcolor1blue

                distancered = int(distancered / 5)
                distancegreen = int(distancegreen / 5)
                distanceblue = int(distanceblue / 5)

                pointcolor2 = [pointcolor1[0] + distancered, pointcolor1[1] + distancegreen,
                               pointcolor1[2] + distanceblue]
                pointcolor3 = [pointcolor2[0] + distancered, pointcolor2[1] + distancegreen,
                               pointcolor2[2] + distanceblue]
                pointcolor4 = [pointcolor3[0] + distancered, pointcolor3[1] + distancegreen,
                               pointcolor3[2] + distanceblue]
                pointcolor5 = [pointcolor4[0] + distancered, pointcolor4[1] + distancegreen,
                               pointcolor4[2] + distanceblue]

                pointcolors = [pointcolor1, pointcolor2, pointcolor3, pointcolor4, pointcolor5]

            if colorpoint == 1:
                randomnumber = random.randint(colorsaved[0][0][0], colorsaved[0][1][0])
                redbasesaved = randomnumber
                distanceinred = colorsaved[0][1][0] - colorsaved[0][0][0]
                distanceingreen = colorsaved[1][1][0] - colorsaved[1][0][0]
                distanceinblue = colorsaved[2][1][0] - colorsaved[2][0][0]
                newdistancered = redbasesaved - colorsaved[0][0][0]
                if distanceinred == 0:
                    distanceinred = 1
                factorofdistance = newdistancered / distanceinred
                newdistancegreen = int(distanceingreen * factorofdistance)
                greenbasesaved = colorsaved[1][0][0] + newdistancegreen
                newdistanceblue = int(distanceinblue * factorofdistance)
                bluebasesaved = colorsaved[2][0][0] + newdistanceblue

                pointcolor1red = redbasesaved
                pointcolor1green = greenbasesaved
                pointcolor1blue = bluebasesaved

                pointcolor1 = [pointcolor1red, pointcolor1green, pointcolor1blue]

                distancered = colorforbase[0] - pointcolor1red
                distancegreen = colorforbase[1] - pointcolor1green
                distanceblue = colorforbase[2] - pointcolor1blue

                distancered = int(distancered / 5)
                distancegreen = int(distancegreen / 5)
                distanceblue = int(distanceblue / 5)

                pointcolor2 = [pointcolor1[0] + distancered, pointcolor1[1] + distancegreen,
                               pointcolor1[2] + distanceblue]
                pointcolor3 = [pointcolor2[0] + distancered, pointcolor2[1] + distancegreen,
                               pointcolor2[2] + distanceblue]
                pointcolor4 = [pointcolor3[0] + distancered, pointcolor3[1] + distancegreen,
                               pointcolor3[2] + distanceblue]
                pointcolor5 = [pointcolor4[0] + distancered, pointcolor4[1] + distancegreen,
                               pointcolor4[2] + distanceblue]

                pointcolors = [pointcolor1, pointcolor2, pointcolor3, pointcolor4, pointcolor5]

            self.basecolor = colorforbase
            self.shadowcolor1 = colorforshadow1
            self.shadowcolor2 = colorforshadow2
            self.eyecolor1 = eye1color
            self.eyecolor2 = eye2color
            self.nosecolor = nosecolor
            self.mouthcolor = mouthcolor
            self.whiskercolor = whiskercolor
            self.tabbycolor = tabbycolorreturn
            self.tortiecolor = tortiecolorreturn1
            self.spotscolor = whitespotscolor
            self.pointcolor = pointcolors

    def draw_me(self):
        from PIL import Image
        import numpy as np
        from resize import resize

        def draw_point(hair, ifcolorpoint, ifmink, ifsepia, pointcolors):
            if ifcolorpoint == 1 or ifmink == 1 or ifsepia == 1:
                from PIL import Image
                import numpy as np
                im = Image.open("temp.png")
                template = Image.open(hair + "point.png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 1) & (blue == 109) & (green == 29)
                data[..., :-1][replace.T] = (pointcolors[0][0], pointcolors[0][1], pointcolors[0][2])
                replace = (red == 67) & (blue == 153) & (green == 89)
                data[..., :-1][replace.T] = (pointcolors[1][0], pointcolors[1][1], pointcolors[1][2])
                replace = (red == 130) & (blue == 200) & (green == 148)
                data[..., :-1][replace.T] = (pointcolors[2][0], pointcolors[2][1], pointcolors[2][2])
                replace = (red == 186) & (blue == 254) & (green == 203)
                data[..., :-1][replace.T] = (pointcolors[3][0], pointcolors[3][1], pointcolors[3][2])
                replace = (red == 206) & (blue == 234) & (green == 213)
                data[..., :-1][replace.T] = (pointcolors[4][0], pointcolors[4][1], pointcolors[4][2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)
                im.save("temp.png")

        def draw_pattern(whichfur, pattern, patterncolor):
            from PIL import Image
            import numpy as np
            im = Image.open("temp.png")
            im = im.convert('RGBA')

            template = Image.open(whichfur + pattern + ".png")
            template = template.convert('RGBA')
            data = np.array(template)
            red, green, blue, alpha = data.T
            if "tabby" in pattern:
                replace = (red == 69) & (blue == 69) & (green == 69)
                data[..., :-1][replace.T] = (patterncolor[0], patterncolor[1], patterncolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            if "tortie" in pattern:
                replace = (red == 217) & (blue == 217) & (green == 217)
                data[..., :-1][replace.T] = (patterncolor[0], patterncolor[1], patterncolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            im.save("temp.png")

        def draw_whitespots(degree, whichhair, whitecolor):
            from PIL import Image
            import numpy as np
            import random
            listofspots = []
            listofareas = []
            im = Image.open("temp.png")
            im = im.convert('RGBA')
            area = 0
            spots = 0
            if degree == [200]:
                template = Image.open(whichhair + "gloves.png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 254) & (blue == 186) & (green == 211)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)
            if degree != [0]:
                if degree == [0, 50]:
                    degree = random.randint(0, 50)
                if degree == [50, 100]:
                    degree = random.randint(50, 100)
            if degree in range(1, 10):
                area = 1
                spots = 0
            if degree in range(10, 15):
                area = 2
                spots = 0
            if degree in range(15, 20):
                area = 0
                spots = 1
            if degree in range(20, 30):
                area = 2
                spots = 1
            if degree in range(30, 40):
                area = 2
                spots = 2
            if degree in range(40, 50):
                area = 4
                spots = 2
            if degree in range(50, 60):
                area = 6
                spots = 1
            if degree in range(60, 70):
                area = 6
                spots = 2
            if degree in range(70, 80):
                area = 8
                spots = 2
            if degree in range(80, 90):
                area = 10
                spots = 2
            if degree in range(90, 100):
                area = 12
                spots = 2
            if degree == 100:
                area = 16
                spots = 3

            for i in range(spots):
                randomnumber = random.randint(0, 2)
                listofspots.append(randomnumber)
                template = Image.open(whichhair + "spots" + str(randomnumber) + ".png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 76) & (blue == 76) & (green == 76)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)
            for i in range(area):
                randomnumber = random.randint(0, 15)
                listofareas.append(randomnumber)
                template = Image.open(whichhair + "area" + str(randomnumber) + ".png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 76) & (blue == 76) & (green == 76)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            im.save("temp.png")

            return listofspots, listofareas

        patterns = []
        if "tortoiseshell" in self.coatpattern:
            patterns.append("tortie")
        if "tabby" in self.coatpattern:
            if "ticked" in self.coatpattern:
                patterns.append("tickedtabby")
            else:
                if "mackerel" in self.coatpattern:
                    patterns.append("mackereltabby")
                else:
                    patterns.append("classictabby")
        drawcolorpoint = 0
        drawmink = 0
        drawsepia = 0
        if self.coatcolor != "white":
            for p in range(len(patterns)):
                if patterns[p] == "tortie":
                    patterns[p] = [patterns[p], self.tortiecolor]
                if "tabby" in patterns[p]:
                    patterns[p] = [patterns[p], self.tabbycolor]
        if "colorpoint" in self.coatcolor:
            drawcolorpoint = 1
        if "mink" in self.coatcolor:
            drawmink = 1
        if "sepia" in self.coatcolor:
            drawsepia = 1

        im = Image.open(self.furlength + 'hairtemplate.png')
        im = im.convert('RGBA')

        data = np.array(im)
        red, green, blue, alpha = data.T

        base_color = (red == 184) & (blue == 184) & (green == 184)
        shadow_1 = (red == 153) & (blue == 153) & (green == 153)
        shadow_2 = (red == 117) & (blue == 117) & (green == 117)
        eye_1 = (red == 87) & (blue == 87) & (green == 87)
        eye_2 = (red == 56) & (blue == 56) & (green == 56)
        nose = (red == 18) & (blue == 18) & (green == 18)
        whiskers = (red == 212) & (blue == 212) & (green == 212)
        mouth = (red == 82) & (blue == 82) & (green == 82)
        data[..., :-1][base_color.T] = (self.basecolor[0], self.basecolor[1], self.basecolor[2])
        data[..., :-1][shadow_1.T] = (self.shadowcolor1[0], self.shadowcolor1[1], self.shadowcolor1[2])
        data[..., :-1][shadow_2.T] = (self.shadowcolor2[0], self.shadowcolor2[1], self.shadowcolor2[2])
        data[..., :-1][mouth.T] = (self.mouthcolor[0], self.mouthcolor[1], self.mouthcolor[2])
        data[..., :-1][eye_2.T] = (self.eyecolor2[0], self.eyecolor2[1], self.eyecolor2[2])
        data[..., :-1][eye_1.T] = (self.eyecolor1[0], self.eyecolor1[1], self.eyecolor1[2])
        data[..., :-1][nose.T] = (self.nosecolor[0], self.nosecolor[1], self.nosecolor[2])
        data[..., :-1][whiskers.T] = (self.whiskercolor[0], self.whiskercolor[1], self.whiskercolor[2])

        im2 = Image.fromarray(data)
        im2.save("temp.png")
        draw_point(self.furlength, drawcolorpoint, drawmink, drawsepia, self.pointcolor)

        if len(patterns) != 0:
            for f in range(len(patterns)):
                if patterns[f][0] == "tortie":
                    draw_pattern(self.furlength, patterns[f][0], self.tortiecolor)
                if "tabby" in patterns[f][0]:
                    draw_pattern(self.furlength, patterns[f][0], self.tabbycolor)

        if self.coatcolor != "white":
            self.whichspots, self.whichareas = draw_whitespots(self.white, self.furlength, self.spotscolor)

        final = Image.open("temp.png")
        self.image = final
        self.resizedimage = resize(self.image)

    def draw_baby(self):
        from PIL import Image
        import numpy as np
        from resize import resize

        def draw_pattern(pattern, patterncolor):
            from PIL import Image
            import numpy as np
            im = Image.open("temp.png")
            im = im.convert('RGBA')

            template = Image.open("baby" + pattern + ".png")
            template = template.convert('RGBA')
            data = np.array(template)
            red, green, blue, alpha = data.T
            if "tabby" in pattern:
                replace = (red == 69) & (blue == 69) & (green == 69)
                data[..., :-1][replace.T] = (patterncolor[0], patterncolor[1], patterncolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            if "tortie" in pattern:
                replace = (red == 217) & (blue == 217) & (green == 217)
                data[..., :-1][replace.T] = (patterncolor[0], patterncolor[1], patterncolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            im.save("temp.png")

        def draw_whitespots(degree, whitecolor, whichspots, whichareas):
            from PIL import Image
            import numpy as np
            import random
            im = Image.open("temp.png")
            im = im.convert('RGBA')
            if degree == [200]:
                template = Image.open("babygloves.png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 254) & (blue == 186) & (green == 211)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            for i in whichspots:
                template = Image.open("babyspots" + str(i) + ".png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 76) & (blue == 76) & (green == 76)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)
            for i in whichareas:
                template = Image.open("babywhite" + str(i) + ".png")
                data = np.array(template)
                red, green, blue, alpha = data.T
                replace = (red == 76) & (blue == 76) & (green == 76)
                data[..., :-1][replace.T] = (whitecolor[0], whitecolor[1], whitecolor[2])
                pattern2 = Image.fromarray(data)
                im.paste(pattern2, (0, 0), pattern2)

            im.save("temp.png")

        patterns = []
        if "tortoiseshell" in self.coatpattern:
            patterns.append("tortie")
        if "tabby" in self.coatpattern:
            if "ticked" in self.coatpattern:
                patterns.append("tickedtabby")
            else:
                if "mackerel" in self.coatpattern:
                    patterns.append("mackereltabby")
                else:
                    patterns.append("classictabby")
        if self.coatcolor != "white":
            for p in range(len(patterns)):
                if patterns[p] == "tortie":
                    patterns[p] = [patterns[p], self.tortiecolor]
                if "tabby" in patterns[p]:
                    patterns[p] = [patterns[p], self.tabbycolor]

        im = Image.open('babytemplate.png')
        im = im.convert('RGBA')

        data = np.array(im)
        red, green, blue, alpha = data.T

        base_color = (red == 184) & (blue == 184) & (green == 184)
        shadow_1 = (red == 153) & (blue == 153) & (green == 153)
        shadow_2 = (red == 117) & (blue == 117) & (green == 117)
        eye_2 = (red == 56) & (blue == 56) & (green == 56)
        nose = (red == 18) & (blue == 18) & (green == 18)
        data[..., :-1][base_color.T] = (self.basecolor[0], self.basecolor[1], self.basecolor[2])
        data[..., :-1][shadow_1.T] = (self.shadowcolor1[0], self.shadowcolor1[1], self.shadowcolor1[2])
        data[..., :-1][shadow_2.T] = (self.shadowcolor2[0], self.shadowcolor2[1], self.shadowcolor2[2])
        data[..., :-1][eye_2.T] = (self.babyeyes[0], self.babyeyes[1], self.babyeyes[2])
        data[..., :-1][nose.T] = (self.nosecolor[0], self.nosecolor[1], self.nosecolor[2])

        im2 = Image.fromarray(data)
        im2.save("temp.png")

        if len(patterns) != 0:
            for f in range(len(patterns)):
                if patterns[f][0] == "tortie":
                    draw_pattern(patterns[f][0], self.tortiecolor)
                if "tabby" in patterns[f][0]:
                    draw_pattern(patterns[f][0], self.tabbycolor)
        if self.coatcolor != "white":
            draw_whitespots(self.white, self.spotscolor, self.whichspots, self.whichareas)

        final = Image.open("temp.png")
        self.babyimage = final
        self.resizedbabyimage = resize(self.babyimage)

    def show_me(self):
        from PIL import Image
        self.resizedimage.show()

    def show_baby(self):
        from PIL import Image
        self.resizedbabyimage.show()

