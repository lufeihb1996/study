import os
import re

# Database of all items in the article
ARTICLES = [
    {
        "type": "img",
        "src": "https://pbs.twimg.com/media/G-efypCbQAEEi8a?format=jpg&name=large",
        "alt": "How to Fix Your Entire Life in 1 Day title card"
    },
    {
        "type": "lead",
        "en": "If you're anything like me, you think new years resolutions are stupid.",
        "zh": "如果你像我一样，你会认为新年誓言（New Year's Resolutions）挺愚蠢的。"
    },
    {
        "type": "p",
        "en": "Because most people go about changing their lives in the completely wrong way. They create these resolutions because everyone else does – we create a superficial meaning out of status games – but they don’t meet the requirements for true change, which goes a lot deeper than convincing yourself you’re going to be more disciplined or productive this year.",
        "zh": "因为大多数人改变生活的方式完全错了。他们之所以制定这些誓言，仅仅是因为其他人都在这么做——我们在地位游戏（status games）中创造出一种表面上的意义——但它们并不符合真正改变的要求。真正的改变要深刻得多，绝不仅仅是说服自己“今年我要变得更自律、更高效”。"
    },
    {
        "type": "p",
        "en": "If you're one of these people, I'm not here to talk down on you (I tend to be a bit harsh in my writing). I’ve quit 10x more goals than I’ve achieved. I think that should be the case for most people. But the fact that people try to change their lives and utterly fail almost every time holds true.",
        "zh": "如果你也是其中之一，我并不是要贬低你（我的写作风格往往有点犀利）。我放弃过的目标比我实现的要多出10倍。我认为对大多数人来说也理应如此。但事实依然是：人们试图改变自己的生活，却几乎每次都彻底失败。"
    },
    {
        "type": "p",
        "en": "However, as much as I think new years resolutions are stupid, it’s always wise to reflect on the life you hate so you can launch yourself toward something that much better, as we will discuss.",
        "zh": "然而，尽管我认为新年誓言很愚蠢，但反思自己讨厌的生活始终是明智的，这样你才能将自己推向更好的未来，正如我们接下来将要讨论的那样。"
    },
    {
        "type": "p",
        "en": "So whether you want to start the business, transform your body, or take the risk toward a more meaningful life without quitting after 2 weeks, I want to share 7 ideas you probably haven’t heard before on behavior change, psychology, and productivity so you can do just that in 2026.",
        "zh": "因此，无论你是想创业、改造身体，还是想踏上通往更有意义生活的冒险，且不会在两周后就放弃，我都想分享 7 个你可能从未听过的关于行为改变、心理学和生产力的观点，以便在 2026 年帮你实现这一目标。"
    },
    {
        "type": "p",
        "en": "This will be comprehensive.",
        "zh": "这将是一份详尽的指南。"
    },
    {
        "type": "p",
        "en": "This isn’t one of those letters that you read through and forget about.",
        "zh": "这绝不是那种你看完就忘的推文。"
    },
    {
        "type": "p",
        "en": "This is something you will want to bookmark, take notes on, and set aside time to think about.",
        "zh": "这是一篇你需要收藏、做笔记，并专门抽时间深度思考的内容。"
    },
    {
        "type": "p",
        "en": "The protocol at the end (to dig deep into your psyche and uncover what you truly want in life) will take about a full day to complete, with effects that last far longer than that.",
        "zh": "文章最后提供的重启协议（用以深入挖掘你的灵魂并发现你真正渴望的生活）将需要大约一整天的时间来完成，但它的效果将持续得比这长久得多。"
    },
    {
        "type": "p",
        "en": "Let’s begin.",
        "zh": "让我们开始吧。"
    },
    
    # SECTION I
    {
        "type": "h2",
        "en": "I – You aren’t where you want to be because you aren’t the person who would be there",
        "zh": "第一部分：你没有达到理想的状态，是因为你还不是那个能达到的人"
    },
    {
        "type": "p",
        "en": "When it comes to setting big goals, people tend to focus on one of the two requirements for success:",
        "zh": "当谈到设定宏伟目标时，人们往往只关注成功的两个要素之一："
    },
    {
        "type": "list",
        "items": [
            {
                "en": "Changing your actions to make progress toward the goal (least important, second order)",
                "zh": "改变你的行动以朝着目标前进（最不重要，属于二阶效应）"
            },
            {
                "en": "Changing who you are so that your behavior naturally follows (most important, first order)",
                "zh": "改变你的身份认知，让你的行为自然随之发生（最重要，属于一阶效应）"
            }
        ]
    },
    {
        "type": "p",
        "en": "Most people set a surface-level goal, hype themselves up to remain disciplined for the first few weeks, then go back to their old ways without much struggle, because they were trying to build a great life on a rotting foundation.",
        "zh": "大多数人只设定了一个表面的目标，在前几周靠打鸡血保持自律，然后没费多大劲就又回到了老样子，因为他们试图在腐烂的地基上建造美好的生活。"
    },
    {
        "type": "p",
        "en": "If this doesn’t make sense, let’s run through an example.",
        "zh": "如果这听起来有点抽象，我们来看个例子。"
    },
    {
        "type": "p",
        "en": "Think of somebody successful. It can be a bodybuilder with a great physique, a founder/CEO worth hundreds of millions, or a charismatic dude who can chat up a group without a shred of anxiety entering his mind.",
        "zh": "想想那些成功的人。他可以是一个拥有完美身材的健美运动员，一个身价数亿的创始人/CEO，或者一个能在一群人中谈笑风生、没有丝毫焦虑的社交达人。"
    },
    {
        "type": "p",
        "en": "Do you think the bodybuilder has to “grind” to eat healthy? Does the CEO have to discipline themselves to show up and lead the team? To you, it may seem like that on the surface, but the truth is that they can’t see themselves living any other way. The bodybuilder has to grind to eat <strong>unhealthily</strong>. The CEO has to force themself to lie in bed past their alarm clock, and they hate every second of it (there is nuance here, just entertain me for a second).",
        "zh": "你认为健美运动员必须“苦苦死撑”才能吃得健康吗？CEO必须逼迫自己自律才能去领导团队吗？在你看来，表面上似乎确实如此，但事实是，他们根本无法想象自己以其他方式生活。健美运动员想吃得<strong>不健康</strong>反而需要硬逼自己。CEO则需要强迫自己躺在床上不起床，而且他们讨厌赖床的每一秒（这里面有微妙的差别，但姑且听我往下说）。"
    },
    {
        "type": "p",
        "en": "To some people, my own lifestyle seems a bit extreme and disciplined. To me, it’s natural, and I don’t say that to contrast it with any other kind of lifestyle. I simply enjoy living this way. When my mom tells me that I should take a break, go out, and have some fun... I hold my tongue from telling her, “If I weren’t having fun, why would I be doing what I’m doing?”",
        "zh": "在一些人看来，我自己的生活方式似乎有些极端和过于自律。但对我而言，这很自然，我这么说并不是为了拿它与其他生活方式作对比。我只是单纯享受这样生活。当我的母亲告诉我应该休息一下、出去玩玩放松时……我忍住没有对她说：“如果我不觉得好玩，为什么还要做我现在做的事呢？”"
    },
    {
        "type": "p",
        "en": "This next sentence may sound simple, but it is baffling how many people don't get it.",
        "zh": "下面这句话听起来可能很简单，但令人困惑的是，竟然有那么多的人无法理解它："
    },
    {
        "type": "strong_p",
        "en": "If you want a specific outcome in life, you must have the lifestyle that creates that outcome long before you reach it.",
        "zh": "如果你想要在生活中获得特定的结果，那么在达成这个结果很久之前，你就必须先过上创造该结果的生活方式。"
    },
    {
        "type": "p",
        "en": "If someone says they want to lose 30 pounds, I often don’t believe them. Not because I don’t think they are capable, but because there are too many times when that same person says, “I can’t wait until I'm done losing weight so I can start to enjoy life again.” I hate to break it to you, but if you don’t adopt the lifestyle that led to you losing the weight, for life, and find a reason with a higher gravitational pull than the one tying you to your previous ways, then you will go straight back to where you started, and you can unhappily say that you wasted the resource you will never get back: time.",
        "zh": "如果有人说他们想减掉30磅，我通常是不信的。这并不是因为我认为他们做不到，而是因为有太多次，同样那个人会说：“我真等不及减完肥，这样我就能重新享受生活了。”我很不想打击你，但如果你不终生采纳那套帮你减肥的生活方式，并找到一个比绑在旧习惯上的拉力更强的“引力引擎”，你就会直接回到原点，然后悲哀地承认你浪费了永远无法找回的资源：时间。"
    },
    {
        "type": "p",
        "en": "When you truly change yourself, all of your habits that don’t move the needle toward your goal become disgusting, because you have a deep and profound awareness of what kind of life those actions compound into. You are okay with your current standards because you are not fully aware of what they are or what they lead to. We will discuss how to uncover this, but we need to build up to that.",
        "zh": "当当你真正改变自己时，所有那些不能对你的目标产生实际推动作用的习惯都会变得令人反胃。因为你对那些行为最终会复利累积成什么样的悲惨生活有着深刻而清晰的认知。你现在能接受你当前的妥协标准，只是因为你还没有完全意识到这些标准到底是什么，以及它们最终会把你带向何方。我们稍后会讨论如何发现这一点，但我们需要一步步来。"
    },
    {
        "type": "p",
        "en": "You say you want to change. You say you want to “become financially free” and “get healthy,” but your actions show otherwise for a reason. And it goes a lot deeper than you think.",
        "zh": "你口口声声说想要改变，想“财务自由”，想“获得健康”，但你的行动却反其道而行之，这是有原因的。它的根源比你想象的要深得多。"
    },

    # SECTION II
    {
        "type": "h2",
        "en": "II – You aren’t where you want to be because you don’t want to be there",
        "zh": "第二部分：你没有达到理想的状态，是因为你其实并不想达到那里"
    },
    {
        "type": "quote",
        "en": "Trust only movement. Life happens at the level of events, not of words. Trust movement.",
        "zh": "只相信行动。生命发生在事件的层面上，而非言语的层面上。相信行动。",
        "author": "Alfred Adler"
    },
    {
        "type": "p",
        "en": "If you want to change who you are, you must understand how the mind works so that you can start to reprogram it.",
        "zh": "如果你想改变你是谁，你必须理解大脑是如何运作的，以便开始对其进行重新编程。"
    },
    {
        "type": "p",
        "en": "The first step to understanding the mind is to understand that all behavior is goal-oriented. It's teleological. When you think about it, this is kinda obvious, but when we dig into it, most people don’t want to hear it.",
        "zh": "理解大脑的第一步是明白：所有的行为都是以目标为导向的，即目的论（teleological）。当你仔细想想，这挺显而易见的，但当我们深入探讨时，大多数人并不想面对这个真相。"
    },
    {
        "type": "p",
        "en": "You take a step forward because you want to reach a certain location.",
        "zh": "你向前迈一步，是因为你想去某个地方。"
    },
    {
        "type": "p",
        "en": "You scratch your nose because you want to make the itch go away.",
        "zh": "你挠挠鼻子，是因为你想消除发痒的感觉。"
    },
    {
        "type": "p",
        "en": "Those ones are clear, but most of the time, your goals are unconscious. You may not realize that when you sit on the couch in the middle of the day, you are trying to burn time before your next responsibility, as one simple example.",
        "zh": "这些都是显而易见的，但大多数时候，你的目标是无意识的。举个简单的例子，当你大中午瘫坐在沙发上时，你可能没有意识到，你实际上是在试图在下一项职责到来前“消磨时间”。"
    },
    {
        "type": "p",
        "en": "On an even more unconscious and complex level, you pursue goals that can harm you, but you justify your actions in a way that is socially acceptable and doesn’t make you seem like a loser.",
        "zh": "在更深层的无意识和复杂层面上，你甚至在追求一些会伤害你的目标，但你会用一种社会公认的借口来合理化自己的行为，好让自己看起来不像个失败者。"
    },
    {
        "type": "p",
        "en": "As an example, if you can’t stop procrastinating your work, you may justify it with the fact that you “lack discipline,” but in reality, you are attempting to achieve a goal like you always are. In this case, that goal could be to protect yourself from the judgment that comes from finishing and sharing your work.",
        "zh": "例如，如果你无法停止拖延工作，你可能会将其归咎于“缺乏自律”，但实际上你和往常一样，是在试图达成一个潜在目标。在这个例子中，这个目标可能是保护自己，免受完成并分享工作后所面临的他人评判。"
    },
    {
        "type": "p",
        "en": "If you say you want to quit your dead-end job, but stay in it without any real reason, you may start to think you don’t have enough courage, or that you were never really a “risk taker,” but the truth is that you are pursuing the goal of safety, predictability, and an excuse to not look like a failure to everyone else in your life who sees working a dead-end job as a sign of success.",
        "zh": "如果你口口声声说想辞掉这份没有前途的工作，却没有任何现实原因地一直熬在那里，你可能会觉得是自己不够勇敢，或者天生不是个“敢于冒险的人”。但真相是，你正在追求安全感、可预测性，以及一个不用在他人面前扮演失败者的借口（因为在那些把你拥有一份死工资视为成功标志的周围人眼里，你做这份工作刚刚好）。"
    },
    {
        "type": "p",
        "en": "The lesson here is that real change requires changing your goals.",
        "zh": "这里的启示是：真正的改变需要改变你的目标。"
    },
    {
        "type": "p",
        "en": "I don’t mean setting some surface-level goal because the act of doing that serves an unconscious goal that is actually harming you. That’s been ran through enough in the productivity space. I mean changing your point of view. Because that’s what a goal is. A goal is a projection into the future that acts as a lens of perception which allows you to notice information, ideas, and resources that aid in you achieving that goal.",
        "zh": "我并不是指随便设一个表面的目标，因为那反而会为你那个有害的无意识目标打掩护。这种做法在效率学界已经被探讨得够多了。我指的是改变你的视角。因为这就是目标的本质：目标是对未来的一种投射，它作为一块感知滤镜，决定了你能注意到哪些有助于你实现该目标的信息、想法和资源。"
    },
    {
        "type": "p",
        "en": "Now let’s dig a bit deeper, because if you don’t understand this, it only becomes more difficult to get out.",
        "zh": "现在让我们逆流而上，挖得更深一点，因为如果你不理解这一点，你就只会越陷越深，更难挣脱。"
    },

    # SECTION III
    {
        "type": "h2",
        "en": "III – You aren’t where you want to be because you’re afraid to be there",
        "zh": "第三部分：你没有达到理想的状态，是因为你害怕到达那里"
    },
    {
        "type": "quote",
        "en": "The important thing for you to remember is that it does not matter in the least how you got the idea or where it came from... if you are firmly convinced that idea is true, it has the same power over you as the hypnotist’s words have over the hypnotized subject.",
        "zh": "你需要记住的最重要的一点是，你如何获得这个想法或它来自哪里完全不重要……只要你深信不疑它是真的，它对你所拥有的掌控力，就与催眠师的指令对被催眠者的控制力毫无二致。",
        "author": "Maxwell Maltz"
    },
    {
        "type": "p",
        "en": "Here’s how you’ve become who you are today, and how you will become who you will be tomorrow. This is the anatomy of identity:",
        "zh": "以下是你如何成为今天的你，以及你将如何成为明天的你。这就是身份的剖析："
    },
    {
        "type": "list",
        "items": [
            {"en": "You want to achieve a goal", "zh": "你想要达成一个目标。"},
            {"en": "You perceive reality through the lens of that goal", "zh": "你通过该目标的感知滤镜来观察现实。"},
            {"en": "You only notice “important” information and ideas that allows you to achieve that goal (learning)", "zh": "你只注意到有助于实现该目标的关键信息和想法（学习阶段）。"},
            {"en": "You act toward that goal and receive feedback that you are progressing toward it", "zh": "你朝着这个目标行动，并获得你正在取得进展的反向反馈。"},
            {"en": "You repeat that behavior until it becomes automatic and unconscious (conditioning)", "zh": "你重复这一行为，直到它变得自动且无意识（条件反射阶段）。"},
            {"en": "That behavior becomes a part of who you think you are (”I am the type of person who...”)", "zh": "这个行为成为了你自我认同的一部分（“我就是那种……的人”）。"},
            {"en": "You defend your identity to maintain psychological consistency", "zh": "你拼命捍卫这个身份，以维持心理上的一致性。"},
            {"en": "Your identity shapes new goals, restarting the cycle, and if that identity is disadvantageous toward a good life, this gets bad very quick", "zh": "你的身份重塑了新的目标，循环再次开启。如果这个身份不利于过上美好的生活，情况很快就会急转直下。"}
        ]
    },
    {
        "type": "p",
        "en": "The unfortunate reality is that you must break the cycle between steps 6 and 7, but this process starts when you are a child.",
        "zh": "遗憾的事实是，你必须在第6步和第7步之间打破这个死循环。然而，这个过程早在你的童年时期就已经开始了。"
    },
    {
        "type": "p",
        "en": "You have the goal of survival.",
        "zh": "你最初的目标是生存。"
    },
    {
        "type": "p",
        "en": "You are dependent on your parents to teach you how to survive. You had to conform. And since the way most people teach is through reward and punishment, unless you adopt their beliefs and values, you will be punished. You don’t actually think for yourself until you see through this.",
        "zh": "你必须依靠父母教会你如何生存。你必须顺从。因为大多数人教育的方式都是通过奖励和惩罚，除非你采纳他们的信念和价值观，否则你就会受到惩罚。在你彻底看穿这一点之前，你从来没有真正为自己思考过。"
    },
    {
        "type": "p",
        "en": "But your parents have also gone through this process throughout their entire lives. That’s where it can get dangerous. Your parents, unless they broke the pattern themselves, were conditioned by the culturally accepted ideas of success from the Industrial age. They also carry the best and worst conditioning from their parents and their parents’ parents.",
        "zh": "但你的父母一生中同样也经历了这个过程。这就是危险的来源。你的父母，除非他们自己打破了这一模式，否则都受到了工业时代公认的成功观念的规训。他们身上同样背负着来自他们父母，乃至祖父母的最佳和最糟的思想钢印。"
    },
    {
        "type": "p",
        "en": "To take it a layer deeper, once you fulfill your physical survival needs (which is quite easy to do in today’s world, you’re practically born into safety), you start to survive on the conceptual or ideological level. You may not try to protect and reproduce your body, but you absolutely protect and reproduce your mind. It’s not difficult to see the war of ideas on the internet, and the participants are individual and group identities.",
        "zh": "往深处再说一步，一旦你满足了肉体上的生存需求（这在当今世界是相当容易实现的，你几乎是出生在安全环境里的），你便开始转向概念或意识形态层面的生存。你也许不再需要极力保护和繁衍肉体，但你绝对在极力保护和繁衍你的心智。在互联网上不难看到思想的战争，而交战的各方正是各种个人和群体的身份认同。"
    },
    {
        "type": "p",
        "en": "When your body feels threatened, you go into fight or flight.",
        "zh": "当你的肉体感到受到威胁时，你会进入战斗或逃跑模式。"
    },
    {
        "type": "p",
        "en": "When your identity feels threatened, the same thing happens.",
        "zh": "当你的身份认同受到威胁时，同样的事情也会发生。"
    },
    {
        "type": "p",
        "en": "If you are heavily identified with a political ideology, you will feel threatened when someone challenges your beliefs. You literally feel the stress. You feel, emotionally, like you were just slapped in the face. Since most people don’t analyze their emotions for truth, you tend to get stuck in echo chambers and double down on claims that harm yourself and others.",
        "zh": "如果你高度认同某种政治意识形态，当有人挑战你的信仰时，你会感到受到威胁。你确实能感受到那种压力。从情感上来说，你感觉就像被狠狠扇了一巴掌。由于大多数人并不会去剖析情绪背后的真实动机，人们往往会困在信息茧房里，并固执于那些对自己和他人都有害的言论。"
    },
    {
        "type": "p",
        "en": "If you were raised in a religious household, and did not think for yourself, you will fight and attack others who threaten your psychological safety within that little bubble.",
        "zh": "如果你在一个宗教家庭长大，没有独立思考过，你就会在那个小泡泡里拼命攻击那些威胁你心理安全感的人。"
    },
    {
        "type": "p",
        "en": "The same thing happens when you unconsciously see yourself as a lawyer, a gamer, or somebody else who would not take the actions to achieve a better life.",
        "zh": "同样地，当你无意识地将自己定义为一个律师、一个游戏玩家，或者其他任何不可能会为了获得更好的生活而付诸行动的人时，同样的抗拒也会发生。"
    },

    # SECTION IV
    {
        "type": "h2",
        "en": "IV – The life you want lies within a specific level of mind",
        "zh": "第四部分：你想要的生活，存在于心智的特定层级中"
    },
    {
        "type": "p",
        "en": "The mind evolves through predictable stages over time.",
        "zh": "随着时间的推移，心智会经历可以预测的发展阶段。"
    },
    {
        "type": "p",
        "en": "When you’re born, you’re like a little survival sponge that absorbs whatever beliefs you can (which are heavily dictated by your culture) so that you can feel safe and secure. And if you don’t be careful, your mind may crystalize and it may make it difficult to live a meaningful life.",
        "zh": "当你出生时，你像一块生存海绵，竭尽所能地吸收能接触到的信念（这些信念很大程度上是由你的文化决定的），以便让自己感到安全和踏实。如果你不够警惕，你的思想可能会就此固化，令你很难过上真正有意义的生活。"
    },
    {
        "type": "p",
        "en": "This has been documented enough in models like Maslow’s Hierarchy, Greuter’s stages of ego development, Spiral Dynamics, and Integral Theory, each building off of one another, but it’s also not difficult to observe in society.",
        "zh": "这一点在诸如马斯洛需求层次理论、格鲁特自我发展阶段（Greuter's stages of ego development）、螺旋动力学（Spiral Dynamics）和整合理论（Integral Theory）等模型中都已得到了充分的研究，它们层层推进。当然，在社会中观察到这些心智状态也并不难。"
    },
    {
        "type": "p",
        "en": "Here’s the 80/20 of the 9 stages of ego development as a refresher (because repetition helps reveal things you didn’t notice before, and there are new people reading these letters):",
        "zh": "以下是自我发展九个阶段的“二八法则”核心概述，让我们重温一下（因为重复阅读能帮你发现之前忽略的细节）："
    },
    {
        "type": "img",
        "src": "https://pbs.twimg.com/media/G-ebHTubsAEsAee?format=jpg&name=large",
        "alt": "9 Stages of Ego Development Chart"
    },
    {
        "type": "list",
        "items": [
            {"en": "<strong>Impulsive</strong> — No separation between impulse and action. Black and white thinking. I.e. A toddler hits when angry because the feeling and the behavior are the same thing.", "zh": "<strong>冲动期 (Impulsive)</strong> —— 冲动与行动之间毫无间隔。非黑即白的思维。例如：蹒跚学步的幼童一生气就会动手，因为情绪和行为在他们那里是同一个东西。"},
            {"en": "<strong>Self-Protective</strong> — The world is dangerous and you learn to look out for yourself. I.e. A kid learns to hide report cards, lie about chores, and figure out what adults want to hear.", "zh": "<strong>自我保护期 (Self-Protective)</strong> —— 觉得世界是危险的，你学会了处处为自己防备。例如：小孩子学会藏起成绩单、在做家务上撒谎，并琢磨大人们爱听什么。"},
            {"en": "<strong>Conformist</strong> — You are your group and its rules feel like reality itself. I.e. Someone who genuinely cannot fathom why anyone would vote differently than their family or group.", "zh": "<strong>顺从期 (Conformist)</strong> —— 你就是你所属的群体，群体的规则在你的世界里就等于现实本身。例如：一个人完全无法理解为什么有人会投出与家人或圈子不同的选票。"},
            {"en": "<strong>Self-Aware</strong> — You notice you have an inner life that doesn’t match the exterior. I.e. Sitting in church and realizing you’re not sure you believe what everyone around you seems to believe, but not knowing what to do with that feeling yet.", "zh": "<strong>自我反思期 (Self-Aware)</strong> —— 你开始注意到自己的内心世界与外在表现并不完全契合。例如：坐在教堂里，却突然意识到自己并不一定相信身边所有人看起来笃信的教条，但又不知道该如何处理这种别扭。"},
            {"en": "<strong>Conscientious</strong> — You build your own system of principles and hold yourself accountable to them. I.e. Leaving your family’s religion after careful study and adopting a personal philosophy you can defend, or building a career plan with clear milestones because you believe the right effort yields the right results.", "zh": "<strong>自律/公正期 (Conscientious)</strong> —— 你建立了自己的原则系统，并自我约束、自我负责。例如：在仔细研究后离开家庭的传统宗教，选择自己认同的哲学；或者制定清晰的职业发展路线图，因为你相信努力就会有回报。"},
            {"en": "<strong>Individualist</strong> — You see that your principles were shaped by context and start holding them more loosely. I.e. Realizing your political views have more to do with where you grew up than objective truth, or noticing that your ambitious career goals were really about earning your father’s approval.", "zh": "<strong>个人主义期 (Individualist)</strong> —— 你意识到你的原则只是特定环境的产物，并开始不再那么死板地固守它们。例如：意识到你的政治观点很大程度上取决于你的成长地，而非客观真理；或者察觉到你雄心勃勃的职业目标，其实只是在寻求父亲的认可。"},
            {"en": "<strong>Strategist</strong> — You work with systems while aware of your own involvement in them. I.e. Leading an organization while actively questioning your own blind spots, or engaging in politics knowing your perspective is partial and shaped by bias you can’t fully see.", "zh": "<strong>策略期 (Strategist)</strong> —— 你能在系统内工作，同时敏锐地意识到自己在其中的作用和局限。例如：领导一个组织，同时积极审视和质疑自己的盲区；参与公共事务，深知自己的视角可能是不全面的、被偏见影响的。"},
            {"en": "<strong>Construct-Aware</strong> — You see all frameworks, including your identity, as useful fictions. I.e. Holding your spiritual beliefs metaphorically not literally, knowing the map is not the territory, or watching yourself play the role of “founder” or “thought leader” with a kind of gentle amusement.", "zh": "<strong>建构自我期 (Construct-Aware)</strong> —— 你把所有的框架，甚至包括你自己的身份认同，都看作有用的虚构。例如：把你的精神信仰视为隐喻而非教条；明白“地图并不等同于疆域”；能够带着温和的幽默感，观察自己扮演着创始人或思想领袖的角色。"},
            {"en": "<strong>Unitive</strong> — Separation between self and life dissolves. I.e. Work, rest, and play feel like the same thing. There’s no one left who needs to become something, just presence responding to what arises.", "zh": "<strong>统一期 (Unitive)</strong> —— 自我与生活之间的分离彻底消失。例如：工作、休息和娱乐完全消融为一件事。不再有“谁”需要变成“什么样”，只有纯粹的临在，去自然应对生命中发生的每一件事。"}
        ]
    },
    {
        "type": "p",
        "en": "For most people reading this, I would assume you hover between 4 and 8, which is a huge gap. Those closer to 8 are reading this are doing so to either learn something or pass time in a non-destructive way. Those closer to 4 are really looking for a change. You feel like you are meant for more, but you can’t make sense of everything yet, because there’s obviously a lot at play.",
        "zh": "对于大多数读到这里的人，我猜你正徘徊在 4 到 8 阶段之间，这是一个巨大的鸿沟。那些更接近 8 的人，读到这里是为了学习知识，或以非建设性的方式打发时间；而那些更接近 4 的人则是真正渴望改变。你觉得你注定会更不凡，但又暂时无法厘清所有的线索，因为显然有太多的因素交织在一起。"
    },
    {
        "type": "p",
        "en": "The good thing is, it doesn’t really matter what stage you are in, because moving through any of them follows a pattern.",
        "zh": "好消息是，你目前处于哪个阶段并不重要，因为跨越其中任何一个阶段都遵循同样的规律。"
    },

    # SECTION V
    {
        "type": "h2",
        "en": "V – Intelligence is the ability to get what you want out of life",
        "zh": "第五部分：智能是你在生活中得偿所愿的能力"
    },
    {
        "type": "quote",
        "en": "The only real test of intelligence is if you get what you want out of life.",
        "zh": "检验智能的唯一真实标准，是你能否在生活中得偿所愿。",
        "author": "Naval Ravikant"
    },
    {
        "type": "p",
        "en": "There is a formula for success.",
        "zh": "成功是有公式的。"
    },
    {
        "type": "p",
        "en": "One ingredient is <strong>agency</strong>.",
        "zh": "第一个要素是<strong>主动性（Agency）</strong>。"
    },
    {
        "type": "p",
        "en": "One ingredient is <strong>opportunity</strong> (which many people like to mistake as “privilege” - because they lack the other ingredients).",
        "zh": "第二个要素是<strong>机会（Opportunity）</strong>（很多人喜欢将其误判为“特权”——因为他们缺乏其他要素）。"
    },
    {
        "type": "p",
        "en": "The last ingredient is <strong>intelligence</strong>.",
        "zh": "最后一个要素就是<strong>智能（Intelligence）</strong>。"
    },
    {
        "type": "p",
        "en": "If you have high agency but low opportunity, it doesn’t matter how likely you are to act toward a goal, because it isn’t a goal that will bear much fruit.",
        "zh": "如果你拥有极强的主动性但缺乏机会，无论你朝着目标行动的意愿有多强，这都不会带来多少丰硕的果实。"
    },
    {
        "type": "p",
        "en": "If you have opportunity and agency but low intelligence, then you will never be fully able to benefit from that opportunity.",
        "zh": "如果你拥有机会和主动性，却缺乏智能，那么你将永远无法完全从机会中受益。"
    },
    {
        "type": "p",
        "en": "First, we’ve talked about agency before here. In terms of opportunity, I can’t tell you to change your physical location, but if you don’t see the abundance of digital opportunity right in front of you, I don’t know what to tell you.",
        "zh": "首先，我们之前已经讨论过主动性了。至于机会，我不能教你改变你的现实地理位置，但如果你连眼前如此充沛的数字化机会都视而不见，我真不知道该对你说什么了。"
    },
    {
        "type": "p",
        "en": "With that said, I want to focus on what intelligence is in the context of these two other ingredients and this letter. For that, we look to cybernetics.",
        "zh": "话虽如此，我今天想把核心放在探讨本信所处语境下的“智能”上。为此，我们需要求助于控制论（cybernetics）。"
    },
    {
        "type": "p",
        "en": "Cybernetics comes from the greek word kybernetikos which means “to steer” or “good at steering.”",
        "zh": "控制论（Cybernetics）源于希腊文 kybernetikos，意为“舵手”或“擅长操舵”。"
    },
    {
        "type": "p",
        "en": "It’s also known as “the art of getting what you want.”",
        "zh": "它也被称为“获得所想之物的艺术”。"
    },
    {
        "type": "p",
        "en": "So, if Naval’s definition of intelligence is getting what you want out of life, understanding cybernetics helps you do that much faster.",
        "zh": "所以，如果纳瓦尔对智能的定义是“在生活中得偿所愿”，那么理解控制论能帮你在人生中极速前进。"
    },
    {
        "type": "p",
        "en": "Cybernetics illustrates the properties of intelligent systems:",
        "zh": "控制论阐明了智能系统的特征："
    },
    {
        "type": "list",
        "items": [
            {"en": "To have a goal.", "zh": "拥有目标。"},
            {"en": "Act toward that goal.", "zh": "朝着目标行动。"},
            {"en": "Sense where you are.", "zh": "感知自身所处的状态。"},
            {"en": "Compare it to the goal.", "zh": "将其与目标进行对比。"},
            {"en": "And act again based on that feedback.", "zh": "根据反馈再次调整行动。"}
        ]
    },
    {
        "type": "img",
        "src": "https://pbs.twimg.com/media/G-eb5tkbEAA8v0u?format=jpg&name=large",
        "alt": "Cybernetic loop of Act, Sense, Compare"
    },
    {
        "type": "p",
        "en": "You can judge intelligence based on the system’s ability to iterate and persist with trial and error.",
        "zh": "你可以通过一个系统迭代和在尝试与纠错中坚持的能力，来判断其智能程度。"
    },
    {
        "type": "p",
        "en": "A ship blown off course that corrects toward its destination. A thermostat sensing a change in heat and turning on. The pancreas excreting insulin after blood glucose spikes.",
        "zh": "比如一艘被狂风吹偏了航线的轮船重新修正回它的目的地；一个温度调节器感知到了温度变化并启动运行；胰腺在血糖飙升后自动分泌胰岛素。"
    },
    {
        "type": "p",
        "en": "What does this have to do with getting what you want out of life?",
        "zh": "这与你得偿所愿有什么关系？"
    },
    {
        "type": "p",
        "en": "Everything.",
        "zh": "关系极大，这就是全部。"
    },
    {
        "type": "p",
        "en": "Acting, sensing, comparing, and understanding the system from a meta-perspective is fundamental to high intelligence (with the definition we are using here).",
        "zh": "采取行动、感知现状、对比差距，并从“元视角”（Meta-Perspective）审视整个系统，是高智能的根本基石。"
    },
    {
        "type": "strong_p",
        "en": "The mark of low intelligence is the inability to learn from your mistakes.",
        "zh": "而低智能的标志则是无法从错误中吸取教训。"
    },
    {
        "type": "p",
        "en": "Low-intelligence people get stuck on problems rather than solving them. They hit a roadblock and quit. Like a writer who fails to build a readership and quits because they lack the ability to try new things, experiment, and figure out a process that works for them (to think that there isn’t an effective process you can create is verifiably false, no matter your limiting beliefs, hence being low intelligence.)",
        "zh": "低智能的人往往会困在问题中怨天尤人，而不是动手去解决它。他们一遇到阻碍就放弃。就像一个写作者无法积累起读者，于是直接封笔，因为他们缺乏尝试新事物、做实验并摸索出一套适合自己的机制的能力（认为不存在一条能让你通向成功的路径，这在逻辑上就已经被证伪了，无论你有着怎样的限制性信念，这种逃避本身正是低智能的体现）。"
    },
    {
        "type": "p",
        "en": "High intelligence is realizing any problem can be solved on a large enough timescale. The reality is that you can achieve any goal you set your mind to.",
        "zh": "高智能则是意识到：在足够长的时间尺度上，任何问题都是可以解决的。现实是，只要你下定决心，你可以实现任何设定的目标。"
    },
    {
        "type": "p",
        "en": "Intelligence is realizing that there is a series of choices you can make which lead to achieving the goal you want. You understand that ideas are hierarchical and that you can’t go from papyrus to Google docs in one fell swoop. Even if that goal is impossible right now, you simply don’t have the resources – which may be invented over the next few years – to achieve that thing.",
        "zh": "智能是意识到：存在着一系列特定的选择，它们复利之后能将你导向所期望的目标。你明白想法是有层级性的，你不可能一蹴而就直接从莎草纸跨越到谷歌文档。哪怕某个目标眼下无法达成，你也只是由于缺乏相应的资源——而这些资源可能会在未来的几年中被发明创造出来——来支撑这个结果。"
    },
    {
        "type": "p",
        "en": "When I talk about “goals,” and as I will continue repeating, I am not speaking from the typical lens of self-help, although that’s a helpful lens to adopt at times.",
        "zh": "当我谈论“目标”时，正如我会不断重复的那样，我并不是从传统自助书的浅显角度切入，尽管这种视角有时也有帮助。"
    },
    {
        "type": "p",
        "en": "I am speaking from the lens of teleology or the Greek kosmos – that everything serves a purpose. That everything is a part of a greater whole.",
        "zh": "我是从目的论或希腊词 kosmos 的本质来谈的——万物皆有其意图，万物都是更大整体的一部分。"
    },
    {
        "type": "p",
        "en": "Goals determine how you see the world.",
        "zh": "目标决定了你如何看待这个世界。"
    },
    {
        "type": "p",
        "en": "Goals determine what you consider “success” or “failure.”",
        "zh": "目标决定了你将什么定义为“成功”或“失败”。"
    },
    {
        "type": "p",
        "en": "You can try to “enjoy the journey,” but if you pursue the wrong goal, you will not enjoy it.",
        "zh": "你可以努力劝自己“享受过程”，但如果你追求了错误的目标，你永远不可能真正享受其中。"
    },
    {
        "type": "p",
        "en": "Your mind is the operating system for reality.",
        "zh": "你的心智是现实世界的操作系统。"
    },
    {
        "type": "p",
        "en": "That system is composed of goals.",
        "zh": "而这个操作系统，正是由目标构成的。"
    },
    {
        "type": "p",
        "en": "For most people, those goals are assigned to them. Programmed like lines of code in your psyche.",
        "zh": "对绝大多数人来说，他们的目标是直接被分配的。像一行行垃圾代码一样被预先写入了你的灵魂。"
    },
    {
        "type": "p",
        "en": "Go to school. Get the job. Get offended. Play victim. Retire at 65.",
        "zh": "上学、找工作、玻璃心、扮演受害者、65岁退休。"
    },
    {
        "type": "p",
        "en": "A known path that doesn’t work.",
        "zh": "一条已经被证明彻底破产的已知路径。"
    },
    {
        "type": "p",
        "en": "To become more intelligent, you must:",
        "zh": "为了变得更具智能，你必须："
    },
    {
        "type": "list",
        "items": [
            {"en": "Reject the known path", "zh": "拒绝既定的旧路线。"},
            {"en": "Dive into the unknown", "zh": "纵身跃入未知。"},
            {"en": "Set new, higher goals to expand your mind", "zh": "设定全新的、更高的目标来扩容你的大脑。"},
            {"en": "Embrace the chaos and allow for growth", "zh": "拥抱混乱，并为成长留出空间。"},
            {"en": "Study the generalized principles of nature", "zh": "学习自然界最普适的底层规律。"},
            {"en": "Become a deep generalist", "zh": "成为一名深度通才。"}
        ]
    },
    {
        "type": "p",
        "en": "I understand this may not be the traditional definition of intelligence, but that sequence of steps leads to an extraordinary level of connections in your brain, leading to what we would observe as an intelligent person. Pair that with agency and you've got a winner.",
        "zh": "我知道这可能不是对“智能”的传统定义，但这一系列步骤能够使你的大脑产生非比寻常的神经连接，最终塑造出世人眼中高度智慧的杰出个体。再加上强悍的执行力，你将无往而不胜。"
    },
    {
        "type": "p",
        "en": "That leads us into the next section perfectly.",
        "zh": "这完美地引出了下一部分。"
    },

    # SECTION VI
    {
        "type": "h2",
        "en": "VI – How to launch into a completely new life (in 1 day)",
        "zh": "第六部分：如何在一天内全面跃入全新的人生"
    },
    {
        "type": "quote",
        "en": "The best periods of my life always came after a period of getting absolutely fed up with the lack of progress I was making.",
        "zh": "我人生中最好的那几个黄金时期，无一例外地都紧随在我对自己止步不前的现状感到彻底恶心和愤怒之后。",
        "author": "Dan Koe"
    },
    {
        "type": "p",
        "en": "How do you dig into your mind?",
        "zh": "你如何深挖你的大脑？"
    },
    {
        "type": "p",
        "en": "How do you become aware of your conditioning?",
        "zh": "你如何意识到你所接受的各种潜移默化的约束？"
    },
    {
        "type": "p",
        "en": "How do you reach profound insights and truths that change the trajectory of your life?",
        "zh": "你如何获得足以改变生命轨迹的深刻洞见和真理？"
    },
    {
        "type": "p",
        "en": "Through the simple, but often painful act of questioning.",
        "zh": "答案就是通过简单、但往往痛苦的“自我拷问”。"
    },
    {
        "type": "p",
        "en": "Something that so few people do, and you can tell by how they speak or give their thoughts on a specific topic. Questioning is thinking, and very few people do it.",
        "zh": "极少有人愿意这样做，你可以从他们平时说话的方式或对特定话题的看法中一眼看出来。提问才是思考的开端，而极少有人真正思考。"
    },
    {
        "type": "p",
        "en": "I want to give you a comprehensive protocol that you can use every year to reset your life and launch into a season of intense progress. This protocol helps you ask the right questions.",
        "zh": "我想给你一套详尽的协议，你可以每年用它来重置人生，开启一段全速前进的爆发期。这套协议将指引你提出正确的问题。"
    },
    {
        "type": "p",
        "en": "These questions will cover the macro to the micro: where you want to be, what you need to do to get there, and what you can do immediately to start moving the needle toward that reality.",
        "zh": "这些问题将涵盖从宏观到微观的每个维度：你想去向何方、需要做些什么才能到达那里，以及为了立刻推动齿轮运转，你现在能马上做些什么。"
    },
    {
        "type": "p",
        "en": "This will require one full day to complete, so I recommend you follow along with the exact protocol. You will need a pen, paper, and an open mind.",
        "zh": "这需要花费你整整一天的时间去完成，所以我建议你严格遵循以下流程。你需要准备好纸和笔，以及一个开放包容的心态。"
    },
    {
        "type": "p",
        "en": "When I observe patterns in people who successfully flip their identity, it happens fast after a build up of tension. Specifically, I’ve noticed 3 phases that people tend to go through.",
        "zh": "当我观察那些成功重塑身份认同的人的共同规律时，我发现这种转变在张力积压到顶点后发生得极快。我注意到人们往往会经历 3 个阶段："
    },
    {
        "type": "list",
        "items": [
            {"en": "<strong>Dissonance</strong> – They feel like they don’t belong in their current life, and become sufficiently fed up with their lack of progress.", "zh": "<strong>认知失调 (Dissonance)</strong> —— 觉得自己不属于当下的生活，对自己毫无长进的现状感到彻底厌恶和无法忍受。"},
            {"en": "<strong>Uncertainty</strong> – They don’t know what comes next, so they either experiment or get lost and feel worse.", "zh": "<strong>迷茫迷失 (Uncertainty)</strong> —— 不知道下一步该做什么，要么四处尝试，要么迷失方向并感觉更糟。"},
            {"en": "<strong>Discovery</strong> – They discover what they want to pursue and make 6 years of progress in 6 months.", "zh": "<strong>恍然觉醒 (Discovery)</strong> —— 发现了自己真正想追求的道路，并在短短 6 个月内取得以前需要 6 年才能积累出的突破。"}
        ]
    },
    {
        "type": "p",
        "en": "So, our goal with this protocol is to help you reach the point of dissonance, navigate through uncertainty, and discover what it truly is that you want to achieve, so much so that the clarity is overwhelming and distractions no longer hold their weight.",
        "zh": "因此，我们这套协议的核心目标，就是促使你达到那层不可忍受的“认知失调”，穿越迷茫，并明确找出你真正渴望达成的伟大使命，直到那股清晰感充盈到排山倒海，一切琐碎干扰再也无法动摇你分毫。"
    },
    {
        "type": "p",
        "en": "This protocol is structured so that it can be completed in one day. In the morning, you do a psychological excavation to uncover your own hidden motives. During the day, you prompt yourself with interrupts to keep you out of autopilot and contemplate your life. At night, you synthesize the insights into a direction you will start to move in tomorrow.",
        "zh": "该协议的日程如下：**上午**，做一次灵魂深处的挖掘，揭示那些你隐藏的潜意识动机。**白天空闲时间**，通过周期性的“中断提醒”强行让自己脱离自动驾驶状态，去审视自己的生活。**晚上**，将这一天的顿悟和洞见融会贯通，总结成你明天就要踏上去的新方向。"
    },
    {
        "type": "p",
        "en": "I cannot guarantee that this will work for everyone, because I cannot guarantee that everyone reading this is in the right chapter of their own story that would make these points impactful. You can’t place the climax at the start of the book and expect it to be interesting.",
        "zh": "我无法向所有人保证这能立竿见影。因为我不能保证正在阅读本文的每个人是否都刚好处于自己故事里那个能发挥影响的“正确章节”。你不可能把整本书的高潮部分强塞进开篇，然后还指望它读起来合情合理。"
    },
    {
        "type": "h3",
        "en": "Part 1) Morning – Psychological Excavation – Vision & Anti-Vision",
        "zh": "第一部分）上午 —— 心理挖掘 —— 愿景与反向愿景"
    },
    {
        "type": "p",
        "en": "First we must create a new frame, or lens of perception, for your mind to operate from. This is like creating a new shell, leaving your old one, and slowly growing into it over time. It won’t feel like it fits at first. That’s a good thing. Set aside 15-30 minutes to think about and answer these questions. Do not attempt to outsource this contemplation to AI. I want you to break past the limiter that is on your mind. If you can’t answer these immediately, come back to them later.",
        "zh": "首先，我们必须为你的大脑建立一个新的感知框架或滤镜。这就像是在身体外面造了一个新外壳，你脱下旧壳，随着时间的推移慢慢成长并融入这个新壳。起初它一定会让你觉得别扭和不适。这才是对的。留出15到30分钟（大概也就是看一段YouTube视频的长度……你一定能做得到）去深度思考并回答以下问题。千万不要试图把这项思考工作“外包”给AI。我需要你冲破扣在你自己思维上的紧箍咒。如果不能瞬间写出答案，没关系，先放放，稍后继续。"
    },
    {
        "type": "list",
        "items": [
            {"en": "What is the dull and persistent dissatisfaction you’ve learned to live with? Not the deep suffering but what you’ve learned to tolerate. (If you don’t hate it, you will tolerate it)", "zh": "什么是你已经习惯与其共处的、沉闷且持久的不满？不是那种极端的剧痛，而是你已经学会麻木忍受的温水煮青蛙。（如果你不恨它，你就会无限期容忍它）"},
            {"en": "What do you complain about repeatedly but never actually change? Write down the three complaints you’ve voiced most often in the past year.", "zh": "你反复抱怨却从未真正付诸改变的事情是什么？写下你在过去一年里最常挂在舌尖的三句抱怨。"},
            {"en": "For each complaint: What would someone who watched your behavior (not your words) conclude that you actually want?", "zh": "针对每句抱怨：如果有人通过观察你的实际行为（而不是你的口头言语）来做出评判，他们会得出你实际上想要什么的结论？"},
            {"en": "What truth about your current life would be unbearable to admit to someone you deeply respect?", "zh": "关于你当下的生活，向一个你深切尊敬的人亲口承认哪条真相会让你觉得最无法忍受？"}
        ]
    },
    {
        "type": "p",
        "en": "Those questions are meant to make you aware of the pain in your current life. Now, we need to turn those into what I call an “anti-vision,” which is a brutal awareness of the life you do not want to live. That way, you can use that negative energy to aim your efforts in a positive direction and act from a place of intrinsic motivation.",
        "zh": "这些问题的核心是让你清醒感知当下的痛苦。接着，我们要把它们塑造成我所谓的“反向愿景（Anti-Vision）”——对你绝对不想过的那种生活的残酷、真实的描绘。如此一来，你就能借用这股强大的负能量反向把精力聚焦在正确的道路上，爆发出发自内心的原始动力。"
    },
    {
        "type": "list",
        "items": [
            {"en": "If absolutely nothing changes for the next five years, describe an average Tuesday. Where do you wake up? What does your body feel like? What’s the first thing you think about? Who’s around you? What do you do between 9am and 6pm? How do you feel at 10pm?", "zh": "如果未来的五年内一切都没有改变，试着描绘出其中极其普通的一个星期二。你在哪里醒来？你的身体有什么感受？你脑子里浮现的第一个念头是什么？你周围都是谁？你在上午9点到下午6点之间在做什么？你在晚上10点感觉如何？"},
            {"en": "Now do it but for ten years. What have you missed? What opportunities closed? Who gave up on you? What do people say about you when you’re not in the room?", "zh": "现在，试想十年。你错过了什么？哪些机会之门永远对你关闭了？谁最终对你感到绝望而离去？当你在房间外时，别人私下是怎么评价你的？"},
            {"en": "You’re at the end of your life. You lived the safe version. You never broke the pattern. What was the cost? What did you never let yourself feel, try, or become?", "zh": "你已经走到了生命的尽头。你过完了平稳安全的一生，从未打破宿命。这付出了什么代价？你从未让自己体会过、尝试过或成为过什么？"},
            {"en": "Who in your life is already living the future you just described? Someone five, ten, twenty years ahead on the same trajectory? What do you feel when you think about becoming them?", "zh": "在你认识的人中，有谁正在过着你刚刚描述的这种未来？在同样轨迹上前行五年、十年或二十年的某个人？想到自己会成为他们时，你内心深处是何感受？"},
            {"en": "What identity would you have to give up to actually change? (”I am the type of person who...”) What would it cost you socially to no longer be that person?", "zh": "为了真正开始改变，你必须放弃什么样的旧身份认同（“我就是那种……的人”）？不再充当那个人，会在社交层面上让你付出什么代价？"},
            {"en": "What is the most embarrassing reason you haven’t changed? The one that makes you sound weak, scared, or lazy rather than reasonable?", "zh": "你至今未能改变的、最令人羞耻难堪的原因是什么？那个让你听起来懦弱、害怕或懒惰，而不是所谓合理的真正借口。"},
            {"en": "If your current behavior is a form of self-protection, what exactly are you protecting? And what is that protection costing you?", "zh": "如果你现在的懈怠是在进行某种自我防卫，你到底在防卫什么？而这份防卫又正在剥夺你的什么未来？"}
        ]
    },
    {
        "type": "p",
        "en": "If you answered those truthfully, and if you are in the right chapter of your life, you will feel a deep sense of dis-ease and possibly disgust for how you are currently living. Now, we need to orient that energy in a positive direction. We need to create a minimum viable vision, because your vision is like a product. It starts out unclear, but with time and experience, it grows stronger and more potent.",
        "zh": "如果你真诚地回答了这些，且正好处于故事的爆发章节，你一定会感到如坐针毡，甚至对自己当下的处境深感嫌恶。接下来，我们要将这股能量引导向正面的出口。我们要起草一个“最小可行性愿景（MVP Vision）”，因为愿景就像一件产品，刚开始可能模糊不清，但随着时间和实践的积累，它会变得愈发强大而具体。"
    },
    {
        "type": "list",
        "items": [
            {"en": "Forget practicality for a minute. If you could snap your fingers and be living a different life in three years, not what’s realistic, what you actually want? What does an average Tuesday look like? Same level of detail as the anti-vision Tuesday.", "zh": "先把实际与否抛在一边。如果你现在可以打个响指，并在三年后过上截然不同的生活。不要退而求其次地追求妥协，你到底真正想要什么？描述一下那个普通的星期二，使用与刚才相同的细节描述。"},
            {"en": "What would have to be believe about yourself for that life to feel natural rather than forced? Write the identity statement: “I am the type of person who...”", "zh": "为了让那种生活成为理所当然，而不是硬着头皮演出来的，你需要对自己确立什么样的新信念？写下这个身份声明：“我就是那种……的人。”"},
            {"en": "What is one thing you would do this week if you were already that person?", "zh": "如果你已经是这样的人了，你在本周会做出的一件具体动作是什么？"}
        ]
    },
    {
        "type": "p",
        "en": "Answer all of those first thing in the morning tomorrow.",
        "zh": "明天早上第一件事就是回答这所有问题。"
    },
    {
        "type": "h3",
        "en": "Part 2) Throughout The Day – Interrupting Autopilot – Breaking Unconscious Patterns",
        "zh": "第二部分）白天的间歇 —— 中断自动驾驶模式 —— 强力打破潜意识惯性"
    },
    {
        "type": "p",
        "en": "These journaling exercises are cute, but we want real change. Frankly, that’s not going to happen if you don’t break the current unconscious patterns that are keeping you the same. Throughout the day, I want you to contemplate on everything you journaled in part one. Beyond that, I don’t want you to forget to contemplate. Please take this seriously. You aren’t going to change by doing the same thing for the rest of your life. You need to consciously force a pattern break. Take the time right now to create reminders or calendar events in your phone. Include the question in the reminder or event so that you can immediately start thinking about it. The more random and non-conflicting with your schedule there are, the better.",
        "zh": "做些纸面手账确实很优雅，但我们需要动真格的改变。直白地说，如果你不打破那些让你停滞不前的旧有潜意识行为模式，改变就绝无可能。在这一天里，我想让你反复玩味和推敲你在第一部分中所写下的所有反思。不仅如此，请绝对不要忘记思考。请务必认真对待。你重复做着同样的事，生活就不可能改变。你需要有意识地进行模式阻断。现在就花时间在你的手机上设置几个定时提醒或日程事件。在提醒里塞入以下问题，强迫大脑去检索："
    },
    {
        "type": "list",
        "items": [
            {"en": "<strong>11:00am:</strong> What am I avoiding right now by doing what I’m doing?", "zh": "<strong>上午11:00：</strong> 我现在做这件事，实际上在刻意逃避什么？"},
            {"en": "<strong>1:30pm:</strong> If someone filmed the last two hours, what would they conclude I want from my life?", "zh": "<strong>下午1:30：</strong> 如果有人把我过去两小时的行为录下来，他们会觉得我这辈子想要什么？"},
            {"en": "<strong>3:15pm:</strong> Am I moving toward the life I hate or the life I want?", "zh": "<strong>下午3:15：</strong> 我目前是一步步走向我讨厌的生活，还是我向往的生活？"},
            {"en": "<strong>5:00pm:</strong> What’s the most important thing I’m pretending isn’t important?", "zh": "<strong>下午5:00：</strong> 我正在假装什么事情不重要，而它实际上最重要？"},
            {"en": "<strong>7:30pm:</strong> What did I do today out of identity protection rather than genuine desire? (Hint: it’s most things you do)", "zh": "<strong>晚上7:30：</strong> 我今天做的哪些事情是为了捍卫旧身份，而不是出于真实热爱？（提示：大多数行为皆是如此）"},
            {"en": "<strong>9:00pm:</strong> When did I feel most alive today? When did I feel most dead?", "zh": "<strong>晚上9:00：</strong> 今天哪一刻让我感到最生机勃勃？哪一刻让我感到行尸走肉？"}
        ]
    },
    {
        "type": "p",
        "en": "To add a bit more fuel to the fire, schedule these questions during times where you are either commuting, walking, or lying around.",
        "zh": "此外，在通勤、散步或躺在床上的碎片时间里，给自己弹这几个终极追问："
    },
    {
        "type": "list",
        "items": [
            {"en": "What would change if I stopped needing people to see me as [the identity you wrote in question 5 of anti-vision]?", "zh": "如果我不再需要别人把我视作[旧身份]时，我的选择会发生什么变化？"},
            {"en": "Where in my life am I trading aliveness for safety?", "zh": "我在人生的哪个部分，为了平庸的安全感出卖了自己的生命活力？"},
            {"en": "What’s the smallest version of the person I want to become that I could be tomorrow?", "zh": "我明天可以扮演的、与我期望成为的人最贴近的最小化版本是什么？"}
        ]
    },
    {
        "type": "h3",
        "en": "Part 3) Evening – Synthesizing Insight – Entering A Season Of Progress",
        "zh": "第三部分）晚上 —— 提炼整合洞见 —— 进入你的爆发前进季"
    },
    {
        "type": "p",
        "en": "If you followed that process, I would be surprised if you didn’t have at least one profound insight that could alter the course of your life. Now, we need to make those known, integrate them into who we are, and act on them to begin solidifying our journey to a new level of mind.",
        "zh": "如果你认真走完了这套流程，我敢保证你至少会产生一个足以改写人生的惊人洞见。现在，我们需要把这些模糊的直觉用文字确定下来，将其内化为我们的一部分，并付诸行动，从而稳固我们的意识跃迁。"
    },
    {
        "type": "list",
        "items": [
            {"en": "After today, what feels most true about why you’ve been stuck?", "zh": "经历完这一天，关于自己此前被卡住的原因，你觉得最真实的关键是什么？"},
            {"en": "What is the actual enemy? Name it clearly. Not circumstances. Not other people. The internal pattern or belief that has been running the show.", "zh": "真正的敌人到底是谁？明确给它命名。不是环境，不是他人。而是那个一直在你心智幕后主导一切的内部模式或固有信念。"},
            {"en": "Write a single sentence that captures what you refuse to let your life become. This is your anti-vision compressed. It should make you feel something when you read it.", "zh": "写下一句简短的话，概括你绝不能忍受自己的生活堕落成什么样。这是你的“压缩版反向愿景”，当你大声读出来时，它必须能挑起你的情绪波澜。"},
            {"en": "Write a single sentence that captures what you’re building toward, knowing it will evolve. This is your vision MVP.", "zh": "写下一句简短的话，概括你正在为之拼搏的理想未来，允许它以后随阅历而进化。这是你的“MVP愿景”。"}
        ]
    },
    {
        "type": "p",
        "en": "Lastly, we need to create goals. Again, these aren’t goals that you set for the sake of achievement, because goals are just projections. They are unreliable and make you feel bound to something that will inevitably change. Instead, think of goals as a point of view. A lens that you can exchange to enter the right state of mind to perform the action that will lead away from the life you don’t want. Do not worry about some kind of finish line, because as we will find, it doesn’t exist. Enjoyment is found in progress.",
        "zh": "最后，我们要设立目标。记住，这些目标并非是为了去炫耀成就而设的，目标只是一种视角的投射。传统的成就目标不可靠，并且容易让你画地为牢。反之，要把目标视为一块可以自由替换的镜片，当你换上它，你就能瞬间调整状态，去从事那些能帮你远离讨厌生活的行动。别去纠结什么“终点线”，因为世上根本不存在什么终点。乐趣始终隐藏在“不断取得进展”的这门体验中。"
    },
    {
        "type": "list",
        "items": [
            {"en": "<strong>One-year lens:</strong> What would have to be true in one year for you to know you’ve broken the old pattern? One concrete thing.", "zh": "<strong>一年期镜片：</strong> 一年内必须发生哪一件具体的事，才能确凿证明你彻底打破了旧有的宿命模式？"},
            {"en": "<strong>One-month lens:</strong> What would have to be true in one month for the one-year lens to remain possible?", "zh": "<strong>单月期镜片：</strong> 为了让上述一年期目标成为可能，本月必须达成什么？"},
            {"en": "<strong>Daily lens:</strong> What are 2-3 actions you can timeblock tomorrow that the person you’re becoming would simply do?", "zh": "<strong>日规镜片：</strong> 明天你要强行划拨出时间去完成哪 2-3 件新身份下的人理所当然会去做的事？"}
        ]
    },
    {
        "type": "p",
        "en": "That was a lot. Hopefully it was helpful. But we have one last piece to lock it all in. Stick with me.",
        "zh": "这确实很多，但愿它对你有所帮助。不过我们还有最后的一块拼图来锁定一切。跟紧我。"
    },

    # SECTION VII
    {
        "type": "h2",
        "en": "VII – Turn Your Life Into A Video Game",
        "zh": "第七部分：将你的人生变成一场通关游戏"
    },
    {
        "type": "quote",
        "en": "The optimal state of inner experience is one in which there is order in consciousness. This happens when psychic energy—or attention—is invested in realistic goals, and when skills match the opportunities for action. The pursuit of a goal brings order in awareness because a person must concentrate attention on the task at hand and momentarily forget everything else.",
        "zh": "内心体验处于最佳状态时，意识中是有序的。这发生于我们将精神能量（即注意力）倾注于切实可行的目标，并且我们的技能正好匹配行动机遇的时候。追求目标能带给意识以秩序，因为一个人必须将所有注意力集中在手头的任务上，并暂时忘却其他一切事物。",
        "author": "Mihaly Csikszentmihalyi"
    },
    {
        "type": "p",
        "en": "You now have all of the components that lead to a good life. Now, it may be helpful to organize all of your insights into one coherent plan. Pull out a new page and write down these 6 components:",
        "zh": "此时，你已经掌握了通往美好人生的所有拼图。现在，把你的所有想法整理成一份连贯一致的规划图会极其有益。拉过一张新纸，写下这 6 大模块："
    },
    {
        "type": "list",
        "items": [
            {"en": "<strong>Anti-vision</strong> – What is the bane of my existence, or the life I never want to experience again?", "zh": "<strong>反向愿景 (Anti-Vision)</strong> —— 让我深恶痛绝、绝对不想再重温一遍的糟糕生活是什么？"},
            {"en": "<strong>Vision</strong> – What is the ideal life that I think I want and can improve as I work toward it?", "zh": "<strong>理想愿景 (Vision)</strong> —— 我当前最向往的、并能在实践中不断优化微调的理想人生是什么？"},
            {"en": "<strong>1 year goal</strong> – What will my life look like in 1 year time, and is that closer to the life I want?", "zh": "<strong>一年期目标 (1 Year Goal)</strong> —— 一年后我的生活将会是什么样子？它是否更接近理想的彼岸？"},
            {"en": "<strong>1 month project</strong> – What do I need to learn? What skills do I need to acquire? What can I build that will move me closer to the one year goal?", "zh": "<strong>单月期项目 (1 Month Project)</strong> —— 为了拉近与一年目标的距离，我需要学习什么？获得哪些技能？搭建什么成果？"},
            {"en": "<strong>Daily levers</strong> – What are the priority, needle-moving tasks that bring my project closer to completion?", "zh": "<strong>每日杠杆 (Daily Levers)</strong> —— 最能产生撬动效应、推动项目完成的前置关键日常任务是什么？"},
            {"en": "<strong>Constraints</strong> – What am I not willing to sacrifice to achieve my vision from the ground up?", "zh": "<strong>边界约束 (Constraints)</strong> —— 在我白手起家实现愿景的过程中，有哪些底线是我绝不妥协和牺牲的？"}
        ]
    },
    {
        "type": "p",
        "en": "Why is this so powerful? Because these components literally create your own little world. If you are meant to pursue this hierarchy of goals at this stage of your life, you will have no other option but to become obsessed. You will feel the pull to something greater. You will not see anything else as an option.",
        "zh": "为什么这极具威力？因为这些元素在你的心智里重新组装成了一个只属于你自己的微型宇宙。如果你在当下的生命阶段恰好契合这一层级结构，你除了对其产生“执念”外别无他选。你会被一股前所未有的宏大引力牵引，此外没有任何事能动摇你的决定。"
    },
    {
        "type": "p",
        "en": "You turn your life into a video game. Because games are the poster child for obsession, enjoyment, and flow states. They have all the components that lead to focus and clarity, so if we reverse engineer what those components are, we can live in a state of deeper enjoyment, less distractions, and more success.",
        "zh": "你将人生玩成了一款游戏。因为游戏是承载专注、乐趣和心流体验的最佳容器。游戏自带所有能诱发专注和清晰感的必备要素，如果我们能够逆向还原这些拼图，我们就能在现实中享受到更极致的沉浸感、更少的干扰和更大的成功率。"
    },
    {
        "type": "list",
        "items": [
            {"en": "Your vision is how you <strong>win</strong>. At least until the game evolves.", "zh": "你的理想愿景，就是你的<strong>终局胜利 (How you win)</strong>。至少在游戏进化之前。"},
            {"en": "Your anti-vision is what’s at <strong>stake</strong>. What happens if you lose or give up.", "zh": "你的反向愿景，就是你的<strong>命运赌注 (What’s at stake)</strong>。如果你输掉或放弃，会发生什么。"},
            {"en": "Your 1 year goal is the <strong>mission</strong>. This is your sole priority in life.", "zh": "你的年度目标，就是你的<strong>主线战役 (The mission)</strong>。这是你生活中唯一的首要任务。"},
            {"en": "Your 1 month project is the <strong>boss fight</strong>. How you gain XP and acquire loot.", "zh": "你的单月项目，就是你的<strong>Boss遭遇战 (The boss fight)</strong>。你如何获得经验值（XP）并赢取战利品。"},
            {"en": "Your daily levers are the <strong>quests</strong>. The daily process that unlocks new opportunities.", "zh": "你的每日杠杆，就是你的<strong>日常任务 (The quests)</strong>。每天解锁新机遇的日常进程。"},
            {"en": "Your constraints are the <strong>rules</strong>. The limitations that encourage creativity.", "zh": "你的边界约束，就是你的<strong>游戏规则 (The rules)</strong>。能够激发创造力的限制。"}
        ]
    },
    {
        "type": "p",
        "en": "All of these act as a concentric set of circles, like a forcefield, that guard your mind from distractions and shiny objects. The more you play the game, the stronger this force becomes, and soon enough it becomes who you are, and you wouldn’t have it any other way.",
        "zh": "这一整套系统就像是一组以你为中心的同心圆力场，阻断并保护你的心智免受喧嚣杂音和外界虚浮名利的干扰。你玩这个游戏的时间越久，这股力场就越坚固，直到最后它彻底化为你灵魂的一部分，你也根本不想再以其他任何方式生活。"
    },
    {
        "type": "p",
        "en": "– Dan",
        "zh": "—— 丹"
    }
]

