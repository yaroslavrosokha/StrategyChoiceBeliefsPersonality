from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Strategy Choice Instructions: description of the payoff table and practice direct-response matches.
"""


class Constants(BaseConstants):
    name_in_url = 'SCP04_PayoffsInstructions'
    players_per_group = None
    num_rounds=10


class Group(BaseGroup):

    pass


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # Store testing history
    myHistory=models.StringField()
    otherHistory = models.StringField()

