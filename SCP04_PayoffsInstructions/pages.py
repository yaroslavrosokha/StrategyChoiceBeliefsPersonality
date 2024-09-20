from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Testing(Page):

    form_model = 'player'
    form_fields = ['myHistory','otherHistory']

    def vars_for_template(self):
        return {'R': self.session.config['R']}


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'R': self.session.config['R'],
                'PointsPerDollar': int(1.0/self.session.config['real_world_currency_per_point']),
                'ShowUpFee': int(self.session.config['participation_fee'])}

page_sequence = [

    Instructions,
    Testing

]