def render_english(item):
    if item["type"] == "img":
        return f'<img src="{item["src"]}" class="article-img" alt="{item["alt"]}">'
    elif item["type"] == "lead":
        return f'<p class="lead-en">{item["en"]}</p>'
    elif item["type"] == "h2":
        return f'<h2 class="subsection-title serif-heading">{item["en"]}</h2>'
    elif item["type"] == "h3":
        return f'<h3 class="subsection-title">{item["en"]}</h3>'
    elif item["type"] == "p":
        return f'<p>{item["en"]}</p>'
    elif item["type"] == "strong_p":
        return f'<p><strong>{item["en"]}</strong></p>'
    elif item["type"] == "quote":
        return f'<div class="inner-quote"><p>"{item["en"]}"</p><span>— {item["author"]}</span></div>'
    elif item["type"] == "list":
        lis = "".join(f'<li>{li["en"]}</li>' for li in item["items"])
        return f'<ul>{lis}</ul>'
    return ""

def render_chinese(item):
    if item["type"] == "img":
        # Keep same image in Chinese
        return f'<img src="{item["src"]}" class="article-img" alt="{item["alt"]}">'
    elif item["type"] == "lead":
        return f'<p class="lead-zh">{item["zh"]}</p>'
    elif item["type"] == "h2":
        return f'<h2 class="subsection-title">{item["zh"]}</h2>'
    elif item["type"] == "h3":
        return f'<h3 class="subsection-title">{item["zh"]}</h3>'
    elif item["type"] == "p" or item["type"] == "strong_p":
        # Check if contains bold tag from raw data
        text = item["zh"]
        if item["type"] == "strong_p":
            text = f'<strong>{text}</strong>'
        return f'<p>{text}</p>'
    elif item["type"] == "quote":
        # Translate Alfred Adler or Mihaly Csikszentmihalyi name to Chinese if needed or keep it
        author = item["author"]
        if author == "Alfred Adler":
            author = "阿尔弗雷德·阿德勒"
        elif author == "Maxwell Maltz":
            author = "麦克斯威尔·马尔茨"
        elif author == "Naval Ravikant":
            author = "纳瓦尔·拉维康特"
        elif author == "Mihaly Csikszentmihalyi":
            author = "米哈里·契克森米哈赖（心流之父）"
        elif author == "Dan Koe":
            author = "丹·柯"
        return f'<div class="inner-quote"><p>“{item["zh"]}”</p><span>— {author}</span></div>'
    elif item["type"] == "list":
        lis = "".join(f'<li>{li["zh"]}</li>' for li in item["items"])
        return f'<ul>{lis}</ul>'
    return ""

