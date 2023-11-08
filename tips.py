import config
# ---------------------------------------------自定义提示语---------------------------------------------

# 消息处理出错时向用户发送的提示信息，仅当config.py中hide_exce_info_to_user为True时生效
# 设置为空字符串时，不发送提示信息
alter_tip_message = ''

# drop策略时，超过限速均值时，丢弃的对话的提示信息，仅当config.py中rate_limitation_strategy为"drop"时生效
# 若设置为空字符串，则不发送提示信息
rate_limit_drop_tip = ""

# 只允许同时处理一条消息时，新消息被丢弃时的提示信息
# 当config.py中的wait_last_done为False时生效
# 若设置为空字符串，则不发送提示信息
message_drop_tip = "【检测到时空信号交集，请等待返回信号处理完成】，"

# 指令！help帮助消息
# config.py,line:279
# pkg/qqbot/process.py,line:122
help_message = """此机器人通过调用大型语言模型生成回复，不具有情感。
你可以用自然语言与其交流，回复的消息中[GPT]开头的为模型生成的语言，[bot]开头的为程序提示。
欢迎到github.com/RockChinQ/QChatGPT 给个star"""

# 私聊消息超时提示
reply_message = ""
# 群聊消息超时提示
replys_message = "【检测到时空风暴影响，返回信号被确认超时】"

# 指令权限不足提示
command_admin_message = "【权限不足】"
# 指令无效提示
command_err_message = "【权限无效】"

# 会话重置提示
command_reset_message = "【已检测到重置，那就让我们再次相遇吧！】"
command_reset_name_message = "【已检测到重置，那就让我们再次相遇吧！】使用场景预设:"
