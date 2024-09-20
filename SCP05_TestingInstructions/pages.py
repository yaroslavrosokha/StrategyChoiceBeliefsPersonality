from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Testing(Page):
    timer_text = 'Time Left:'
    timeout_seconds = 300

    form_model = 'player'
    form_fields = ['testingHistory']

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),'order':Constants.orders[self.player.id_in_group-1],'R': self.session.config['R']}

class Plans(Page):
    timer_text = 'Time Left:'
    timeout_seconds = 180

    def vars_for_template(self):
        tempStrategies=[Constants.strategySet[i-1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),'order':Constants.orders[self.player.id_in_group-1],'R': self.session.config['R']}


class Reminder(Page):
    def vars_for_template(self):
        return {'strategies': zip(range(1, len(Constants.strategySet) + 1), Constants.strategySet),
                'order': Constants.orders[self.player.id_in_group - 1], 'R': self.session.config['R']}


class Task(Page):

    form_model = 'player'
    form_fields = ['task']

    def vars_for_template(self):
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),Constants.strategySet),'order':Constants.orders[self.player.id_in_group-1],'R': self.session.config['R']}

class Beliefs(Page):

    form_model = 'player'
    form_fields = ['belief']

    def vars_for_template(self):
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),Constants.strategySet)}

page_sequence = [


    Plans,
    Testing,
    Reminder,
    # Task,
    # Beliefs,

]
