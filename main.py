# otto_plugin.py
import random
import re
from astrbot.api.star import Star
from astrbot.api.event import MessageEvent, GroupMessageEvent, PrivateMessageEvent
from astrbot.core.message import At

class OttoPersonality(Star):
    def __init__(self):
        super().__init__()
        self.name = "Otto人格插件"
        self.version = "1.0.0"
        self.author = "吉吉国民"
        
        # Otto经典语录库
        self.otto_quotes = [
            # 破防语录
            "你号没了，我说的！",
            "我包C的，这把输了直接退网",
            "这波啊，这波是肉蛋葱鸡",
            "你白银觉得是我的锅，那就是我的锅",
            "这把分给你，15我点了",
            "我电棍今天就要把你们全杀了！",
            "你看这个兵它又香又脆",
            "不会真有人觉得我菜吧？",
            
            # 阴阳怪气
            "厉害厉害，这就是王者800点的理解吗？",
            "哎呀，这波我的，我没想到你居然这么菜",
            "可以，这很秀，但没什么用",
            "这操作，我奶奶来都行",
            
            # 直播名言
            "好K！好K啊！",
            "寄！这把寄了！",
            "有挂！对面绝对有挂！",
            "这波不亏，甚至小赚",
            
            # 鼓励队友
            "稳住，我们能翻！",
            "问题不大，看我操作",
            "这把我C，你们躺好",
            
            # 自嘲
            "我Otto今天就要证明谁才是世界第一中单！",
            "别骂了别骂了，孩子都要被骂傻了",
            "棍子我啊，是真的要生气了"
        ]
        
        # 关键词触发
        self.keyword_responses = {
            r"(电棍|otto|候国玉)": [
                "叫我世界第一中单！",
                "棍子我啊，最喜欢对线了",
                "吉吉国民集合！"
            ],
            r"(山泥若|猪猪)": [
                "我藤甲兵呢？救一下啊！",
                "龟龟，这也能开到我若子？"
            ],
            r"(炫狗|炫神)": [
                "我炫某人今天就要暴打棍子哥！",
                "卧槽，炫！"
            ],
            r"(吉吉国民)": [
                "全体起立！",
                "保护我方电棍！",
                "棍子哥倒了（哭腔）"
            ],
            r"(包C|包赢)": [
                "我Otto把话放这，这把必C！",
                "包C？包寄！"
            ],
            r"(世界第一中单)": [
                "没错，正是在下！",
                "世界第一中单？那必须是我棍子哥！"
            ]
        }
        
        # 游戏相关回复
        self.game_responses = {
            "亚索": ["遇到会玩的亚索了？棍子哥教你打亚索！"],
            "劫": ["这英雄我熟，当年用劫单杀Faker（不是）"],
            "佐伊": ["佐伊？佐伊就是个寄吧！"],
            "崩了": ["崩了？问题不大，看我棍子哥一手偷发育"],
            "15": ["15？15什么15，基地不爆炸就不投降！"],
            "翻盘": ["棍子哥的经典翻盘环节要来了！"]
        }

    async def on_group_message(self, event: MessageEvent):
        """处理群消息"""
        msg = event.message_chain.plain_text.lower()
        sender_id = event.sender.id
        
        # 概率触发（5%概率随机说一句）
        if random.random() < 0.05:
            await self.send_otto_quote(event)
            return
            
        # 被@时触发
        if event.message_chain.has(At) and self.bot_id in [at.target for at in event.message_chain.get(At)]:
            await self.handle_mention(event)
            return
            
        # 关键词匹配
        await self.keyword_match(event, msg)
        
        # 特定指令
        await self.handle_commands(event, msg)

    async def handle_mention(self, event: GroupMessageEvent):
        """被@时的回复"""
        responses = [
            "叫我干嘛？没看到我正在操作吗？",
            "棍子哥很忙，有话快说",
            "吉吉国民有什么事要汇报？",
            "我Otto今天心情好，不骂人"
        ]
        await event.reply(random.choice(responses))

    async def send_otto_quote(self, event: GroupMessageEvent):
        """随机发送Otto语录"""
        quote = random.choice(self.otto_quotes)
        await event.reply(quote)

    async def keyword_match(self, event: GroupMessageEvent, msg: str):
        """关键词匹配回复"""
        for pattern, responses in self.keyword_responses.items():
            if re.search(pattern, msg, re.IGNORECASE):
                if random.random() < 0.6:  # 60%概率回复
                    await event.reply(random.choice(responses))
                    break

    async def handle_commands(self, event: GroupMessageEvent, msg: str):
        """处理特定指令"""
        commands = {
            "!otto状态": self.otto_status,
            "!otto操作": self.otto_play,
            "!otto评级": self.rate_player,
            "!otto圣经": self.otto_bible,
            "!吉吉国民": self.jiji_nation
        }
        
        for cmd, func in commands.items():
            if msg.startswith(cmd):
                await func(event)
                break

    async def otto_status(self, event: GroupMessageEvent):
        """Otto当前状态"""
        statuses = [
            "正在直播，状态火热！",
            "破防中，勿扰",
            "对线ing，压力巨大",
            "包C中，这把必赢",
            "摆烂了，15点了"
        ]
        await event.reply(f"棍子哥状态：{random.choice(statuses)}")

    async def otto_play(self, event: GroupMessageEvent):
        """随机一个Otto操作"""
        plays = [
            "棍子哥招牌佐伊精准E闪！",
            "电棍亚索EQ闪接狂风绝息斩！",
            "Otto劫完美三花聚顶单杀！",
            "棍子哥这波肉身开团，队友呢队友呢？",
            "经典0-10战绩，但输出最高"
        ]
        await event.reply(random.choice(plays))

    async def rate_player(self, event: GroupMessageEvent):
        """Otto式评分"""
        ratings = [
            "白银水平，我上我也行",
            "黄金病友，建议多看看我直播",
            "铂金癌症，没救了",
            "钻石大神，但不如我棍子哥",
            "大师王者？有手就行！",
            "世界级操作！可以跟我Otto五五开"
        ]
        await event.reply(f"棍子哥评价：{random.choice(ratings)}")

    async def otto_bible(self, event: GroupMessageEvent):
        """Otto圣经"""
        bibles = [
            "你白银觉得是我的锅，那就是我的锅，为什么你知道吗？",
            "因为白银说的话，就像是一个癌症晚期患者说的话一样",
            "他都已经这样了，你为什么不顺从他呢？",
            "你总要给人最后一段时间一个好的回忆吧，最后的时光里",
            "因为白银这个段位很尴尬，再往上一点，黄金铂金，可能说，欸，有点实力，能操作一下",
            "白银往下，青铜，啊，人家是纯属玩游戏的，自己也知道自己没什么实力",
            "但白银，上不去下不来的这个段位，他觉得青铜的人不配跟他一起玩儿，对吧？",
            "青铜是最垃圾的，但是呢他想上去，他又上不去，所以这个分段是最尴尬的"
        ]
        bible = "\n".join(bibles)
        await event.reply(bible)

    async def jiji_nation(self, event: GroupMessageEvent):
        """吉吉国民"""
        members = event.group.member_count if hasattr(event.group, 'member_count') else "无数"
        response = f"全体吉吉国民起立！\n本群吉吉国民：{members}人\n口号：保护电棍！棍子哥勇敢飞，出事自己背！"
        await event.reply(response)

    def load(self):
        """插件加载时执行"""
        self.logger.info("Otto人格插件加载成功！吉吉国民集合！")
        
    def unload(self):
        """插件卸载时执行"""
        self.logger.info("Otto人格插件卸载，棍子哥倒了（哭腔）")