def render_bilingual(item):
    if item["type"] == "img":
        return f'<div class="bilingual-para"><img src="{item["src"]}" class="article-img" alt="{item["alt"]}"></div>'
    elif item["type"] == "lead":
        return f'<div class="bilingual-para"><p class="b-en">{item["en"]}</p><p class="b-zh">{item["zh"]}</p></div>'
    elif item["type"] == "h2":
        return f'<div class="bilingual-para"><h2 class="subsection-title serif-heading">{item["en"]}</h2><h2 class="subsection-title">{item["zh"]}</h2></div>'
    elif item["type"] == "h3":
        return f'<div class="bilingual-para"><h3 class="subsection-title">{item["en"]}</h3><h3 class="subsection-title">{item["zh"]}</h3></div>'
    elif item["type"] == "p" or item["type"] == "strong_p":
        en_text = item["en"]
        zh_text = item["zh"]
        if item["type"] == "strong_p":
            en_text = f'<strong>{en_text}</strong>'
            zh_text = f'<strong>{zh_text}</strong>'
        return f'<div class="bilingual-para"><p class="b-en">{en_text}</p><p class="b-zh">{zh_text}</p></div>'
    elif item["type"] == "quote":
        author_zh = item["author"]
        if author_zh == "Alfred Adler":
            author_zh = "阿尔弗雷德·阿德勒"
        elif author_zh == "Maxwell Maltz":
            author_zh = "麦克斯威尔·马尔茨"
        elif author_zh == "Naval Ravikant":
            author_zh = "纳瓦尔·拉维康特"
        elif author_zh == "Mihaly Csikszentmihalyi":
            author_zh = "米哈里·契克森米哈赖（心流之父）"
        elif author_zh == "Dan Koe":
            author_zh = "丹·柯"
            
        return f'<div class="bilingual-para"><div class="inner-quote"><p class="b-en">"{item["en"]}"</p><p class="b-zh">“{item["zh"]}”</p><span>— {item["author"]} / {author_zh}</span></div></div>'
    elif item["type"] == "list":
        lis = ""
        for li in item["items"]:
            lis += f'<li><span class="b-en" style="display:block; margin-bottom:4px; font-style:italic; opacity:0.85;">{li["en"]}</span><span class="b-zh" style="display:block; color:var(--text-primary);">{li["zh"]}</span></li>'
        return f'<div class="bilingual-para"><ul>{lis}</ul></div>'
    return ""

