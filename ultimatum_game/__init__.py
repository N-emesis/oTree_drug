from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = 'ultimatum_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    # Initial amount allocated to each player
    ENDOWMENT = cu(50)
    # RANDOM = [0, 5, 10, 15, 20, 25, 30]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Offer = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="请选择你本轮想要分配给参与者2的分数",
         doc="提议者选择分配给接收者的分数"
    )
    accept_offer = models.BooleanField(
        choices=[
            (True, '接受分配'),
            (False, '拒绝分配')
        ],
        widget=widgets.RadioSelect,
        label="请决定是否接受提议者的分配"
    )
    random_value = models.IntegerField()
    
    # def set_random_value(player):
    #     player.random_value = random.choice([0, 5, 10, 15, 20, 25, 30])



# def set_payoffs(group: Group):
#         Player.payoff = Player.Offer





# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Offer(Page):
    form_model = 'player'
    form_fields = ['Offer']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)

    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class Accept(Page):
    def vars_for_template(player: Player):
        # 在每次加载页面时生成一个新的随机数
        random_value = random.choice([0, 5, 10, 15, 20, 25, 30])
        player.random_value = random_value
        
        # 把玩家的 random_value 传递给模板
        return {
            'random_value': player.random_value
        }
    form_model = 'player'
    form_fields = ['accept_offer']

class Result2(Page):
    def vars_for_template(player: Player):
        accept1 = player.accept_offer
        # 获取提议者的分配金额（从之前的随机值中获取）
        offer_amount = player.random_value
        # 如果回应者接受分配，提议者和回应者的得分
        if accept1:
            proposer_final = C.ENDOWMENT - offer_amount  # 提议者的最终分数
            responder_final = offer_amount  # 回应者的最终分数
        else:
            proposer_final = 0
            responder_final = 0
        
        # 将这些变量传递给模板
        return {
            'accept_offer': accept1,
            'offer_amount': offer_amount,
            'proposer_final': proposer_final,
            'responder_final': responder_final,
        }
        # 清除 accept_offer 的值


    
    

class ResultsWaitPage(WaitPage):
    body_text = "请稍等，其他参与者正在进行决策。"
    def after_all_players_arrive(group: Group):
        Player.payoff = Player.Offer
        

class Results(Page):
    pass

page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Accept,
    ResultsWaitPage,
    Result2,
    #Results,
]
