from otree.api import *




doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class C(BaseConstants):
    NAME_IN_URL = 'trust_game_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Initial amount allocated to each player
    ENDOWMENT1 = cu(45)
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Offer1 = models.CurrencyField(
         min=0,
         max=C.ENDOWMENT1,
         label="请输入你想回馈给参与者1的分数",
         doc="参与者选择回馈的分数"
    )
    Offer2 = models.CurrencyField(
         min=0,
         max=75,
         label="请输入你想回馈给参与者1的分数",
         doc="参与者选择回馈的分数"
    )  
    Offer3 = models.CurrencyField(
         min=0,
         max=30,
         label="请输入你想回馈给参与者1的分数",
         doc="参与者选择回馈的分数"
    )
    Offer4 = models.CurrencyField(
         min=0,
         max=120,
         label="请输入你想回馈给参与者1的分数",
         doc="参与者选择回馈的分数"
    )            
    def role(self):
        return 'player2'





# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

#三种设置

class Offer1(Page):
    form_model = 'player'
    form_fields = ['Offer1']

class Offer2(Page):
    form_model = 'player'
    form_fields = ['Offer2']

class Offer3(Page):
    form_model = 'player'
    form_fields = ['Offer3']

class Offer4(Page):
    form_model = 'player'
    form_fields = ['Offer4']
    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True

class Results(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return {"a" : player.Offer1}
    
class Results2(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer2)
    
class Results3(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer3)

class Results4(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer4)

page_sequence = [
    Offer1,
    ResultsWaitPage,
    Results,
    Offer2,
    ResultsWaitPage,
    Results2,
    Offer3,
    ResultsWaitPage,
    Results3,
    Offer4,
    ResultsWaitPage,
    Results4,
]
