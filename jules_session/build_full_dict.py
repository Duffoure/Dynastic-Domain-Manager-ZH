import json

# We will generate a complete dictionary for all 1400 keys
tr = {}

def a(k, v):
    tr[k] = v

# Load Part 1
with open('tr_part1.json', 'r', encoding='utf-8') as f:
    tr.update(json.load(f))

# Part 2: Dynasty & succession, review, military, construction, rules
a("ddm_manager.2000.t", "宗族与继承")
a("ddm_manager.2000.desc", "继承与封地现在被视为同一系统的组成部分。在均分继承下，默认平衡政策首先将过剩安置限制在CK3的实际合法继承人范围内，随后利用才能、家族重视、性情和公平度来决定每人接收多少。它还可以维持宗族同盟，并在统治者更迭后运行一键清理。\n\n#help 本公署并不替代CK3的继承引擎。它向引擎询问继承人是谁，因此限男性、限女性、剥夺继承权及类似资格规则会自动塑造首选候选池。#!")
a("ddm_manager.2000.a", "打开继承简报。")
a("ddm_manager.2000.a.flavor", "查看我当前的继承法、主要继承人、预计头衔数量以及领地管理器正在使用的规则。")
a("ddm_manager.2000.b", "审查并整理在世宗族。")
a("ddm_manager.2000.b.flavor", "单批次评估整个宗族，并从最弱的合格成员开始向上行动。")
a("ddm_manager.2000.c", "刷新宗族同盟。")
a("ddm_manager.2000.c.flavor", "根据我的同盟政策创建缺失的同盟，而不是在每次封赏后都要求手动外交。")
a("ddm_manager.2000.d", "运行继位后清理。")
a("ddm_manager.2000.d.flavor", "重新检查我的新个人领地，组织继承的高级头衔，刷新宗族同盟，并准备一份全新的继承报告。")

a("ddm_manager.2010.t", "继承总簿")
a("ddm_manager.2010.desc", "文书官在角色继承列表中识别出 #V [GetPlayer.MakeScope.Var('ddm_succession_heir_count').GetValue|0]#! 名当前继承人，包括主继承人身后的 #V [GetPlayer.MakeScope.Var('ddm_partition_secondary_heirs').GetValue|0]#! 名次要继承人。\n")
a("ddm_manager.2010.law_confederate", "\n当前领地继承：#V 联盟均分继承。#! #warning 在常规规则允许时，新设立的同阶头衔可能会在死亡时自动创建，因此表面整洁的领地依然可能分裂。#!")
a("ddm_manager.2010.law_partition", "\n当前领地继承：#V 均分继承。#! 领地在合格继承人之间分割，不会产生联盟均分继承的额外头衔创建。")
a("ddm_manager.2010.law_high_partition", "\n当前领地继承：#V 高阶均分继承。#! 主继承人获得较大的首份份额，其余部分再行分割。")
a("ddm_manager.2010.law_single", "\n当前领地继承：#V 单一继承人。#! 在此法律下，均分预留启发式规则的重要性大为降低。")
a("ddm_manager.2010.law_other", "\n当前继承法不属于本公署识别的标准均分法律之一；报告仅供参考。")
a("ddm_manager.2010.heir1", "\n第一继承人：#V [ddm_succession_heir_1.GetName]#! — 目前是我持有的 #V [GetPlayer.MakeScope.Var('ddm_primary_heir_expected_titles').GetValue|0]#! 个头衔的继承人。")
a("ddm_manager.2010.heir2", "\n第二继承人：#V [ddm_succession_heir_2.GetName]#! — 目前是我持有的 #V [GetPlayer.MakeScope.Var('ddm_second_heir_expected_titles').GetValue|0]#! 个头衔的继承人。")
a("ddm_manager.2010.heir3", "\n第三继承人：#V [ddm_succession_heir_3.GetName]#! — 目前是我持有的 #V [GetPlayer.MakeScope.Var('ddm_third_heir_expected_titles').GetValue|0]#! 个头衔的继承人。")
a("ddm_manager.2010.a", "更改继承规划政策。")
a("ddm_manager.2010.a.flavor", "决定头衔分配应当忽略继承人、仅保护主继承人、资助次要均分继承人，还是更强烈地偏向主继承。")

a("ddm_manager.succession_policy_1", "\n领地管理器政策：#V 忽略继承。#! 继承人身份不会影响受封者排名（独立的玩家继承人保护除外）。")
a("ddm_manager.succession_policy_2", "\n领地管理器政策：#V 保护主继承人。#! 除非手动偏好，主继承人在自动封赏中受到强烈冷落。")
a("ddm_manager.succession_policy_3", "\n领地管理器政策：#V 平衡均分继承人。#! 我持有头衔的去重当前继承人成为首选池。每次封赏都会根据可遗传资质、成年才能（如适用）、家族重视、政治性情以及当前批次中每已接收一个头衔扣除 #V -65#! 分重新排名。主继承人不会被自动排除，因此两个合格的儿子可以实际分割一份大额过剩地产，而不是一人隐藏在继承人保护之后。")
a("ddm_manager.succession_policy_4", "\n领地管理器政策：#V 主继承最大化。#! 使用相同的均分感知行为，并带有最强烈的意图将次要继承人资助安排在核心之外。")

