from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


### Change EarnBelief5 to EarnBelief25 below ###


class PaymentInfo(Page):

    def before_next_page(self):

        self.player.payoff=c(self.participant.vars['EarnBelief1'])+c(self.participant.vars['EarnBelief25'])
        self.participant.vars['totalPayoffs'] = (c(self.participant.vars['EarnBelief1'])+c(self.participant.vars['EarnBelief25'])+self.participant.payoff).to_real_world_currency(self.session)

    def vars_for_template(self):
        return {
                'MatchesPayoff':self.participant.payoff.to_real_world_currency(self.session),
                'BeliefsPayoff':(c(self.participant.vars['EarnBelief1'])+c(self.participant.vars['EarnBelief25'])).to_real_world_currency(self.session),
                'TotalPayoff':(c(self.participant.vars['EarnBelief1'])+c(self.participant.vars['EarnBelief25'])+self.participant.payoff).to_real_world_currency(self.session),
                'Matches':self.participant.vars['Matches']
                }

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [

    PaymentInfo

]