def main():
    html_path = "index.html"
    if not os.path.exists(html_path):
        print("index.html not found in current directory.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Generate the contents for each section
    en_html = '<div class="badge">Part 01</div>\n<h1 class="section-title serif-heading">Original Article: How to Fix Your Entire Life in 1 Day</h1>\n<div class="content-text original-text-area">\n'
    for item in ARTICLES:
        en_html += render_english(item) + "\n"
    en_html += "</div>"

    zh_html = '<div class="badge">Part 02</div>\n<h1 class="section-title">中文译文：如何在一天内重塑你的整个人生</h1>\n<div class="content-text translation-text-area">\n'
    for item in ARTICLES:
        zh_html += render_chinese(item) + "\n"
    zh_html += "</div>"

    bi_html = '<div class="badge">Part 03</div>\n<h1 class="section-title">中英双语对照阅读</h1>\n<div class="content-text bilingual-text-area">\n'
    for item in ARTICLES:
        bi_html += render_bilingual(item) + "\n"
    bi_html += "</div>"

    # Now replace in index.html
    # We want to replace the sections using regular expressions or manual slicing
    orig_start = content.find("<!-- SECTION 1: ORIGINAL EN -->")
    trans_start = content.find("<!-- SECTION 2: TRANSLATION ZH -->")
    bi_start = content.find("<!-- SECTION 3: BILINGUAL SPLIT -->")
    analysis_start = content.find("<!-- SECTION 4: ANALYSIS & WORKSHOP -->")

    if -1 in [orig_start, trans_start, bi_start, analysis_start]:
        print("Could not find section comment boundaries in index.html.")
        return

    part0 = content[:orig_start]
    part1 = f"<!-- SECTION 1: ORIGINAL EN -->\n<section class='doc-section active-section' id='original-en'>\n{en_html}\n</section>\n\n"
    part2 = f"<!-- SECTION 2: TRANSLATION ZH -->\n<section class='doc-section' id='translation-zh'>\n{zh_html}\n</section>\n\n"
    part3 = f"<!-- SECTION 3: BILINGUAL SPLIT -->\n<section class='doc-section' id='bilingual-split'>\n{bi_html}\n</section>\n\n"
    part4 = content[analysis_start:]

    new_content = part0 + part1 + part2 + part3 + part4

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully compiled index.html with full translated sections.")

if __name__ == "__main__":
    main()