a("ddm_manager.0104.t", "宗族同盟已刷新")
a("ddm_manager.0104.desc", "公署与符合当前同盟政策的有领地宗族成员创建了 #V [GetPlayer.MakeScope.Var('ddm_last_alliances_created').GetValue|0]#! 个新同盟。现有同盟保持原样。")
a("ddm_manager.2020.t", "新朝秩序已确立")
a("ddm_manager.2020.desc", "继位后处理分配了 #V [GetPlayer.MakeScope.Var('ddm_last_baronies_granted').GetValue|0]#! 个次级男爵领和 #V [GetPlayer.MakeScope.Var('ddm_last_counties_granted').GetValue|0]#! 个伯爵领，随后安置了 #V [GetPlayer.MakeScope.Var('ddm_last_duchies_granted').GetValue|0]#! 个公爵领、#V [GetPlayer.MakeScope.Var('ddm_last_kingdoms_granted').GetValue|0]#! 个王国和 #V [GetPlayer.MakeScope.Var('ddm_last_empires_granted').GetValue|0]#! 个帝国。任何配置的宗族同盟刷新均推迟至次日以单个简明事件执行，而不是在头衔封赏循环内部运行。\n\n#help 这有意设计为一个按钮而非后台自动化：继位可能充满混乱，玩家保留对公署何时重组新朝的最终决定权。#!")
a("ddm_manager.2020.a", "阅读最新的继承总簿。")

# Dynasty review
a("ddm_manager.0200.t", "审查在世宗族")
a("ddm_manager.0200.desc", "我的每位在世宗族成员均可接受评估——新生儿、孩童、青少年、成年人、有领地或无领地。公署现已使用与行动相同的数值构建了固定名册。\n\n在世 #V [GetPlayer.MakeScope.Var('ddm_purge_living_total').GetValue|0]#! 名宗族成员中，目前有 #V [GetPlayer.MakeScope.Var('ddm_purge_candidate_count').GetValue|0]#! 人被标记待处理。\n")
a("ddm_manager.purge_stage_1", "\n当前标准：#V 保存 — 评分低于 40。#! 只有严重负资产才会落入线外。")
a("ddm_manager.purge_stage_2", "\n当前标准：#V 宽容 — 评分低于 75。#! 弱势支系将被审查，但普通的有用亲属通常能够存活。")
a("ddm_manager.purge_stage_3", "\n当前标准：#V 平衡 — 评分低于 110。#! #P 默认。#! 资质平平的平庸成年人无需特殊血统特质即可存活；良好遗传特质使生存愈发容易。")
a("ddm_manager.purge_stage_4", "\n当前标准：#V 挑选 — 评分低于 155。#! 宗族成员被期望展现出强大的继承资质、实在的治理能力，或令人信服的组合。")
a("ddm_manager.purge_stage_5", "\n当前标准：#V 高标准 — 评分低于 210。#! 需要强大的能力；无单一特定特质是强制要求的。")
a("ddm_manager.purge_stage_6", "\n当前标准：#V 精英 — 评分低于 280。#! 期望卓越的继承品质或卓越的履历能力。")
a("ddm_manager.purge_stage_7", "\n当前标准：#V 巅峰 — 评分低于 360。#! 只有宗族中最具价值的继承、能力与地位组合才有可能达标。")
a("ddm_manager.purge_method_1", "\n当前行动：#V 仅剥夺继承权。#!")
a("ddm_manager.purge_method_2", "\n当前行动：#V 剥夺领地头衔，随后剥夺继承权。#!")
a("ddm_manager.purge_method_3", "\n当前行动：#N 致命整理 — 剥夺符合条件的领地头衔，随后处决。#!")
a("ddm_manager.floor_0", "\n最小宗族底线：#N 无。#!")
a("ddm_manager.floor_4", "\n最小宗族底线：#V 4 名在世成员。#!")
a("ddm_manager.floor_8", "\n最小宗族底线：#V 8 名在世成员。#!")
a("ddm_manager.floor_12", "\n最小宗族底线：#V 12 名在世成员。#!")
a("ddm_manager.0200.a", "选择宗族标准。")
a("ddm_manager.0200.a.flavor", "设置在任何人被标记待行动之前评估要求有多高。")
a("ddm_manager.0200.b", "选择“整理”的含义。")
a("ddm_manager.0200.b.flavor", "将质量门槛与后果区分开来：剥夺继承权、剥夺头衔与继承权，或致命行动。")
a("ddm_manager.0200.c", "审查命令并继续。")
a("ddm_manager.0200.c.flavor", "在批次行动开始前展示当前候选人数。")

