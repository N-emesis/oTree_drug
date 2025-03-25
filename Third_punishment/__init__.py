from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'Third_punishment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Initial amount allocated to each player
    ENDOWMENT = cu(50)
    #MULTIPLIER = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # random_value = models.IntegerField()
    Offer1 = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你要付出的分数",
         doc="观察者付出的分数"
    )
    Offer2 = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你要付出的分数",
         doc="观察者付出的分数"
    )
    Offer3 = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你要付出的分数",
         doc="观察者付出的分数"
    )
    Offer4 = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你要付出的分数",
         doc="观察者付出的分数"
    )
    Offer5 = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你要付出的分数",
         doc="观察者付出的分数"
    )
    # Offer1 = models.CurrencyField(
    #      choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    #      label="你向参与者2分配的分数会翻三倍给予参与者2，请选择你本轮想要分配给参与者2的分数",
    #      doc="投资者选择投资的分数"
    # )
    # def role(self):
    #     return 'dictator'



# def set_payoffs(group: Group):
#         Player.payoff = Player.kept





# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
class MyWaitPage(Page):
    timeout_seconds = 10
    def vars_for_template(self):
        return {}
    

class Offer1(Page):
    # def vars_for_template(player: Player):
    #     # 在每次加载页面时生成一个新的随机数
    #     random_value = random.choice([0, 10, 20, 30, 40, 50])
    #     player.random_value = random_value
        
    #     # 把玩家的 random_value 传递给模板
    #     return {
    #         'random_value': player.random_value
    #     }
    
    form_model = 'player'
    form_fields = ['Offer1']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)
    
class Offer2(Page):
    form_model = 'player'
    form_fields = ['Offer2']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)
class Offer3(Page):
    form_model = 'player'
    form_fields = ['Offer3']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)
class Offer4(Page):
    form_model = 'player'
    form_fields = ['Offer4']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)
class Offer5(Page):
    form_model = 'player'
    form_fields = ['Offer5']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)
    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class ResultsWaitPage(WaitPage):
    body_text = "请稍等，其他参与者正在进行决策。"
    def after_all_players_arrive(group: Group):
        pass


class Result1(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer1 * 2)
    
class Result2(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer2 * 2)
class Result3(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer3 * 2)
class Result4(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer4 * 2)
class Result5(Page):
    @staticmethod
    def vars_for_template(player:Player):
        # group = player.group
        return dict(a = player.Offer5 * 2)

page_sequence = [
    Introduction,
    MyWaitPage,
    Offer1,
    ResultsWaitPage,
    Result1,
    MyWaitPage,
    Offer2,
    ResultsWaitPage,
    Result2,
    MyWaitPage,
    Offer3,
    ResultsWaitPage,
    Result3,
    MyWaitPage,
    Offer4,
    ResultsWaitPage,
    Result4,
    MyWaitPage,
    Offer5,
    ResultsWaitPage,
    Result5,
]
