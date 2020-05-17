from django.db import models

class Round(models.Model):
    """A single debate round
    Members:
    --------
    debater: str, required
        character field corresponding to the name field of a Comp-object instance
    opponent: str, required
        character field containing the name of the opponent
    bracket: str, required
        3-character code representing round-type (PRE, OCT, QRT, SEM, FIN)
    won: boolean, required
        Indicates if the debater won the round
    position: boolean, required
        Indicates if the debater argued AFF
    event:
        3-character code representing round-event (VPO, VLD, VPF, NPO, NLD)
    """
    #Relational Fields
    debater = models.CharField() #Make foreign key?
    tournament = models.CharField() #Make foreign key?
    
    #Local fields
    ROUND_TYPES = [
        ("PRE", "Preliminary"),
        ("OCT", "Octafinal"),
        ("QRT", "Quarterfinal"),
        ("SEM", "Semifinal"),
        ("FIN", "Final")
    ]

    EVENT_TYPES = [
        ("VPO", "Varsity Policy"),
        ("VLD", "Varsity Lincoln-Douglas"),
        ("VPF", "Public Forum"),
        ("NPO", "Novice Policy"),
        ("NLD", "Novice Lincoln-Douglas")
    ]

    opponent = models.CharField(max_length=100)
    bracket = models.CharField(max_length=3, choices=ROUND_TYPES)
    event = models.CharField(max_length=3, choices=EVENT_TYPES)
    won = models.BooleanField(default=False)
    position = models.BooleanField(default=False)

    def get_debater(self):
        return self.debater

    def get_tournament(self):
        return self.tournament

    def get_braket(self):
        return self.bracket

    def get_won(self):
        return self.won

    def get_position(self):
        return self.position

    def __str__(self):
        return str(self.debater) + "v." + str(self.opponent)

class Comp(models.Model):
    """A single team or competitor
    Members:
    --------
    name: str, required, primary key
        name of the debater/team
    """
    name = models.CharField(max_length=100, unique=True)

    def get_name(self):
        return self.name

    def __str__(self):
        return str(self.name)

class Tournament(models.Model):
    """A single tournament
    Members:
    --------
    location: str, required
        Place where tournament took place (e.g. Bozeman, Helena, etc.)
    year: str, required
        Year of the tournament (2020, etc.)
    """
    location = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    
    def get_location(self):
        return self.location

    def get_year(self):
        return self.year

    def __str__(self):
        return str(self.location) + " " + str(self.year)