a("ddm_manager.0210.t", "设置宗族标准")
a("ddm_manager.0210.desc", "公署不再将神圣血统、纯血、天才或任何其他单一特质视为及格/不及格的硬门槛。每位宗族成员获得一个加权总分。对于遗传特质，名册在Paradox提供处复制原版统治者设计师花费；成年才能和家族重视随后分别提供贡献。#P 平衡是默认设置#!，因此新开始的 867 或 1066 宗族不会始于不可能的血统标准之下。")
a("ddm_manager.0210.a", "保存 — 门槛 40。")
a("ddm_manager.0210.b", "宽容 — 门槛 75。")
a("ddm_manager.0210.c", "平衡 — 门槛 110。（默认）")
a("ddm_manager.0210.d", "挑选 — 门槛 155。")
a("ddm_manager.0210.e", "高标准 — 门槛 210。")
a("ddm_manager.0210.f", "精英 — 门槛 280。")
a("ddm_manager.0210.g", "巅峰 — 门槛 360。")

a("ddm_manager.0220.t", "定义整理行动")
a("ddm_manager.0220.desc", "排名体系与针对低于该体系者采取的行动是完全分离的。这使得相同的宗族评估能够指导土地和继承规划，而无需强制采取致命行动。")
a("ddm_manager.0220.a", "剥夺门槛下方者的继承权。")
a("ddm_manager.0220.b", "剥夺其领地头衔并剥夺继承权。")
a("ddm_manager.0220.c", "剥夺其领地头衔并处决。")

a("ddm_manager.0230.t", "我面前的名册")
a("ddm_manager.0230.desc", "名册在 #V [GetPlayer.MakeScope.Var('ddm_purge_living_total').GetValue|0]#! 名在世宗族成员中包含 #V [GetPlayer.MakeScope.Var('ddm_purge_candidate_count').GetValue|0]#! 名目标。#V [GetPlayer.MakeScope.Var('ddm_purge_standard_survivor_count').GetValue|0]#! 人目前高于所选评分门槛。#V [GetPlayer.MakeScope.Var('ddm_purge_protected_count').GetValue|0]#! 人被排除，因为是我、手动受保护者，或受保护的玩家继承人；#V [GetPlayer.MakeScope.Var('ddm_purge_already_satisfied_count').GetValue|0]#! 人已满足所选后果（例如已剥夺继承权）。\n\n#help 无需任何特定的血统特质。天才贡献 240 点原版统治者设计师点数，聪明 160，敏捷 80；赫拉克勒斯/亚马逊 180，强健 120，健壮 60；倾国倾城 120，英俊/秀丽 80，姣好 40。教育等级贡献其原版的 0/20/40/80/150 成本。成年能力、政治安全和家族重视是独立的上下文衡量指标，而非凭空捏造的“官方特质”权重。#!\n\n#warning 名册在执行前即已固定。在我确认后，行动不会重新计算家族重视并悄悄更改列表。#!")
a("ddm_manager.0230.a", "执行宗族审查。")
a("ddm_manager.0230.a.flavor", "一条命令即可处理整个合格列表；我不会被迫为每个亲属重复返回菜单。")
a("ddm_manager.0230.b", "暂不执行。")

a("ddm_manager.0240.t", "宗族审查结束")
a("ddm_manager.0240.desc", "命令开始于 #V [GetPlayer.MakeScope.Var('ddm_purge_candidate_count').GetValue|0]#! 名登记目标。公署针对其中 #V [GetPlayer.MakeScope.Var('ddm_last_purged').GetValue|0]#! 人采取了行动。#V [GuiScope.SetRoot(GetPlayer.MakeScope).ScriptValue('ddm_purge_unprocessed_value')|0]#! 人保持未处理状态，通常是因为最小在世宗族底线阻止了整理。任何收回的地产随后归还给常规领地计划。")
a("ddm_manager.0240.a", "再次审查宗族公署。")

a("ddm_manager.0300.t", "宗族价值评估")
a("ddm_manager.0300.desc", "文书官将 [ddm_subject.GetName] 的卷宗呈在我面前。\n\n特质价值：#V [GuiScope.SetRoot(ddm_subject.MakeScope).ScriptValue('ddm_quality_trait_value')|0]#!\n教育价值：#V [GuiScope.SetRoot(ddm_subject.MakeScope).ScriptValue('ddm_education_trait_value')|0]#!\n治理才能：#V [GuiScope.SetRoot(ddm_subject.MakeScope).ScriptValue('ddm_governance_merit_value')|0]#!\n宗族整体价值：#V [GuiScope.SetRoot(ddm_subject.MakeScope).ScriptValue('ddm_dynastic_value')|0]#!\n政治安全：#V [GuiScope.SetRoot(ddm_subject.MakeScope).AddScope('ddm_actor',GetPlayer.MakeScope).ScriptValue('ddm_loyalty_value')|0]#!\n家族重视：#V [ddm_subject.MakeScope.Var('ddm_family_regard').GetValue|0]#!\n\n#help 在CK3提供数据处，特质价值对先天/身体特质复制了原版统治者设计师的花费。教育价值同样使用官方教育等级花费：0/20/40/80/150。治理才能随后加入适度的已培养技能组件；CK3没有官方的通用统治者才能公式，因此该部分是明确透明的DDM政策，而非伪装成原版。政治安全读取CK3自己的AI性格轴线——正直、同情、理性、贪婪、报复、果敢与精力——再加上该人物与我的关系。#!")

with open('tr_part2.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f"Part 2 saved: {len(tr)} total items so far")
