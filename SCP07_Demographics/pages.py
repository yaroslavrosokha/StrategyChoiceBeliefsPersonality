from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class Questionnaire(Page):

    form_model = 'player'
    form_fields = [
                   'ageSelect',
                   'genderSelect',
                   'majorSelect',
                   'hsSelect'
                   ]


class WaitForOthers(WaitPage):
    template_name = 'strategyChoiceDemographics/myWaitPage.html'

    def vars_for_template(self):
        print("demographicQuestionnaire,WaitForOthers()...")

        if self.player.ageSelect>=18:
            title_text = "Please wait for experiment to begin."
            body_text = ""
        else:
            #Needs some work because now advances to the next stage even if not consented
            title_text = "You are not eligible to participate in this experiment. Please raise your hand."
            body_text = ""

        return {'title_text': title_text,"body_text":body_text}


page_sequence = [

    Questionnaire,
    # WaitForOthers

]