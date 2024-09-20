from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Yaroslav Rosokha'

doc = """
Introduction to Strategy Choice and Personal Characteristics Experiment
"""

class Constants(BaseConstants):
    name_in_url = 'SCP01_Introduction'

    min_payment = 5
    players_per_group = None
    duration = 60

    num_rounds = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.R = self.session.config['R']
            p.Seq = self.session.config['Sequence']


class Player(BasePlayer):
    R = models.IntegerField()
    Seq = models.IntegerField()
