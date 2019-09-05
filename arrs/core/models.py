from django.db import models

#Model representing a tournament
#NOTE: has a many-to-one relationship with Round, Many-to-many with Comp
class Tournament(models.Model):
    ## TODO
    pass

#Model representing a single competitor/competitor-partnership
#NOTE: has none-to-many relationship with Round model
class Comp(models.Model):
    name = models.CharField(max_length="50", unique=True, null=False)
    event = models.CharField(max_length="100", null=False)
    varsity = models.BooleanField(default=False)

#Model representing a single debate round
#NOTE: has a many-to-one relationship with Comp model
#TODO: create subclasses for speech/debate rounds (PHASE II)
class Round(models.Model):

    tournament = models.ForeignKey(Tournament) #TODO: Need some sort of primary key in addition to this?
    #aff = models.ForeignKey(Comp)
    #neg = models.ForeignKey(Comp) #Not

    #Round Type Information
    ROUND_TYPES = [
        ("PRE", "Preliminary")
        ("TOC", "Triple Octafinal"),
        ("DOC", "Double Octafinal"),
        ("OCT", "Octafinal"),
        ("QRT", "Quarterfinal"),
        ("SEM", "Semifinal"),
        ("FIN", "Final")
    ]
    type = models.CharField(null=False, max_length=3, choices=ROUND_TYPES, default="PRE")
    #result = models.BooleanField(default=True) ##TODO: use true to indicate AFF win, false for NEG win?
