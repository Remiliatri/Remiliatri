import logging

# ---------------------------------------------基本参数---------------------------------------------

# 新版本目前支持以下适配器:
# - "yirimirai": mirai的通信框架，YiriMirai框架适配器, 请同时填写下方mirai_http_api_config
# - "nakuru": go-cqhttp通信框架，请同时填写下方nakuru_config
#    如果你用的【gocq】登录，则改成 "nakuru"
msg_source_adapter = "nakuru"

nakuru_config = {
    "host": "localhost",    # go-cqhttp的地址,这个代表本机，不用改！
    "port": 6700, # go-cqhttp的正向websocket端口
    "http_port": 5700,      # go-cqhttp的正向http端口,默认就是，不用改！
    "token": ""             # 若在go-cqhttp的config.yml设置了access_token, 则填写此处，不用改！
}

# 注意: QQ机器人配置不支持热重载及热更新
mirai_http_api_config = {
    "adapter": "WebSocketAdapter",
    "host": "localhost",
    "port": 10081,
    "verifyKey": "yirimirai",
    "qq": 
} #这里填需要挂bot的qq，最好是自己的小号

# [必需] OpenAI的配置，api_key: OpenAI的API Key
# 1.若只有一个api-key，请直接修改以下内容中的"openai_api_key"为你的api-key
# 2.如准备了多个api-key，可以以字典的形式填写，程序会自动选择可用的api-key 
# 3.（非必要选择！）现已支持网络代理，格式："http_proxy": "http://127.0.0.1:7890"   其中7890是你代理软件打开的端口，一般开全局则无需设置
# 4.（非必要选择！）现已支持反向代理，可以添加reverse_proxy字段以使用反向代理，使用反向代理可以在国内使用OpenAI的API，反向代理的配置请参考 ，https://github.com/Ice-Hazymoon/openai-scf-proxy , 格式为： "reverse_proxy": "http://example.com:12345/v1"

openai_config = {
    "api_key": {
        "default": "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",
        },
    "http_proxy": None,
    "reverse_proxy": None    
}

# ---------------------------------------------响应参数---------------------------------------------
# user_name: 管理员(主人)的名字
# bot_name: 机器人的名字
user_name = ''
bot_name = ''

# 每个会话的预设信息，影响所有会话，无视指令重置，这是你机器人的人格
# 使用 !reset 第二人格 ，来使用指定的情景预设重置会话，如果不指定则为default默认的
default_prompt = {
   "default": "",
   "第二人格": "我想让你充当 Linux 终端。我将输入命令，您将回复终端应显示的内容。",
   "第三人格": "我想让你充当英英词典，对于给出的英文单词，你要给出其中文意思以及英文解释，并且给出一个例句，此外不要有其他反馈。",
 } #第一人格建议填写树洞相关的人格设定，如有需要可以添加更多人格（请勿泄露！reset命令给非管理员）

# [必需] 管理员QQ号，用于接收报错等通知及执行管理员级别指令，以下改成你的QQ号，现在支持多个管理员，可以使用list形式设置，例如：admin_qq = [12345678, 87654321]
admin_qq = 

# 群内响应规则，符合此消息的群内消息即使不包含at机器人也会响应
# 支持消息前缀匹配及正则表达式匹配，注意：由消息前缀(prefix)匹配的消息中将会删除此前缀且具有高优先级，而正则表达式(regexp)匹配的消息不会删除匹配的部分 
# 正则表达式简明教程：https://www.runoob.com/regexp/regexp-tutorial.html
response_rules = {
    "at": True,  # 是否响应at机器人的消息，ps：就是群聊艾特会不会回，如果为False则不回
    "prefix": ["/ai", "!ai", "！ai", "ai"],
    "regexp": ["怎么?样.*", "怎么.*", "如何.*", ".*咋办"],
    "random_rate": 0.0,  # 随机响应概率，取值范围 0.0-1.0     0.0为完全不随机响应  1.0响应所有消息, 仅在前几项判断不通过时生效
}

