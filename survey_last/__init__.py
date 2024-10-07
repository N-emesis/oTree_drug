from otree.api import *
from otree.api import widgets



class C(BaseConstants):
    NAME_IN_URL = 'survey_last'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='你的年龄是多少？', min=13, max=125)
    name = models.StringField(label='请输入你的名字')
    # drugs_used = models.LongStringField(
    #     label="是否曾吸食以下毒品？(可多选)",
    #     choices=[
    #         '海洛因', 
    #         '麻古', 
    #         '冰毒', 
    #         '麻黄素', 
    #         '大麻', 
    #         '美沙酮'
    #     ],
    #     widget=widgets.CheckboxSelectMultiple
    # )
    drugs_used_heroin = models.BooleanField(label='使用过海洛因',doc="使用过海洛因",choices=[[True,'是'],[False,'否']])
    drugs_used_methamphetamine = models.BooleanField(label='使用过冰毒',doc="使用过冰毒",choices=[[True,'是'],[False,'否']])
    drugs_used_mdma = models.BooleanField(label='使用过麻古',doc="使用过麻古",choices=[[True,'是'],[False,'否']])
    drugs_used_marijuana = models.BooleanField(label='使用过大麻',doc="使用过大麻",choices=[[True,'是'],[False,'否']])
    drugs_used_amphetamine = models.BooleanField(label='使用过麻黄素',doc="使用过麻黄素",choices=[[True,'是'],[False,'否']])
    drugs_used_methadone = models.BooleanField(label='使用过美沙酮',doc="使用过美沙酮",choices=[[True,'是'],[False,'否']])

    last_use_year = models.IntegerField(label="上一次吸食年份")
    usage_count = models.IntegerField(label="吸食次数")
    usage_years = models.IntegerField(label="吸食年限")


    #毒品渴望量表
    craving_1 = models.IntegerField(label="如果现在使用毒品，我的思路或头脑会更清晰。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_2 = models.IntegerField(label="我对毒品的渴望非常强烈，难以控制。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_3 = models.IntegerField(label="我在想方设法得到毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_4 = models.IntegerField(label="如果送我一些毒品，我会立即使用。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_5 = models.IntegerField(label="现在我非常需要毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_6 = models.IntegerField(label="现在使用毒品的话，我会觉得自己很能干。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_7 = models.IntegerField(label="如果毒品就摆在我面前，很难克制自己不用。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_8 = models.IntegerField(label="为了得到毒品，我可以做任何事。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_9 = models.IntegerField(label="如果现在能用毒品，我将更好处理各种问题。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_10 = models.IntegerField(label="我现在有一种迫切要用毒品的冲动。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_11 = models.IntegerField(label="如果我有毒品，我不能控制使用的量。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_12 = models.IntegerField(label="在今后很长一段时间内，没毒品我也过得去。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_13 = models.IntegerField(label="如果能用毒品，我的脾气不会那么暴躁。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_14 = models.IntegerField(label="如果能用毒品，我将感到精力充沛。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_15 = models.IntegerField(label="我现在心里只想着毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_16 = models.IntegerField(label="目前我不需要毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_17 = models.IntegerField(label="此刻我抵挡不住毒品的诱惑。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_18 = models.IntegerField(label="目前最美好的事情就是用毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_19 = models.IntegerField(label="拒绝使用毒品是非常容易的。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_20 = models.IntegerField(label="只要有可能，我就用毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_21 = models.IntegerField(label="如果我自己有毒品，我一定会用。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_22 = models.IntegerField(label="此刻使用毒品，我就不会那么疲劳。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_23 = models.IntegerField(label="如果现在用一点毒品，我将一发不可收拾地继续用。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_24 = models.IntegerField(label="现在我不再想用毒品。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    craving_25 = models.IntegerField(label="如果现在我有毒品，我可能不用。", choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


# FUNCTIONS
# PAGES
class page_2(Page):
    form_model = 'player'
    form_fields = ['craving_1', 'craving_2', 'craving_3', 'craving_4', 'craving_5', 
'craving_6', 'craving_7', 'craving_8', 'craving_9', 'craving_10', 
'craving_11', 'craving_12', 'craving_13', 'craving_14', 'craving_15', 
'craving_16', 'craving_17', 'craving_18', 'craving_19', 'craving_20', 
'craving_21', 'craving_22', 'craving_23', 'craving_24', 'craving_25']


class page_1(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'drugs_used_heroin','drugs_used_methamphetamine','drugs_used_mdma','drugs_used_marijuana','drugs_used_amphetamine','drugs_used_methadone','last_use_year','usage_count','usage_years']

class page_3(Page):
    pass


page_sequence = [page_1,page_2,page_3]
