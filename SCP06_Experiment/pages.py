from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import numpy as np
import copy as cp

## ------------------------------------------ STRATEGIES - -----------------------------------------------
## ALLC
def allc(hist):
    return 0

## ALLD
def alld(hist):
    return 1

## TFT
def tft(hist):
    if len(hist)==0:
        return 0
    else:
        return int(hist[-1])

def grim(hist):
    if len(hist)==0:
        return 0
    else:
        return int(np.any(hist==1))

def stft(hist):
    if len(hist)==0:
        return 1
    else:
        return int(hist[-1])

def sgrim(hist):
    if len(hist)==0:
        return 1
    else:
        return int(np.any(hist == 1))

def check2Dinarow(hist):
    for i in range(len(hist)-1):
        if hist[i]==1 and hist[i+1]==1:
            return 1
    return 0

def grim2(hist):
    if len(hist)<2:
        return 0
    else:
        return int(check2Dinarow(hist))

def tf2t(hist):
    if len(hist)<2:
        return 0
    else:
        return int(np.all(hist[-2:]==1))

def two_tft(hist):
    if len(hist)==0:
        return 0
    elif len(hist)==1:
        return int(hist[-1])
    else:
        return int(hist[-1]==1 or hist[-2]==1)


def random(hist):
    return np.random.choice([0, 1])

def playStrategies(strategy1, strategy2, R, periods):

    Game = [[R,12],[50,25]]

    h1 = np.empty(periods)
    h2 = np.empty(periods)

    r1 = np.empty(periods)
    r2 = np.empty(periods)

    for p in range(periods):
        a1 = strategy1(h2[:p])
        a2 = strategy2(h1[:p])

        h1[p] = a1
        h2[p] = a2

        r1[p] = Game[a1][a2]
        r2[p] = Game[a2][a1]

    str_h1="".join([","+str(x) for x in h1])
    str_h2="".join([","+str(x) for x in h2])

    str_r1="".join([","+str(x) for x in r1])
    str_r2="".join([","+str(x) for x in r2])

    return str_h1, str_h2, str_r1, str_r2, np.sum(r1), np.sum(r2)


class Match(Page):

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),
                'order':Constants.orders[self.player.id_in_group-1],
                'R': self.session.config['R'],
                'myRow':self.player.myRow,
                'myHistory':self.player.myHistory,
                'otherHistory':self.player.otherHistory,
                'myPayoffs':self.player.myPayoffs,
                'otherPayoffs':self.player.otherPayoffs}


class BeliefsInstructions(Page):
    def is_displayed(self):
        return self.player.round_number == 1 or self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),
                'order':Constants.orders[self.player.id_in_group-1],
                'R': self.session.config['R'],
                'myHistory':None,
                'otherHistory':None,
                'myPayoffs':None,
                'otherPayoffs':None}

class Message(Page):
    timer_text = ''
    timeout_seconds = 10
    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),
                'order':Constants.orders[self.player.id_in_group-1],
                'R': self.session.config['R'],
                'myHistory':None,
                'otherHistory':None,
                'myPayoffs':None,
                'otherPayoffs':None}


class StrategyChoice(Page):
    form_model = 'player'
    form_fields = ['myStrategy','myRow']

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),
                'order':Constants.orders[self.player.id_in_group-1],
                'R': self.session.config['R'],
                'myHistory':None,
                'otherHistory':None,
                'myPayoffs':None,
                'otherPayoffs':None}


class Beliefs(Page):
    form_model = 'player'
    form_fields = ['belief']

    # def before_next_page(self):
    #     temp = self.player.belief.split(',')
    #     temp = temp[1:]
    #     temp = [int(x) for x in temp]
    #
    #     # print(int(self.player.otherStrategy)-1,temp[int(self.player.otherStrategy)-1],100-temp[int(self.player.otherStrategy)-1])
    #     penalty = (100-temp[int(self.player.otherStrategy)-1])*(100-temp[int(self.player.otherStrategy)-1])*0.02
    #     # print("Other Strategy:", int(self.player.otherStrategy),"Belief:",temp[int(self.player.otherStrategy)-1], "Penalty:", penalty)
    #     for i in range(10):
    #         if i!=int(self.player.otherStrategy)-1:
    #             penalty += (temp[i])*(temp[i])*0.02
    #             # print("i:", i+1,"Belief:",temp[i],  "Penalty:", (temp[i])*(temp[i])*0.01)
    #
    #
    #     self.player.earnBelief = 400-penalty
    #     self.participant.vars['EarnBelief'+str(self.player.round_number)] = self.player.earnBelief
    #     self.participant.vars['Matches']=self.player.round_number
    #     # print("Split beliefs:", temp, " Other strategy:", self.player.otherStrategy,"Penalty:",penalty)


    def is_displayed(self):
        return self.player.round_number == 1 or self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        tempStrategies = [Constants.strategySet[i - 1] for i in Constants.orders[self.player.id_in_group-1]]
        return {'strategies': zip(range(1,len(Constants.strategySet)+1),tempStrategies),
                'order':Constants.orders[self.player.id_in_group-1],
                'R': self.session.config['R'],
                'myHistory':None,
                'otherHistory':None,
                'myPayoffs':None,
                'otherPayoffs':None}


