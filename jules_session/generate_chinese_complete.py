import re

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+)(:\d*)\s*"(.*)"\s*$')

# We will construct a mapping of exact translated strings or python translation logic
tr = {}

def add(k, v):
    tr[k] = v

# --- Decisions & Interactions ---
add("game_rule_category_ddm", "宗族领地管理器")
add("decision_group_type_ddm_domain_management_group", "宗族领地管理")
add("ddm_domain_management_group", "宗族领地管理")

add("ddm_open_manager_decision", "管理宗族领地")
add("ddm_open_manager_decision_desc", "开启常设宗族行政机构，统一管理头衔、继承、军事基础设施和家族政策。")
add("ddm_open_manager_decision_tooltip", "打开宗族领地公署。各项事务已按部门分组，以便连续处理多项任务而无需重复打开决策。")
add("ddm_open_manager_decision_confirm", "进入公署")

add("ddm_assess_dynasty_member_interaction", "评估宗族价值")
add("ddm_assess_dynasty_member_interaction_desc", "让内廷评估该宗族成员的血统、能力、性情、忠诚度以及在家族中的地位。")
add("ddm_protect_dynasty_member_interaction", "保护免受自动化管理")
add("ddm_protect_dynasty_member_interaction_desc", "将该宗族成员排除在自动化整理与领地分配行动之外。")
add("ddm_unprotect_dynasty_member_interaction", "取消自动化保护")
add("ddm_unprotect_dynasty_member_interaction_desc", "允许领地管理器再次对该宗族成员进行常规考量。")
add("ddm_favor_for_land_interaction", "优先分封土地")
add("ddm_favor_for_land_interaction_desc", "指示宗族公署在有合适头衔可用时强烈优先考虑此人。")
add("ddm_never_grant_land_interaction", "绝不分封土地")
add("ddm_never_grant_land_interaction_desc", "禁止自动领地管理器向此人授予任何头衔。")
add("ddm_clear_land_preference_interaction", "清除土地偏好")
add("ddm_clear_land_preference_interaction_desc", "取消在土地分配系统中对此人的特殊优先或排除指令。")
add("ddm_protect_holding_interaction", "保护个人地产")
add("ddm_protect_holding_interaction_desc", "选择我个人持有的一处伯爵领或次级男爵领并锁定在受保护领地中。过剩分配器绝不会分出手动受保护的地产。此头衔选择器可从我自己的肖像或当前玩家继承人处打开；点击的人物并非接收者。")
add("ddm_unprotect_holding_interaction", "取消保护个人地产")
add("ddm_unprotect_holding_interaction_desc", "选择我手动受保护的一处地产，恢复其常规优化考量。头衔选择器可从我的肖像或当前玩家继承人处打开。")
add("ddm_prioritize_holding_for_distribution_interaction", "优先分出地产")
add("ddm_prioritize_holding_for_distribution_interaction_desc", "选择我的一处地产并将其标记为预定放弃土地。除非是首都或后来受到保护，否则过剩管理器会在让出优化器选定的土地之前先放弃此地产。")
add("ddm_clear_holding_distribution_priority_interaction", "清除地产分出优先级")
add("ddm_clear_holding_distribution_priority_interaction_desc", "选择先前标记为优先分出的地产并移除该指令。")
add("ddm_reserve_title_for_recipient_interaction", "为候选人预留头衔")
add("ddm_reserve_title_for_recipient_interaction_desc", "选择我的一处直属头衔并为该人物预留。有效的预留会在普通评分之前处理。王室领地保护、首都、宗教头衔限制、阶衔限制以及CK3常规分封合法性依然适用。")
add("ddm_clear_title_reservation_interaction", "清除头衔预留")
add("ddm_clear_title_reservation_interaction_desc", "选择目前为此人物预留的头衔，恢复其普通按分分配状态。")

add("ddm_manager.close", "到此为止。")
add("ddm_manager.back", "返回。")
add("ddm_manager.main", "返回主公署。")
add("ddm_manager.continue_realm", "继续处理领地与头衔。")
add("ddm_manager.continue_dynasty", "继续处理宗族与继承。")
add("ddm_manager.continue_military", "继续处理军事与建设。")

