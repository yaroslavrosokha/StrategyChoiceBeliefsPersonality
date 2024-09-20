from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class p01_introduction(Page):
    def before_next_page(self):
        # user has 6 minutes to complete as many pages as possible
        self.participant.vars['expiryPersonality'] = time.time() + 6*60

class page1(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses1']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(1,10+1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i]-1])
        return {'randomQuestionsOrder': zip(range(1, 10 + 1), tempQ1)}

class page2(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses2']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(11,20+1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i]-1])
        return {'randomQuestionsOrder': zip(range(11, 20 + 1), tempQ1)}

class page3(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses3']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(21,30+1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i]-1])
        return {'randomQuestionsOrder': zip(range(21, 30 + 1), tempQ1)}


class page4(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses4']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(31, 40 + 1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i] - 1])
        return {'randomQuestionsOrder': zip(range(31, 40 + 1), tempQ1)}


class page5(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses5']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(41, 50 + 1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i] - 1])
        return {'randomQuestionsOrder': zip(range(41, 50 + 1), tempQ1)}


class page6(Page):
    timer_text = 'Time Left:'

    form_model = 'player'
    form_fields = ['myResponses6']

    def get_timeout_seconds(self):
        return self.participant.vars['expiryPersonality'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiryPersonality'] - time.time() > 1

    def vars_for_template(self):
        tempQ1 = []
        for i in range(51, 52 + 1):
            tempQ1.append(Constants.questions[self.participant.vars['bigFiveOrder'][i] - 1])
        return {'randomQuestionsOrder': zip(range(51, 52 + 1), tempQ1)}


page_sequence = [

    p01_introduction,
    page1,
    page2,
    page3,
    page4,
    page5,
    page6

]