# 消息忽略规则，符合此规则的消息将不会被【响应】，此设置优先级高于response_rules，可用以过滤mirai等其他层级的指令
# 教程 https://github.com/RockChinQ/QChatGPT/issues/165
ignore_rules = {
    "prefix": ["/"],
    "regexp": []
}

# 新版情景预设格式（非必要设置）
# 参考值：旧版本方式：normal | 完整情景：full_scenario
# 新版完整情景：full_scenario或prompts目录下的文件名
# 完整情景预设的格式为JSON，编写方法见scenario目录下的default-template.json ，每个JSON文件都是一个情景预设，文件名即为情景预设的名称，【如果要使用】可先参考群文件json人格设置
preset_mode = "normal"

# 特殊功能1.QChatGPT目录下的【tips.py】打开是修改报错或者超时等回复的消息
# 特殊功能2.QChatGPT目录下的【banlist.py】打开是修改机器人响应禁用列表
# 特殊功能3.QChatGPT目录下的【cmdpriv.json】打开是修改管理员等一些重置指令对外人的权限

# ---------------------------------------------模型参数---------------------------------------------
# 每次向OpenAI接口发送对话记录上下文的字符数
# 最大不超过(4096 - max_tokens)个字符，max_tokens为上述completion_api_params中的max_tokens
# 注意：较大的prompt_submit_length会导致OpenAI账户额度消耗更快
prompt_submit_length = 1024
 
# OpenAI补全API的参数，OpenAI的文档: https://beta.openai.com/docs/api-reference/completions/create
# 请在下方填写模型，程序自动选择接口,现已支持的模型有：
#    'gpt-4'	             -->新出的更强4.0接口，目前版本似乎仅plus会员等可用
#    'gpt-4-0314'
#    'gpt-4-32k'
#    'gpt-4-32k-0314'
#    'gpt-3.5-turbo'                -->这个是默认的3.5接口，使用方法复制到下面的"model"：xxx  ，替换xxx
#    'gpt-3.5-turbo-0301'
#    'text-davinci-003'             -->这个是原来的3.0接口，人格相对好设置，但是token收费会更高
#    'text-davinci-002' 
#    'code-davinci-002' | 'code-cushman-001' | 'text-curie-001' | 'text-babbage-001' | 'text-ada-001'   ....等等、还有一些你可能用不到的模型
completion_api_params = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.6,  # 数值越低得到的回答越理性，取值范围[0, 1]
    "top_p": 1,  # 生成的文本的文本与要求的符合度, 取值范围[0, 1]
    "frequency_penalty": 0.2,
    "presence_penalty": 1.0,
}

# OpenAI的Image API的参数，使用 ！draw xxx描述信息，来获取一张简单的图片
# 具体请查看OpenAI的文档: https://beta.openai.com/docs/api-reference/images/create
image_api_params = {
    "size": "512x512",  # 图片尺寸，支持256x256, 512x512, 1024x1024
}

# 回复绘图时是否包含图片描述
include_image_description = True

# 群内回复消息时是否以@的形式回复提问者，默认为False不开启，如果True，则开启
quote_origin = False

# 消息处理的超时时间，单位为秒
process_message_timeout = 60

# 消息处理超时重试次数
retry_times = 1

# 回复消息时是否显示[GPT]前缀
show_prefix = True

# [暂未实现] 群内会话是否启用多对象名称
# 若不启用，群内会话的prompt只使用user_name和bot_name
multi_subject = False

# 仅在旧版语音包模型时存在时有效！ 否则无视
waifu_voice = 2       # 0 日语标准语气   1 日语活跃语气   2 温柔全能   3 关东腔  


# ---------------------------------------------会话限制---------------------------------------------

# 线程池相关配置，该参数决定机器人可以同时处理几个人的消息，超出线程池数量的请求会被阻塞，不会被丢弃，如果你不清楚该参数的意义，请不要更改
sys_pool_num = 8
# 执行管理员请求和指令的线程池并行线程数量，一般和管理员数量相等
admin_pool_num = 2
# 执行用户请求和指令的线程池并行线程数量，如需要更高的并发，可以增大该值
user_pool_num = 10

