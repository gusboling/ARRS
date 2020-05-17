from django.db import models

class Comp(models.Model):
    """A single team or competitor
    Members:
    --------
    name: str, required, primary key
        name of the debater/team
    """
    name = models.CharField(max_length=100, unique=True, default="Unknown")

    def get_name(self):
        return self.name

    def __str__(self):
        return str(self.name)

class Tournament(models.Model):
    """A single tournament
    Members:
    --------
    name: str, required
        Name of tournament
    """

    name = models.CharField(max_length=100, default="Unknown")

    def get_name(self):
        return self.name

    def __str__(self):
        return str(self.name)

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
    debater = models.ForeignKey(Comp, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    
    #Local fields
    ROUND_TYPES = [
        ("PRE", "Preliminary"),
        ("OCT", "Octafinal"),
        ("QRT", "Quarterfinal"),
        ("SEM", "Semifinal"),
        ("FIN", "Final"),
        ("OTH", "Other")
    ]

    EVENT_TYPES = [
        ("VPO", "Varsity Policy"),
        ("VLD", "Varsity Lincoln-Douglas"),
        ("VPF", "Public Forum"),
        ("NPO", "Novice Policy"),
        ("NLD", "Novice Lincoln-Douglas"),
        ("OTH", "Other")
    ]

    opponent = models.CharField(max_length=100, default="Unknown")
    bracket = models.CharField(max_length=3, choices=ROUND_TYPES, default="OTH")
    event = models.CharField(max_length=3, choices=EVENT_TYPES, default="OTH")
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
