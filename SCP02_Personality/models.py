from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import random

author = 'Yaroslav Rosokha'

doc = """
Personality Questionnaire. 
52-items: 10 Trust (BFI A1), 10 Anxiety (BFI N1), 10 Coutiousness (BFI C6), 8 Forgiveness (VIA F), 8 Kindness (VIA F), 6 Manipulativeness (CATPD)
"""


class Constants(BaseConstants):
    name_in_url = 'SCP02_Personality'
    players_per_group = None
    num_rounds=1

    questions=[
        "I trust others.",
        "I believe that others have good intentions.",
        "I trust what people say.",
        "I believe that people are basically moral.",
        "I believe in human goodness.",
        "I think that all will be well.",
        "I distrust people.",
        "I suspect hidden motives in others.",
        "I am wary of others.",
        "I believe that people are essentially evil.",

        "I worry about things.",
        "I fear for the worst.",
        "I am afraid of many things.",
        "I get stressed out easily.",
        "I get caught up in my problems.",
        "I am not easily bothered by things.",
        "I am relaxed most of the time.",
        "I am not easily disturbed by events.",
        "I don't worry about things that have already happened.",
        "I adapt easily to new situations.",

        "I avoid mistakes.",
        "I choose my words with care.",
        "I stick to my chosen path.",
        "I jump into things without thinking.",
        "I make rash decisions.",
        "I like to act on a whim.",
        "I rush into things.",
        "I do crazy things.",
        "I act without thinking.",
        "I often make last-minute plans.",

        "VIA-IS-R No. 6",
        "VIA-IS-R No. 30",
        "VIA-IS-R No. 54",
        "VIA-IS-R No. 78",
        "VIA-IS-R No. 102",
        "VIA-IS-R No. 126",
        "VIA-IS-R No. 150",
        "VIA-IS-R No. 174",


        "VIA-IS-R No. 12",
        "VIA-IS-R No. 36",
        "VIA-IS-R No. 60",
        "VIA-IS-R No. 84",
        "VIA-IS-R No. 108",
        "VIA-IS-R No. 132",
        "VIA-IS-R No. 156",
        "VIA-IS-R No. 180",

        "I take advantage of others.",
        "I cheat to get ahead.",
        "I like to trick people into doing things for me.",
        "I deceive people.",
        "I have exploited others for my own gain.",
        "I am an honest person.",
    ]


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        def creating_session(self):
            if self.round_number == 1:
                for p in self.get_players():
                    randomOrder=[47, 4, 23, 17, 43, 14, 45, 21, 33, 2,
                                 11, 36, 7, 25, 13, 32, 42, 34, 18, 24,
                                 41, 16, 6, 28, 3, 22, 46, 50, 26, 10,
                                 27, 1, 38, 12, 8, 35, 49, 40, 20, 44,
                                 15, 29, 37, 51, 31, 39, 19, 48, 9, 52,
                                 5, 30]
                    # randomOrder = list(range(1,52+1))
                    # random.shuffle(randomOrder)
                    p.participant.vars['bigFiveOrder'] = dict(zip(range(1,52+1), randomOrder))
                    out = ""
                    for x in randomOrder:
                        out+=","+str(x)
                    p.myOrder = out


class Player(BasePlayer):

    myResponses1 = models.StringField()
    myResponses2 = models.StringField()
    myResponses3 = models.StringField()
    myResponses4 = models.StringField()
    myResponses5 = models.StringField()
    myResponses6 = models.StringField()

    myOrder=models.StringField()
