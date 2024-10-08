from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'dictator_game_2'
    PLAYERS_PER_GROUP = None  # 每组1名玩家
    NUM_ROUNDS = 2         # 实验轮数，可以更改为多轮
    ENDOWMENT = cu(50)      # 独裁者每轮的初始分数

class Subsession(BaseSubsession):
    def creating_session(self):
        pass

class Group(BaseGroup):
    pass
    # kept = models.CurrencyField(
    #     min=0, 
    #     max=C.ENDOWMENT,
    #     doc="独裁者选择保留的分数"
    # )


class Player(BasePlayer):
    participant_number = models.StringField(
        label="请输入您的号码",
        doc="玩家输入的号码"
    )
    Offer = models.CurrencyField(
         min=0, 
         max=C.ENDOWMENT,
         label="请输入你本轮想给参与者2分配的分数",
         doc="独裁者分配给参与者2的分数"
    )
    def role(self):
        return 'dictator'


def set_payoffs(group: Group):
        Player.payoff = Player.Offer

#页面

class ParticipantNumberInput(Page):
    form_model = 'player'
    form_fields = ['participant_number']

    def is_displayed(self):
        return self.round_number == 1  # 仅在第一轮显示号码输入页面


class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Offer(Page):
    form_model = 'player'
    form_fields = ['Offer']
    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class TimedWaitPage(Page):
    wait_for_all_groups = True
    

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(kept = C.ENDOWMENT - player.Offer)


page_sequence = [ Introduction, Offer, ResultsWaitPage, TimedWaitPage, Results]





