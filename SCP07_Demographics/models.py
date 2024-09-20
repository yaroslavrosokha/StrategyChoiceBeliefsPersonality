from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Demographic Questionnaire (Pre-experiment Survey) 
"""


class Constants(BaseConstants):
    name_in_url = 'SCP07_Demographics'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):


    #Questionnaire

    ageSelect = models.StringField(
        choices=['Under 20', '20 and over', 'Prefer Not to Say'],
        verbose_name='Age:')

    genderSelect = models.StringField(
        choices=['Male', 'Female', 'Prefer Not to Say'],
        verbose_name='Gender:')

    majorSelect = models.StringField(
        choices=['Economics or Management', 'STEM (Science, Technology, Engineering, Math)',
                 'Liberal Arts','Other', 'Prefer Not to Say'],
        verbose_name='Major:')

    hsSelect = models.StringField(
        choices=['In US',
                 'Outside of US', 'Prefer Not to Say'],
        verbose_name='Went to High School:')