from otree.api import *
from logic import run_step

doc = """
    Simple implementation for the pandemic experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'pandemie_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    player_id =  models.IntegerField(initial=1)
    budget = models.IntegerField(initial=100)
    new_money = models.IntegerField(initial=0)

    num_neighbours = models.IntegerField(initial=10)
    num_infected_neighbours = models.IntegerField(initial=0)

    is_infested = models.BooleanField(
        initial=False
    ) 

    is_protected = models.BooleanField(
        label="Entscheidung:",
        choices=[
            [True, 'schützen'],
            [False, 'nicht schützen'],
        ]
    )
    


# PAGES
class WelcomePage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class DecisionPage(Page):
    form_model = "player"
    form_fields = ["is_protected"]
    timeout_seconds = None

    def vars_for_template(player):
        if player.round_number > 1:
                prev_player = player.in_previous_rounds()[-1]
        else:
            prev_player = player
        return dict (
             prev_player_is_infested = prev_player.is_infested,
             prev_player_num_infected_neighbours =  prev_player.num_infected_neighbours,
             prev_player_num_neighbours = prev_player.num_neighbours,
             prev_player_budget = prev_player.budget
             )

    @staticmethod
    def before_next_page(player, timeout_happened):
            if player.round_number > 1:
                prev_player = player.in_previous_rounds()[-1]
            else:
                prev_player = player
            player.budget, player.new_money, player.num_infected_neighbours, player.num_neighbours, player.is_infested, player.is_protected = run_step(prev_player.budget, prev_player.new_money, prev_player.num_infected_neighbours, prev_player.num_neighbours, prev_player.is_infested, prev_player.is_protected)
    
    
class TotalPayoff(Page):
    pass


class ExitPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [WelcomePage, DecisionPage, TotalPayoff, ExitPage]