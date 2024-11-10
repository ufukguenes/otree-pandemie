from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pandemie_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    player_id =  models.IntegerField(initial=1)


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass
    

class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
