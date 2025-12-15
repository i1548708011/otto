# main.py
import random
import re
from astrbot.api.star import Star

class OttoPersonality(Star):
    def __init__(self, context):
        super().__init__(
            name="otto",
            author="吉吉国民",
            version="1.0.0",
            desc="Otto人格插件（电棍行为向）"
        )
        self.context = context  # 保存 context 给需要的地方使用

        # Otto经典语录库
        self.otto_quotes = [
            "你号没了，我说的！",
            "我包C的，这把输了直接退网",
            "这波啊，这波是肉蛋葱鸡",
            "你白银觉得是我的锅，那就是我的锅",
            "这把分给你，15我点了",
            "我电棍今天就要把你们全杀了！",
            "你看这个兵它又香又脆",
            "不会真有人觉得我菜吧？",
            "厉害厉害，这就是王者800点的理解吗？",
            "哎呀，这波我的，我没想到你居然这么菜",
            "可以，这很秀，但没什么用",
            "这操作，我奶奶来都行",
            "好K！好K啊！",
            "寄！这把寄了！",
            "有挂！对面绝对有挂！",
            "这波不亏，甚至小赚",
            "稳住，我们能翻！",
            "问题不大，看我操作",
            "这把我C，你们躺好",
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

    async def on_message(self, event):
        msg = event.message_chain.plain_text
        if not msg:
            return
        msg = msg.lower()

        if not hasattr(event, "group") or event.group is None:
            return

        # 5%随机语录
        if random.random() < 0.05:
            await self.send_otto_quote(event)
            return

        # 被@触发
        for seg in event.message_chain:
            if getattr(seg, "type", None) == "at" and getattr(seg, "target", None) == self.bot_id:
                await self.handle_mention(event)
                return

        # 关键词触发
        for pattern, replies in self.keyword_responses.items():
            if re.search(pattern, msg):
                if random.random() < 0.6:
                    await event.reply(random.choice(replies))
                    return

        # 游戏相关触发
        for pattern, replies in self.game_responses.items():
            if pattern.lower() in msg:
                if random.random() < 0.6:
                    await event.reply(random.choice(replies))
                    return

        # 指令
        await self.handle_commands(event, msg)

    async def handle_mention(self, event):
        responses = [
            "叫我干嘛？没看到我正在操作吗？",
            "棍子哥很忙，有话快说",
            "吉吉国民有什么事要汇报？",
            "我Otto今天心情好，不骂人"
        ]
        await event.reply(random.choice(responses))

    async def send_otto_quote(self, event):
        await event.reply(random.choice(self.otto_quotes))

    async def handle_commands(self, event, msg):
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
                return

    async def otto_status(self, event):
        statuses = [
            "正在直播，状态火热！",
            "破防中，勿扰",
            "对线ing，压力巨大",
            "包C中，这把必赢",
            "摆烂了，15点了"
        ]
        await event.reply(f"棍子哥状态：{random.choice(statuses)}")

    async def otto_play(self, event):
        plays = [
            "棍子哥招牌佐伊精准E闪！",
            "电棍亚索EQ闪接狂风绝息斩！",
            "Otto劫完美三花聚顶单杀！",
            "棍子哥这波肉身开团，队友呢队友呢？",
            "经典0-10战绩，但输出最高"
        ]
        await event.reply(random.choice(plays))

    async def rate_player(self, event):
        ratings = [
            "白银水平，我上我也行",
            "黄金病友，建议多看看我直播",
            "铂金癌症，没救了",
            "钻石大神，但不如我棍子哥",
            "大师王者？有手就行！",
            "世界级操作！可以跟我Otto五五开"
        ]
        await event.reply(f"棍子哥评价：{random.choice(ratings)}")

    async def otto_bible(self, event):
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
        await event.reply("\n".join(bibles))

    async def jiji_nation(self, event):
        members = getattr(event.group, "member_count", "无数")
        response = f"全体吉吉国民起立！\n本群吉吉国民：{members}人\n口号：保护电棍！棍子哥勇敢飞，出事自己背！"
        await event.reply(response)
