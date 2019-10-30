from django.db import models
from datetime import date


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

    #Returns name of the competitor
    def getName(self):
        return self.name

    #Returns (name?) of all rounds associated with comp
    def getRounds(self):
        comprounds = {"affirmative": self.affcomp.all(), "negative": self.negcomp.all()}
        return comprounds
        

    #Iterates over self.getRounds() and returns the number of rounds where comp won.
    def getWinCount(self):
        win_count = 0
        rnds = self.getRounds()
        for rnd in rnds["affirmative"]: 
            if rnd.getWinner() == self.getName(): win_count += 1
        for rnd in rnds["negative"]: 
            if rnd.getWinner() == self.getName(): win_count += 1
        return win_count

    #Returns value of len(self.getRounds()) minus self.getWinCount()
    def getLossCount(self):
        rnds = self.getRounds()
        totalRounds = len(rnds["affirmative"]) + len(rnds["negative"])
        return totalRounds - self.getWinCount()

    def __str__(self):
        vString = ("N", "V")[self.varsity]
        return self.name + " (" + vString + " " + self.event + ") " + str(self.getWinCount()) + "-" + str(self.getLossCount()) 

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
