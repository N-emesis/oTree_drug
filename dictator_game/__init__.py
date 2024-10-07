from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'dictator_game'
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
    kept = models.CurrencyField(
         min=0, 
         max=C.ENDOWMENT,
         label="请输入你本轮想要保留的分数",
         doc="独裁者选择保留的分数"
    )
    def role(self):
        return 'dictator'


def set_payoffs(group: Group):
        Player.payoff = Player.kept

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
    form_fields = ['kept']
    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(Offer = C.ENDOWMENT - player.kept)


page_sequence = [ParticipantNumberInput, Introduction, Offer, ResultsWaitPage, Results]





