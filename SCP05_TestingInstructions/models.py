from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Strategy Choice: Plan Testing Phase
"""


class Constants(BaseConstants):
    name_in_url = 'SCP05_TestingInstructions'
    players_per_group = None
    num_rounds=1
    orders=[
        [10, 9, 5, 2, 3, 4, 8, 7, 1, 6],
        [5, 2, 10, 9, 1, 8, 3, 4, 6, 7],
        [2, 1, 7, 9, 10, 6, 8, 3, 5, 4],
        [9, 4, 2, 7, 10, 3, 5, 8, 1, 6],
        [1, 4, 8, 2, 5, 10, 3, 6, 9, 7],
        [3, 9, 2, 8, 6, 7, 10, 4, 5, 1],
        [8, 1, 6, 10, 5, 4, 7, 3, 2, 9],
        [6, 5, 3, 1, 4, 7, 2, 8, 9, 10],
        [2, 7, 10, 5, 4, 8, 9, 1, 6, 3],
        [4, 7, 1, 9, 6, 8, 3, 2, 10, 5],
        [4, 10, 7, 6, 8, 5, 3, 1, 2, 9],
        [7, 10, 9, 1, 6, 2, 8, 3, 5, 4],
        [9, 8, 2, 10, 3, 5, 7, 4, 6, 1],
        [5, 2, 9, 3, 7, 6, 4, 1, 8, 10],
        [10, 5, 9, 3, 7, 1, 4, 2, 8, 6],
        [6, 10, 5, 4, 2, 7, 3, 1, 8, 9]
    ]

    strategySet = [ 'Choose A in every round.',
                    'Choose B in every round.',
                    'Choose A in round 1. After round 1: choose A if the other chose A in the previous round; choose B if the other chose B in the previous round.',
                    'Choose A in round 1. After round 1: choose A if the other chose A in every one of the previous rounds; choose B if the other chose B in one or more of the previous rounds.',
                    'Choose B in round 1. After round 1: choose A if the other chose A in the previous round; choose B if the other chose B in the previous round.',
                    'Choose B in round 1. After round 1: choose A if the other chose A in every one of the previous rounds; choose B if the other chose B in one or more of the previous rounds.',
                    'Choose A in rounds 1 and 2. After round 2: choose A if the other chose A in either of the previous two rounds; choose B if the other chose B in both of the previous two rounds.',
                    'Choose A in rounds 1 and 2. After round 2: choose A if the other has never chosen B twice in a row (i.e., if the other has never chosen B in two consecutive previous rounds); choose B if the other has ever chosen B twice in a row.',
                    'Choose A in round 1. In round 2: choose A if the other chose A in round 1; choose B if the other chose B in round 1. After round 2: choose A if the other chose A in both of the previous two rounds; choose B if the other chose B in either of the previous two rounds.',
                    'Choose randomly between A and B in every round. At the beginning of every round, the computer flips a computerized fair coin for you: when your coin comes up heads, you choose A; when your coin comes up tails you choose B.'
                    ]

class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                randomOrder = Constants.orders[p.id_in_group-1]
                # randomOrder = list(range(1,52+1))
                # random.shuffle(randomOrder)
                p.participant.vars['strategiesOrder'] = dict(zip(range(1, 10 + 1), randomOrder))
                out = ""
                for x in randomOrder:
                    out += "," + str(x)
                p.myOrder = out

class Player(BasePlayer):

    # Store testing history
    testingHistory=models.StringField()

    myOrder = models.StringField()