# 每个会话的过期时间，单位为秒，原默认值20分钟，即 1200 ,注意这里的数字只能是整数
session_expire_time = 1200

# 会话限速
# 单会话内每分钟可进行的对话次数，若不需要限速，可以设置为一个很大的值
# 默认值60次，基本上不会触发限速
rate_limitation = 60

# 允许等待
# 同一会话内，是否等待上一条消息处理完成后再处理下一条消息
# 若设置为False，若上一条未处理完时收到了新消息，将会丢弃新消息
# 丢弃消息时的提示信息可以在tips.py中修改
wait_last_done = True

# 会话限速策略
# - "wait": 每次对话获取到回复时，等待一定时间再发送回复，保证其不会超过限速均值
# - "drop": 此分钟内，若对话次数超过限速次数，则丢弃之后的对话，每自然分钟重置
rate_limit_strategy = "wait"

# drop策略时，超过限速均值时，丢弃的对话的提示信息，仅当rate_limitation_strategy为"drop"时生效
# 若设置为空字符串，则不发送提示信息
rate_limit_drop_tip = "本分钟对话次数超过限速次数，此对话被丢弃"

# 应用长消息处理策略的阈值
# 当回复消息长度超过此值时，将使用长消息处理策略，如果需要一段话直接说完，则改成一个超大的值
blob_message_threshold = 2000

# 长消息处理策略
# - "image": 将长消息转换为图片发送
# - "forward": 将长消息转换为转发消息组件发送
blob_message_strategy = "forward"

# 文字转图片时使用的字体文件路径，仅当 blob_message_strategy= "image" 策略时生效
# 若在Windows系统下，程序会自动使用Windows自带的微软雅黑字体，如果不是Windows，将禁用文字转图片功能，改为使用转发消息组件
font_path = ""                # 我这里已经把字体压进去了，如果上述长消息处理策略改成image，【你是Linux且指定字体】则  font_path = "./res/simhei.ttf"  

# 是否检查收到的消息中是否包含敏感词
# 若收到的消息无法通过下方指定的敏感词检查策略，则发送提示信息
income_msg_check = False
# 敏感词过滤开关，以同样数量的*代替敏感词回复
# 请在sensitive.json中添加敏感词
sensitive_word_filter = True

# 是否启用百度云内容安全审核，用于接入百度云，从而智能的拦截机器人发出的不合格图片和消息
# 注册方式查看 https://cloud.baidu.com/doc/ANTIPORN/s/Wkhu9d5iy，如果开启 baidu_check = True
baidu_check = False
# 百度云API_KEY 24位英文数字字符串
baidu_api_key = ""
# 百度云SECRET_KEY 32位的英文数字字符串
baidu_secret_key = ""
# 不合规消息自定义返回
inappropriate_message_tips = "[百度云]请珍惜机器人，当前返回内容不合规"

# ---------------------------------------------开发者参数---------------------------------------------

# 单个api-key的费用警告阈值，当使用此api-key进行请求所消耗的费用估算达到此阈值时，会在控制台输出警告并通知管理员
# 若之后还有未使用超过此值的api-key，则会切换到新的api-key进行请求，单位：美元
api_key_fee_threshold = 1.0

# 启动时是否发送赞赏码，这将仅当使用量已经超过2048字时发送
encourage_sponsor_at_start = False

# 是否根据估算的使用费用切换api-key
# 设置为False将只在接口报错超额时自动切换
auto_switch_api_key = False

# 消息处理出错时是否向用户隐藏错误详细信息
# 设置为True时，仅向管理员发送错误详细信息
# 设置为False时，向用户及管理员发送错误详细信息
hide_exce_info_to_user = True

# 是否在启动时进行依赖库更新
upgrade_dependencies = False

# 是否上报统计信息
# 用于统计机器人的使用情况，不会收集任何用户信息
# 仅上报时间、字数使用量、绘图使用量，其他信息不会上报
report_usage = True

# 日志级别
logging_level = logging.INFO
