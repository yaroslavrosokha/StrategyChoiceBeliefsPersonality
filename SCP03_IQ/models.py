from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import random

author = 'Yaroslav Rosokha'

doc = """
ICAR 11-item Matrix Reasoning Test 
"""


class Constants(BaseConstants):
    name_in_url = 'SCP03_IQ'
    players_per_group = None
    num_rounds=11
    figNames=['fig12043.jpg','fig12044.jpg','fig12045.jpg','fig12046.jpg','fig12047.jpg',
              'fig12048.jpg','fig12050.jpg','fig12053.jpg','fig12054.jpg','fig12055.jpg','fig12056.jpg']

class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        def creating_session(self):
            if self.round_number == 1:
                for p in self.get_players():
                    order = list(range(1,11+1))
                    # random.shuffle(order) #randomize order of questions
                    p.participant.vars['iqOrder'] = dict(zip(range(1,11+1), order))
                    out = ""
                    for x in order:
                        out+=","+str(x)
                    p.myOrder = out


class Player(BasePlayer):

    iqResponses = models.StringField()
    myOrder=models.StringField()
