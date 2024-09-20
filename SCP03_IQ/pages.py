from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time

class page0(Page):
    def before_next_page(self):
        # user has 7 minutes to complete as many pages as possible
        self.participant.vars['expiryIQ'] = time.time() + 7*60

    def is_displayed(self):
        return self.subsession.round_number == 1

class page1(Page):
    timer_text = 'Time Left:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiryIQ'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryIQ'] - time.time() > 1

    form_model = 'player'
    form_fields = ['iqResponses']

    def vars_for_template(self):
        return {'image_path': 'StrategyChoiceIQ/{}'.format(Constants.figNames[self.participant.vars['iqOrder'][self.player.round_number]-1])}

page_sequence = [

    page0,
    page1,

]