class WaitForOthers(WaitPage):
    wait_for_all_groups = True
    template_name = 'SCP06_Experiment/myWaitPage.html'

    def vars_for_template(self):
        title_text = "Please wait for the other participant to make the choice..."
        # body_text = "My Strategy: "+str(self.player.myStrategy) + " My Row: "+str(self.player.myRow)
        body_text=""
        return {'title_text': title_text, "body_text": body_text}

    def after_all_players_arrive(self):
        # print("WaitForOthers()...after_all_players_arrive()")
        subs = [p for p in self.subsession.get_players()]
        np.random.shuffle(subs)
        # print("Shuffled:",[p.id_in_group for p in subs])

        for i in range(int(len(subs)/2)):
            p1 = subs[2*i]
            p2 = subs[2*i+1]

            p1.otherSubject=str(p2.id_in_group)
            p1.otherStrategy=p2.myStrategy

            p2.otherSubject = str(p1.id_in_group)
            p2.otherStrategy = p1.myStrategy

            strategies = [allc, alld, tft, grim, stft, sgrim, tf2t, grim2, two_tft, random]

            # print("p1.round_number=", p1.round_number-1)
            # print("Sequence:", Constants.seqs[self.session.config['Sequence']-1])

            res = playStrategies(strategies[int(p1.myStrategy)-1], strategies[int(p2.myStrategy)-1], self.session.config['R'], Constants.seqs[self.session.config['Sequence']-1][p1.round_number-1])
            p1.myHistory = res[0]
            p2.myHistory = res[1]
            p1.myPayoffs = res[2]
            p1.otherPayoffs = res[3]
            p2.myPayoffs = res[3]
            p2.otherPayoffs = res[2]
            p1.payoff = res[4]
            p2.payoff = res[5]
            p1.otherHistory = p2.myHistory
            p2.otherHistory = p1.myHistory


            if self.round_number==1 or self.round_number==Constants.num_rounds:

                temp1 = p1.belief.split(',')
                temp1 = temp1[1:]
                temp1 = [int(x) for x in temp1]

                # print(int(self.player.otherStrategy)-1,temp[int(self.player.otherStrategy)-1],100-temp[int(self.player.otherStrategy)-1])
                penalty1 = (100 - temp1[int(p1.otherStrategy) - 1]) * (
                            100 - temp1[int(p1.otherStrategy) - 1]) * 0.02
                # print("Other Strategy:", int(p1.otherStrategy),"Belief:",temp1[int(p1.otherStrategy)-1], "Penalty1:", penalty1)
                for i in range(10):
                    if i != int(p1.otherStrategy) - 1:
                        penalty1 += (temp1[i]) * (temp1[i]) * 0.02
                        # print("i:", i+1,"Belief:",temp1[i],  "Penalty1:", (temp1[i])*(temp1[i])*0.02)

                p1.earnBelief = 400 - penalty1
                p1.participant.vars['EarnBelief' + str(p1.round_number)] = p1.earnBelief
                p1.participant.vars['Matches'] = p1.round_number
                # print("Split beliefs:", temp, " Other strategy:", self.player.otherStrategy,"Penalty:",penalty)

                temp2 = p2.belief.split(',')
                temp2 = temp2[1:]
                temp2 = [int(x) for x in temp2]

                # print(int(self.player.otherStrategy)-1,temp[int(self.player.otherStrategy)-1],100-temp[int(self.player.otherStrategy)-1])
                penalty2 = (100 - temp2[int(p2.otherStrategy) - 1]) * (
                            100 - temp2[int(p2.otherStrategy) - 1]) * 0.02
                # print("Other Strategy:", int(self.player.otherStrategy),"Belief:",temp[int(self.player.otherStrategy)-1], "Penalty:", penalty)
                for i in range(10):
                    if i != int(p2.otherStrategy) - 1:
                        penalty2 += (temp2[i]) * (temp2[i]) * 0.02
                        # print("i:", i+1,"Belief:",temp[i],  "Penalty:", (temp[i])*(temp[i])*0.01)

                p2.earnBelief = 400 - penalty2
                p2.participant.vars['EarnBelief' + str(p2.round_number)] = p2.earnBelief
                p2.participant.vars['Matches'] = p2.round_number
                # print("Split beliefs:", temp, " Other strategy:", self.player.otherStrategy,"Penalty:",penalty)



page_sequence = [

    StrategyChoice,
    BeliefsInstructions,
    Beliefs,
    Message,
    WaitForOthers,
    Match,

]
