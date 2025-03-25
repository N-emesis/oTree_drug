from otree.api import *




doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class C(BaseConstants):
    NAME_IN_URL = 'trust_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    # Initial amount allocated to each player
    ENDOWMENT = cu(50)
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    kept = models.CurrencyField(
         choices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
         label="你向参与者2分配的分数会翻三倍给予参与者2，请选择你本轮想要分配给参与者2的分数",
         doc="投资者选择投资的分数"
    )
    def role(self):
        return 'dictator'



def set_payoffs(group: Group):
        Player.payoff = Player.kept





# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Offer(Page):
    form_model = 'player'
    form_fields = ['kept']
    def vars_for_template(self):
        # 在模板中传递等待时间
        return dict(wait_time=5)

    
    # @staticmethod
    # def is_displayed(player:Player):
    #     return player.id_in_group == 1  # 只有独裁者才能看到分配页面

class ResultsWaitPage(WaitPage):
    body_text = "请稍等，其他参与者正在进行决策。"
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass

page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results,
]
