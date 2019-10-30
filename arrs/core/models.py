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

    def __str__(self):
        vString = ("N", "V")[self.varsity]
        return self.name + " (" + vString + " " + self.event + ")"

#Model representing a single debate round
#NOTE: has a many-to-one relationship with Comp model
#TODO: create subclasses for speech/debate rounds (PHASE II)
class Round(models.Model):

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    aff = models.ManyToManyField(Comp, related_name="RND_AFF")
    neg = models.ManyToManyField(Comp, related_name="RND_NEG")

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
    type = models.CharField(null=False, max_length=3, choices=ROUND_TYPES, default="PRE")
    #result = models.BooleanField(default=True) ##TODO: use true to indicate AFF win, false for NEG win
    result = models.StringField(null=False, default="AFF")

    #GET METHODS
    def getAff(self):
        return self.aff.all()[0].name

    def getNeg(self):
        return self.neg.all()[0].name

    def getWinner(self):
        if self.result == "AFF":
            return self.getAff()
        else:
            return self.getNeg()

    def __str__(self):
        return str(self.tournament) + " " + self.getAff() + " v. " + self.getNeg() + " (" + self.type + ")"
