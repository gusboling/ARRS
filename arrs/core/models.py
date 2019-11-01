from django.db import models
from datetime import date

import operator

#Model representing a tournament
#NOTE: has a many-to-one relationship with Round, Many-to-many with Comp
class Tournament(models.Model):
    location = models.CharField(max_length=100, null=False, default="Unofficial")
    year = models.IntegerField(default=date.today().year)

    def __str__(self):
        return self.location + " " + str(self.year)


#Model representing a single competitor/competitor-partnership
#NOTE: has none-to-many relationship with Round model
class Comp(models.Model):

    name = models.CharField(max_length=50, unique=True)
    event = models.CharField(max_length=100)
    varsity = models.BooleanField(default=False)
    onteam = models.BooleanField(default=False)

    #ACCESOR METHODS
    def getName(self):
        return self.name

    def getEvent(self):
        return self.event

    def getLevel(self):
        return ("Novice", "Varsity")[self.varsity]

    def getRounds(self):
        comprounds = {"affrounds": self.affcomp.all(), "negrounds": self.negcomp.all()}
        return comprounds

    #STAT METHODS
    #DESC: Returns integer representing total number of rounds won.
    def getWinCount(self):
        win_count = 0
        rnds = self.getRounds()
        for rnd in rnds["affirmative"]:
            if rnd.getWinner() == self.getName(): win_count += 1
        for rnd in rnds["negative"]:
            if rnd.getWinner() == self.getName(): win_count += 1
        return win_count


    #DESC: Returns integer representing total number of rounds lost.
    def getLossCount(self):
        rnds = self.getRounds()
        total_rounds = len(rnds["affrounds"]) + len(rnds["negrounds"])
        return total_rounds - self.getWinCount()

    #TOSTRING METHOD
    def __str__(self):
        return self.getName() + " (" + self.getLevel() + " " + self.getEvent() + ")


#Model representing a single debate round
#NOTE: has a many-to-one relationship with Comp model
#TODO: create subclasses for speech/debate rounds (PHASE II)
class Round(models.Model):

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    aff = models.ManyToManyField(Comp, related_name="affcomp")
    neg = models.ManyToManyField(Comp, related_name="negcomp")

    #Round Type Information
    ROUND_TYPES = [
        ("PRE", "Preliminary"),
        ("TOC", "Triple Octafinal"),
        ("DOC", "Double Octafinal"),
        ("OCT", "Octafinal"),
        ("QRT", "Quarterfinal"),
        ("SEM", "Semifinal"),
        ("FIN", "Final")
    ]
    RESULTS = [("AFF", "Affirmative Win"), ("NEG", "Negative Win")]
    type = models.CharField(null=False, max_length=3, choices=ROUND_TYPES, default="PRE")
    result = models.CharField(null=False, max_length=3, choices=RESULTS, default="AFF")

    #GET METHODS
    def getAff(self):
        return self.aff.all()[0].name

    def getNeg(self):
        return self.neg.all()[0].name

    def getWinner(self):
        #return []
        if self.result == "AFF":
            return self.getAff()
        else:
            return self.getNeg()

    def __str__(self):
        return str(self.tournament) + " " + self.getAff() + " v. " + self.getNeg() + " (" + self.type + ")"

def getVarsityPolicyDozen():
    vpol_comps = Comp.objects.filter(event="Policy").filter(varsity=True)
    vpol_dict = {}
    for vc in vpol_comps:
        vpol_dict[vc.getName()] = vc.getWinCount()
    ranked_comps = sorted(vpol_dict.items(), key=operator.itemgetter(1))
    print(ranked_comps)
