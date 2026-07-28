import os

ARTICLES = [
    {
        "id": 1,
        "title_en": "1. Two Types of People",
        "title_zh": "1. 两种类型的人",
        "quote_en": "Health isn't optional. In your 30s, your habits compound for better or for worse.",
        "quote_zh": "健康不是可选项。到了 30 多岁，无论好坏，你的各种习惯都会产生复利效应。",
        "content": [
            {
                "en": "When you hit your 40s, you're going to see two types of people. Those who took care of themselves and those who did not.",
                "zh": "到了 40 多岁的时候，你会看到两种类型的人：一种是那些懂得照顾自己的人，另一种则是那些不懂得照顾自己的人。"
            },
            {
                "en": "The gap is brutal. One group is thriving. They're sharp, energetic, building wealth, and present with their families. The other is declining. They're living in a fog, tired, wondering where it all went wrong.",
                "zh": "差距巨大得令人难以置信。一方过得很好：他们聪明、有活力，不断创造财富，还能与家人共度美好时光。而另一方则每况愈下：他们生活在迷茫之中，疲惫不堪，不明白自己究竟哪里做错了。"
            },
            {
                "en": "Health isn't optional. In your 20s, you can get away with a lot. But in your 30s, your habits compound for better or for worse.",
                "zh": "健康不是可选择性的事情。在 20 多岁时，你可以随心所欲地生活。但到了 30 多岁，无论好坏，你的各种习惯都会逐渐累积起来，产生持久的影响。"
            }
        ]
    },
    {
        "id": 2,
        "title_en": "2. Lifting Weights Is Non-Negotiable",
        "title_zh": "2. 举重训练是不可或缺的训练内容",
        "quote_en": "It's way better to be the oldest person in the weight room than the youngest person in the nursing home.",
        "quote_zh": "比起成为养老院里最年轻的人，做健身房里年纪最大的人要好得多。",
        "content": [
            {
                "en": "You lose 3-8% of muscle mass every decade after 30. And this rate accelerates after 60.",
                "zh": "30 岁之后，每十年肌肉量会减少 3%到 8%。而 60 岁以后，这一下降速度还会进一步加快。"
            },
            {
                "en": "Lifting weights is an investment in your future self. When you're 60, 70, 80, weight lifting is what keeps you functional and independent as you age. It's what keeps you mobile and out of a nursing home.",
                "zh": "举重是对自己未来的投资。当你 60 岁、70 岁、80 岁时，举重能帮助你保持行动能力与独立性。它能让你继续独立生活，不必入住养老院。"
            },
            {
                "en": "It's way better to be the oldest person in the weight room than the youngest person in the nursing home.",
                "zh": "比起成为养老院里最年轻的人，做健身房里年纪最大的人要好得多。"
            }
        ]
    },
    {
        "id": 3,
        "title_en": "3. You Are What You Eat",
        "title_zh": "3. 人如其食",
        "quote_en": "Eat a whole nutrient based diet and stop trying to out-supplement a trash diet.",
        "quote_zh": "坚持食用富含营养的饮食，不要再试图用各种补充剂来弥补不健康的饮食结构了。",
        "content": [
            {
                "en": "The foods you take in are investments in your present and future energy, mood, and health.",
                "zh": "你摄入的食物，其实是对你当前和未来的精力、情绪以及健康状况的“投资”。"
            },
            {
                "en": "If you're feeling foggy, irritable, low energy, etc., look no further than the fuel you're putting into your body.",
                "zh": "如果你感到头脑不清醒、易怒、缺乏精力等等，那就先看看自己摄入体内的“燃料”吧。"
            },
            {
                "en": "Studies consistently show that the nutrients you consume directly contribute to either positive or negative mental health.",
                "zh": "各项研究都表明，我们所摄入的营养物质会直接影响到我们的心理健康状况，要么带来积极影响，要么带来消极影响。"
            },
            {
                "en": "Eat a whole nutrient based diet and stop trying to out-supplement a trash diet.",
                "zh": "坚持食用富含营养的饮食，不要再试图用各种补充剂来弥补不健康的饮食结构了。"
            }
        ]
    },
    {
        "id": 4,
        "title_en": "4. You Are When You Eat",
        "title_zh": "4. 吃饭的时间与时机至关重要（时间营养学）",
        "quote_en": "Eat your final meal 3-5 hours before bed. Eat your first meal 1-2 hours after waking.",
        "quote_zh": "在睡前 3 到 5 小时进食最后一餐。在醒来后 1-2 小时再进食第一餐。",
        "content": [
            {
                "en": "One of the most underrated tools to getting healthy is to create the best meal schedule for you.",
                "zh": "保持健康的最有效方法之一，就是为自己制定一份合适的饮食计划。"
            },
            {
                "en": "It's a concept called Chrononutrition and it's simple:",
                "zh": "这是个名为“时间营养学”的概念，其实很简单："
            },
            {
                "en": "Eat your final meal 3-5 hours before bed. This lets your body digest and improves sleep quality.",
                "zh": "在睡前 3 到 5 小时进食最后一餐。这样有助于身体消化，同时也能提升睡眠质量。"
            },
            {
                "en": "Eat your first meal 1-2 hours after waking to regulate your appetite, hunger, and turn on your circadian rhythms.",
                "zh": "在醒来后 1-2 小时再进食，有助于调节食欲和饥饿感，同时也有助于调整生物钟。"
            },
            {
                "en": "Put a meal in between if you want. Do this for about 7 days and your body will start to adapt to the times you're eating. Your hunger stops being random.",
                "zh": "如果愿意的话，可以中间加一顿饭。坚持这样做大约 7 天，你的身体就会开始适应你的进食时间。饥饿感不再那么无规律了。"
            }
        ]
    },
    {
        "id": 5,
        "title_en": "5. Good Sleep Is Key",
        "title_zh": "5. 良好的睡眠至关重要",
        "quote_en": "Sleep is the best performance-enhancing drug on the planet, and it's completely free.",
        "quote_zh": "睡眠是地球上最有效的提升表现的方法，而且完全免费。",
        "content": [
            {
                "en": "Sleep is the best performance-enhancing drug on the planet, and it's completely free.",
                "zh": "睡眠是地球上最有效的提升表现的方法，而且完全免费。"
            },
            {
                "en": "At bare minimum, aim for 7-9 hours every night with similar sleep and wake times. To enhance quality, focus on fixing your environment so you can make sleep evergreen.",
                "zh": "至少，每晚应保证 7 到 9 小时的睡眠时间，同时保持规律的作息时间。为了提升睡眠质量，务必改善睡眠环境，让睡眠成为一种自然而然的习惯。"
            },
            {
                "en": "Most people won't admit this, but when you fix your horrible sleep habits, you fix a lot of problems in life.",
                "zh": "大多数人不会承认这一点，但当你改掉那些糟糕的睡眠习惯后，生活中的许多问题都会迎刃而解。"
            }
        ]
    },
    {
        "id": 6,
        "title_en": "6. Care About Your Appearance",
        "title_zh": "6. 在意自己的外表",
        "quote_en": "Everyone says not to judge a book by its cover. What do people actually do? They judge a book by its cover.",
        "quote_zh": "大家都说不要以貌取人，但人们实际上总是以貌取人。",
        "content": [
            {
                "en": "Everyone says not to judge a book by its cover. What do people actually do? They judge a book by its cover.",
                "zh": "大家都说，不要以貌取人。人们到底是怎么做的呢？他们总是根据外表来评判事物。"
            },
            {
                "en": "If you want to care about your appearance, it starts with your body: taking care of it, putting in the right foods, lifting, exercising, moving, sleeping.",
                "zh": "如果你想注重自己的外表，那就得从照顾好自己的身体开始：合理饮食、进行锻炼、保持身体活动、保证充足的睡眠。"
            },
            {
                "en": "Then we get into the finer details: your haircut, the clothes you wear. You don't need to be a fashionista. You just need to care about how you look.",
                "zh": "接着，我们再来看看一些更细节的部分：你的发型、你穿的衣服。你不必非得成为时尚达人。只要在乎自己的外表就好了。"
            },
            {
                "en": "Once you start doing this, people will treat you a lot differently. And that's for the better.",
                "zh": "一旦你开始这么做，人们对待你的方式就会大不相同。而那当然是件好事。"
            }
        ]
    },
    {
        "id": 7,
        "title_en": "7. Embrace New Technology",
        "title_zh": "7. 拥抱新技术",
        "quote_en": "Use AI as a thinking partner. DO NOT outsource your thinking to AI.",
        "quote_zh": "应将人工智能视为辅助思考的工具，切勿将所有的思考任务都交给 AI。",
        "content": [
            {
                "en": "When I was in my 30s, it was the internet. Now that I'm in my 40s, it's AI.",
                "zh": "我 30 多岁的时候，是互联网改变了世界。现在我 40 多岁了，则是人工智能在发挥着重要作用。"
            },
            {
                "en": "You would not believe the amount of 30 year olds I talk to who are NOT using AI on a regular basis. Mind boggling.",
                "zh": "你简直无法相信，我遇到的 30 岁人群中，竟然有那么多人并不经常使用人工智能。真是不可思议。"
            },
            {
                "en": "Whatever the new technology is, use it as much as you can. This will put you ahead of everyone else that is not using it.",
                "zh": "无论这项新技术是什么，都要尽可能地加以利用。这样，你就能比那些不使用这项技术的人更胜一筹。"
            },
            {
                "en": "The people who resisted the internet got left behind. The people resisting AI right now are making the same mistake.",
                "zh": "那些抵制互联网的人被抛在了后面。现在，那些抵制人工智能的人也在重蹈同样的错误。"
            },
            {
                "en": "Important note: Use AI as a thinking partner. DO NOT outsource your thinking to AI. Thinking is a muscle that atrophies the less you use it.",
                "zh": "重要提示：应将人工智能视为辅助思考的工具，切勿将所有的思考任务都交给人工智能来完成。思考能力就像肌肉一样，如果不经常使用，就会逐渐退化。"
            }
        ]
    },
    {
        "id": 8,
        "title_en": "8. Desexualize Your Brain",
        "title_zh": "8. 让大脑摆脱低级欲望与干扰",
        "quote_en": "Desexualize your brain as soon as possible. Divert the energy saved into the development of self.",
        "quote_zh": "尽快让大脑不再受欲望的支配。省下来的精力，可以用来提升自我。",
        "content": [
            {
                "en": "One of the best things I've ever done for my life was to quit watching porn. That shit will suck the life out of you if you're not careful.",
                "zh": "我这辈子做过的最正确的决定之一，就是不再看色情内容了。如果不小心的话，那东西会把你活活累死的。"
            },
            {
                "en": "And it's not just about porn. It's about not clicking on Instagram thirst accounts. It's about not engaging with AI companions or whatever weird shit is coming out now.",
                "zh": "这不仅仅与色情内容有关。还包括不要去点击社交平台上那些博眼球的账号，不要与人工智能‘伴侣’之类的东西互动，或者参与那些奇怪的玩意儿。"
            },
            {
                "en": "Desexualize your brain as soon as possible. The energy you save? Divert it into the development of self.",
                "zh": "尽快让大脑不再受欲望的支配吧。省下来的精力，可以用来提升自我。"
            },
            {
                "en": "Stop giving your chi away to pixels.",
                "zh": "别再把你的精力浪费在那些像素上了。"
            }
        ]
    },
    {
        "id": 9,
        "title_en": "9. Walking Is the Best Habit",
        "title_zh": "9. 步行是最好的习惯",
        "quote_en": "Walk when you're stressed. Walk when you're angry. Walk when you need creativity.",
        "quote_zh": "感到压力大时去散步，生气时去散步，需要创意时去散步。步行是地球上最被低估的运动。",
        "content": [
            {
                "en": "One of the best habits you can ever bring into your life is to walk.",
                "zh": "你能养成的最佳习惯之一，就是坚持走路。"
            },
            {
                "en": "Walk when you're stressed. Walk when you're angry. Walk when you need creativity. Walk to gain clarity.",
                "zh": "感到压力大时，就去散步吧。生气的时候，也去散步吧。需要发挥创造力时，不妨去散步。想要清醒头脑的话，也请去散步吧。"
            },
            {
                "en": "Walking is the most underrated exercise on the planet. It burns calories. It's accessible. It's sustainable. It improves brain function. It reduces stress.",
                "zh": "步行是地球上最被低估的运动方式。它能帮助燃烧卡路里，而且随时随地都可以进行。这种运动既方便又可持续。此外，步行还能改善大脑功能、减轻压力。"
            },
            {
                "en": "Make it the default and your life will change.",
                "zh": "将其设为默认习惯，你的生活将会因此改变。"
            }
        ]
    },
    {
        "id": 10,
        "title_en": "10. Money Is a Horrible Master",
        "title_zh": "10. 金钱是个糟糕的主宰者",
        "quote_en": "Money is a great slave but a horrible master. Use it to buy your freedom, not status.",
        "quote_zh": "金钱是极好的“奴隶”，却是糟糕的“主人”。用它来换取自由，而非虚荣的地位。",
        "content": [
            {
                "en": "Money is a great slave but a horrible master.",
                "zh": "金钱是极好的“奴隶”，却是糟糕的“主人”。"
            },
            {
                "en": "Use it to buy your freedom, not status. First: clear off any consumer debt. Then invest in assets and yourself.",
                "zh": "用它来换取自由，而非虚荣的地位。首先，还清所有的消费债务。然后再将资金用于投资资产和自我提升上。"
            },
            {
                "en": "I remember seeing a tweet from some guy saying, 'Buy a Rolex and go into debt if you have to.' His rationalization was that he attracted his partner and business because of the Rolex. This is one of the WORST things you can do.",
                "zh": "我记得看到有个人发推文说：“就算要负债，也要买一块劳力士。”他的理由是，自己能吸引到伴侣和合作伙伴全靠劳力士。而这绝对是你能做的最糟糕的事情之一。"
            },
            {
                "en": "If you attract a partner based on your watch, you'll get exactly what you paid for. If you need a Rolex to attract business, you lack the skills to persuade people.",
                "zh": "如果你想用手表来吸引伴侣，那你得到的只会与你的投入成正比。如果你想用劳力士来赢得业务，那说明你缺乏说服他人的能力。"
            },
            {
                "en": "Most purchases are just a form of artificial status elevation and it's best to exit that game as quick as you can. Because greatest forms of status cannot be bought. They must be earned.",
                "zh": "大多数购物行为只是为了虚荣心地提升社会地位罢了。最好能尽快摆脱这种虚荣行为。因为最崇高的地位是无法用金钱买来的，它们必须通过努力才能获得。"
            }
        ]
    },
    {
        "id": 11,
        "title_en": "11. Who Are You Asking for Advice?",
        "title_zh": "11. 你向谁寻求建议呢？",
        "quote_en": "Stop asking advice from people who have never been where you want to be.",
        "quote_zh": "请不要向那些从未达到过你想要达到的境界的人寻求建议。",
        "content": [
            {
                "en": "This is self-explanatory, but stop asking advice from people who have never been where you want to be.",
                "zh": "这不用多解释，但请不要向那些从未达到过你想要达到的境界的人寻求建议。"
            },
            {
                "en": "Why would you take fitness advice from someone out of shape? Business advice from someone who's never built anything? Parenting advice from non-parents?",
                "zh": "为什么要听那些身材不佳的人关于健身的建议呢？为什么要听那些从未成功创造过任何东西的人关于商业的建议呢？为什么要听那些没有孩子的人关于育儿的建议呢？"
            },
            {
                "en": "Find people who have the results you want. Listen to them. Ignore everyone else.",
                "zh": "找到那些拥有你想要的结果的人。倾听他们的意见。忽略其他所有人。"
            }
        ]
    },
    {
        "id": 12,
        "title_en": "12. Stop Thinking It's Too Late",
        "title_zh": "12. 别再觉得为时已晚了",
        "quote_en": "At 30, you're not late. You're early. You finally have enough wisdom to know what matters.",
        "quote_zh": "30 岁时，你并不算晚。相反，你反而很早。你终于有了足够的智慧来明白什么才是重要的。",
        "content": [
            {
                "en": "When I was 24, I thought it was too late to switch careers. At 30, I thought it was too late to start a business. Crazy.",
                "zh": "24 岁时，我觉得换职业为时已晚。30 岁时我觉得自己创业已经太晚。真是荒谬。"
            },
            {
                "en": "At 30, you're not late. You're early. You finally have enough wisdom to know what matters and enough time to build it.",
                "zh": "30 岁时，你并不算晚。相反，你反而很早。你现在终于有了足够的智慧来明白什么才是重要的，也有了足够的时间去实现它。"
            },
            {
                "en": "Forget the 'too late' nonsense. At 30, you're just getting started.",
                "zh": "别再提什么“为时已晚”的废话了。30 岁的人，才刚刚开始人生旅程而已。"
            }
        ]
    },
    {
        "id": 13,
        "title_en": "13. Stop Taking Things Personally",
        "title_zh": "13. 别把别人的言行太往心里去 (API思维)",
        "quote_en": "If you are easily offended, you are easily manipulated. Adopt API—Always Assume Positive Intent.",
        "quote_zh": "如果你容易受冒犯，你就很容易被别人操纵。采用 API 思维方式：始终假设对方出于善意。",
        "content": [
            {
                "en": "If you are easily offended, you are easily manipulated. Stop taking things personally.",
                "zh": "如果你容易生气、容易受冒犯，那你就很容易被别人操纵。别把别人的言行太往心里去。"
            },
            {
                "en": "Take it a step further by adopting a mental frame called API—Always Assume Positive Intent.",
                "zh": "再进一步，可以采用一种名为“API”的思维方式——始终假设对方出于善意（Always Assume Positive Intent）。"
            },
            {
                "en": "Life is way too short to give mental energy to slights and perceived insults.",
                "zh": "人生太短暂了，没必要把精力浪费在那些无端的冒犯和误解上。"
            }
        ]
    },
    {
        "id": 14,
        "title_en": "14. Perception Is Power",
        "title_zh": "14. 感知即力量 (框架效应)",
        "quote_en": "Reality is not actually reality. Your perception is your reality. Same facts, different frame, different life.",
        "quote_zh": "现实并非客观全貌，你的感知才是你的现实。同样的事实，因为呈现视角不同，结果截然不同。",
        "content": [
            {
                "en": "Your biggest mental superpower is the ability to control your perception. Reality is not actually reality. Your perception is your reality.",
                "zh": "你最强大的心理能力，就是能够掌控自己的感知方式。现实其实并非真正的客观现实，你所感知到的，才是你的现实。"
            },
            {
                "en": "Psychologists call it the Framing Effect: The same information presented differently produces completely different decisions and emotional responses. Same facts, different frame, different life.",
                "zh": "心理学家将这种现象称为“框架效应”：同样的信息，如果以不同的方式呈现出来，就会导致完全不同的决策和情感反应。同样的事实，因为呈现方式的差异，会带来截然不同的结果。"
            },
            {
                "en": "I can take two people with the exact same background, put them through the exact same situation, and get two wildly different outcomes. One becomes a victim. The other sees a lesson and a path forward. The difference isn't the event. It's the lens.",
                "zh": "我可以找两个背景完全相同的人，让他们面对完全相同的处境，结果却截然不同：一个人沦为受害者，而另一个人则能从中吸取教训，找到前进的方向。区别不在于事件本身，而在于看待事件的视角。"
            },
            {
                "en": "Your lens is trained by the people you hang around, the media you consume, the environment you stay in.",
                "zh": "你所形成的观念，其实是由你经常交往的人、你接触的媒体以及你所处的环境所塑造的。"
            },
            {
                "en": "But here's what most people miss: you can choose your perception. Reframe stress as challenge. Failure as feedback. Obstacles as training. You don't control every event. You control which interpretation you reinforce.",
                "zh": "但大多数人忽略了一点：你可以自行选择如何看待这些事情。把压力视为挑战，把失败当作反馈，把障碍看作锻炼的机会。你无法控制每一件事情的发生，你能做的，只是决定要强化哪种解读方式而已。"
            }
        ]
    },
    {
        "id": 15,
        "title_en": "15. Change Your Thoughts to Change Your Reality",
        "title_zh": "15. 改变思维方式，才能改变现实",
        "quote_en": "Your thoughts create your beliefs, which lead to your actions, which become your reality.",
        "quote_zh": "你的想法造就了你的信念，这些信念又引导你的行为，而你的行为则构成了你的现实。",
        "content": [
            {
                "en": "The way you change your reality is to start with how you think.",
                "zh": "改变现实的方式，首先在于改变自己的思维方式。"
            },
            {
                "en": "Your thoughts create your beliefs, which lead to your actions, which become your reality.",
                "zh": "你的想法造就了你的信念，这些信念又引导你的行为，而你的行为则构成了你的现实。"
            },
            {
                "en": "If you want to change your reality, look no further than your level of thinking. You can change your thoughts. It takes effort, but you can do this.",
                "zh": "如果你想改变自己的现实，那就先从自己的思维方式入手吧。你可以改变自己的想法。这需要付出努力，但你是可以做到的。"
            }
        ]
    },
    {
        "id": 16,
        "title_en": "16. Frame Failure as an Iteration",
        "title_zh": "16. 将失败视为一种尝试与迭代过程",
        "quote_en": "Your rate of iteration is equal to your rate of success. Want to succeed faster? Do more experiments.",
        "quote_zh": "你的迭代速度，其实就等于你的成功速度。想更快取得成功？多做实验，加快迭代。",
        "content": [
            {
                "en": "Stop framing things that didn't work out as failures. Frame them as iterations.",
                "zh": "不要把那些没有成功的事情视为失败。应该把它们看作是尝试的过程而已。"
            },
            {
                "en": "Imagine if Thomas Edison tried to create the light bulb for the first time and said, 'Okay, well that didn't work. I guess it's a failure.' No. He tried 10,000 iterations to create something we use every single day.",
                "zh": "试想一下，如果托马斯·爱迪生在第一次尝试发明电灯泡时说：“好吧，这次没成功。看来算是失败了。”会怎么样呢？不，他尝试了上万次迭代，最终创造了我们每天都在使用的东西。"
            },
            {
                "en": "Your rate of iteration is equal to your rate of success. Want to succeed faster? Do more experiments. Iterate faster.",
                "zh": "你的迭代速度，其实就等于你的成功速度。想更快取得成功吗？那就多做实验，加快迭代速度。"
            }
        ]
    },
    {
        "id": 17,
        "title_en": "17. Judge Actions, Not Words",
        "title_zh": "17. 应以行动而非言语来评判人",
        "quote_en": "Behavior is the most accurate way of assessing character. Words are cheap. Watch what people do.",
        "quote_zh": "行为是衡量一个人品格的最准确方式。言语容易说出口，但要看人们的实际行为。",
        "content": [
            {
                "en": "Never judge a person based on what they say. Judge them based on what they do.",
                "zh": "永远不要根据一个人的话来评判他。应该根据他的行为来评判他。"
            },
            {
                "en": "Behavior is the most accurate way of assessing character, especially when it comes to the people you allow into your life.",
                "zh": "行为是衡量一个人品格的最准确方式，尤其是对于那些你允许进入自己生活的人而言。"
            },
            {
                "en": "Words are cheap. Watch what people do.",
                "zh": "言语容易说出口。但要看人们的实际行为。"
            }
        ]
    },
    {
        "id": 18,
        "title_en": "18. Learn From People You Disagree With",
        "title_zh": "18. 向那些与你意见相左的人学习",
        "quote_en": "You will get so much farther in life when you stay objective and learn from people you disagree with.",
        "quote_zh": "如果你能保持客观态度，愿意向那些与你意见相左的人学习，你在人生中会取得更大的成就。",
        "content": [
            {
                "en": "Most times when people disagree with someone, they see it as a reflection of their entire personality when it's just one thing they disagree with.",
                "zh": "大多数时候，当人们与他人意见不合时，他们往往会认为这反映了对方的整个人格缺陷，而实际上，他们可能只是在某一件具体事情上存在分歧而已。"
            },
            {
                "en": "This is a sign of protecting your ego, staying in an echo chamber, and being a snowflake.",
                "zh": "这是自我保护的表现，是活在自我的小圈子里、不愿接受现实的表现。"
            },
            {
                "en": "You will get so much farther in life when you stay objective and learn from people you disagree with.",
                "zh": "如果你能保持客观态度，愿意向那些与你意见相左的人学习，那么你在人生中会取得更大的成就。"
            },
            {
                "en": "Or you can stay in your echo chamber and keep thinking the same thoughts over and over. We'll see how that works out.",
                "zh": "或者，你也可以继续待在自己的“回音室”里，反复思考着同样的想法。让我们看看那样做会有什么结果吧。"
            }
        ]
    },
    {
        "id": 19,
        "title_en": "19. Forgive the Four People in Your Life",
        "title_zh": "19. 原谅你生命中的那四个人吧",
        "quote_en": "Forgive your parents, those who left, those who wronged you, and forgive yourself.",
        "quote_zh": "原谅你的父母、离开你的人、伤害过你的人，以及最难原谅的——你自己。",
        "content": [
            {
                "en": "Forgive your parents. Resenting the people who gave you life is like taking a poison pill and expecting them to get hurt. Forgiveness releases resentment and frees up energy.",
                "zh": "原谅你的父母吧。怨恨那些赋予你生命的人，就好比自己吞下毒药，却希望别人因此受伤。宽恕能消除怨恨，释放出更多的正能量。"
            },
            {
                "en": "Forgive the people who didn't stay. Exes, former friends. Stop carrying the burden. Learn and move on.",
                "zh": "请原谅那些没有留下来的人吧。那些前任、曾经的友人……不必再背负着他们的重担了。学会放下，继续前行吧。"
            },
            {
                "en": "Forgive people who wronged you. Holding onto resentment hurts you, not them.",
                "zh": "原谅那些伤害过你的人吧。心怀怨恨只会伤害你自己，而不会伤害到他们。"
            },
            {
                "en": "Forgive yourself. The hardest one. Learn from those situations, forgive, and move on.",
                "zh": "原谅自己吧。这是最难做到的。从那些经历中吸取教训，然后原谅自己，继续前进吧。"
            }
        ]
    },
    {
        "id": 20,
        "title_en": "20. Who Do You Surround Yourself With?",
        "title_zh": "20. 你身边都和谁在一起呢？",
        "quote_en": "If they don't match the reality you want to build, find a better group.",
        "quote_zh": "如果身边的人不符合你想要构建的现实与未来，你不得不另找更合适的圈子。",
        "content": [
            {
                "en": "If you want better results in life, look at the people you surround yourself with.",
                "zh": "如果你想在生活中取得更好的成绩，那就看看你身边的人吧。"
            },
            {
                "en": "If they don't match the reality you want to build, unfortunately, you're going to have to find a better group.",
                "zh": "如果他们不符合你想要构建的现实状况，那么很遗憾，你不得不另找一家更合适的团队或圈子了。"
            },
            {
                "en": "This isn't about being disloyal. It's about being intentional with the most important input in your life.",
                "zh": "这并非出于不忠，而是为了慎重对待人生中最重要的投入。"
            }
        ]
    },
    {
        "id": 21,
        "title_en": "21. Be the Dumbest Person in the Room",
        "title_zh": "21. 当房间里最愚蠢的人吧",
        "quote_en": "You level up by process of osmosis. Get around people who are levels ahead of you.",
        "quote_zh": "提升自己其实是一个“渗透”过程。多去和那些比你优秀的人相处。",
        "content": [
            {
                "en": "You become smarter by being the dumbest person in the room. You become fitter by being the least fit person in the gym.",
                "zh": "通过成为房间里最笨的人，你反而会变得更聪明。通过成为健身房里体能最差的人，你反而会变得更健康。"
            },
            {
                "en": "Stop protecting your ego. Get around people who are levels ahead of you.",
                "zh": "别再维护自己的自尊心了。远离那些不如你的人，多去和那些比你优秀的人相处。"
            },
            {
                "en": "Something I realized by continually doing this: you level up by process of osmosis. You see how they act, think, and behave. When you hang around people operating at a higher level, you start to adopt that same level inside your own life.",
                "zh": "通过不断这样做，我明白了：提升自己其实是一个循序渐进的“渗透”过程。你可以观察到他们的行为方式、思维模式和行事风格。当你与那些处于更高境界的人相处时，你也会在自己的生活中开始采用同样的方式来行事。"
            }
        ]
    },
    {
        "id": 22,
        "title_en": "22. Money Can't Buy You Fulfillment",
        "title_zh": "22. 金钱买不来真正的满足感",
        "quote_en": "A great life is based on things money can't buy: doing work you love, being healthy, having a great family.",
        "quote_zh": "美好的生活离不开金钱买不到的东西：做热爱的事业、保持健康、拥有美好的家庭。",
        "content": [
            {
                "en": "Most people think a great life is about money, cars, and houses.",
                "zh": "大多数人认为，美好的生活就是拥有金钱、汽车和房子。"
            },
            {
                "en": "The reality is that a great life is based on things money can't buy: doing work you love, being healthy, having a great family, and great relationships.",
                "zh": "事实上，美好的生活离不开金钱所能买不到的东西：做自己热爱的事业、保持健康、拥有美好的家庭和和谐的人际关系。"
            },
            {
                "en": "I'm always focused on making sure I don't over-index on external measures of success and index heavily on the ones that create a fulfilling life.",
                "zh": "我始终努力确保自己不会过分依赖外在的成功标准，而是更重视那些能带来真正幸福感与充实感的因素。"
            }
        ]
    },
    {
        "id": 23,
        "title_en": "23. Focus on the Right Constraints",
        "title_zh": "23. 专注于正确的约束条件/限制因素",
        "quote_en": "Success is less about addition and more about subtraction. Remove bottlenecks.",
        "quote_zh": "成功的关键不在于添加，而在于去除那些阻碍前进的瓶颈障碍。",
        "content": [
            {
                "en": "Constraint #1: The bottleneck. What's the one thing holding you back from achieving what you want? Fix that. Subordinate everything else. The greatest entrepreneurs aren't focused on adding more...they're removing bottlenecks. Success is less about addition and more about subtraction.",
                "zh": "约束条件 1：所谓的“瓶颈”问题。究竟是什么因素阻碍了你实现目标？请先解决这个问题。其他一切都可以暂时搁置一旁。最优秀的企业家并不专注于不断增加新的东西……他们致力于消除各种瓶颈。成功的关键不在于添加，而在于去除那些阻碍前进的障碍。"
            },
            {
                "en": "Constraint #2: Values-based constraints. Want to build a successful business? Can you get home at 5pm every night to have dinner with your family? Can you maintain your health while building? These uphold what means the most to you while achieving. This is what makes a full life.",
                "zh": "约束条件 2：基于价值观的约束。想要打造一家成功的企业吗？那你是否能够每晚 5 点回家与家人共进晚餐呢？在创业过程中，你能否保持健康呢？这些约束条件有助于确保你在实现目标的过程中，不会忽视那些对你来说最重要的事情。这才是真正让生活变得完整的关键。"
            }
        ]
    },
    {
        "id": 24,
        "title_en": "24. Use the Three Levels of Learning",
        "title_zh": "24. 运用三个学习层次来学习",
        "quote_en": "Level 1: Consumption. Level 2: Application. Level 3: Teaching. Turns experience into wisdom.",
        "quote_zh": "第一级：消费；第二级：应用；第三层：教学。通过教学，经验才能升华为智慧。",
        "content": [
            {
                "en": "Level 1: Consumption. It's what you're doing right now. This is the shallowest level of learning.",
                "zh": "第一级：消费。这就是你此刻正在做的事情。这是最浅层次的学习方式。"
            },
            {
                "en": "Level 2: Application. This turns knowledge into actual experience.",
                "zh": "第二级：应用。将知识转化为实际经验。"
            },
            {
                "en": "Level 3: Teaching. It's what I'm doing right now. This turns experience into wisdom.",
                "zh": "第三级：教学。这正是我目前所从事的工作。通过教学，经验才能转化为智慧。"
            },
            {
                "en": "When you apply all three, you learn at a deeper level than most people ever will.",
                "zh": "当你同时运用这三者时，你所能获得的理解深度，是大多数人永远无法企及的。"
            }
        ]
    },
    {
        "id": 25,
        "title_en": "25. Your Emotions Are Your Responsibility",
        "title_zh": "25. 你的情绪由你自己负责",
        "quote_en": "I created that feeling. I shouldn't blame it on anyone else.",
        "quote_zh": "是我自己创造了这种情绪，我不应该把责任推到别人身上。",
        "content": [
            {
                "en": "Something I wish they taught in high school: how to manage emotions.",
                "zh": "我希望高中时能学到的一件事：如何控制情绪。"
            },
            {
                "en": "I remember getting into arguments with my wife and saying, 'You made me feel this way.' She would always correct me—because I'm the one feeling it. I created that feeling. I shouldn't blame it on anyone else.",
                "zh": "我记得自己曾和妻子争吵时说：“是你让我有这种感觉的。”她总会纠正我——因为其实，是我自己创造了这种感觉，我不应该把责任推到别人身上。"
            },
            {
                "en": "We're trying to teach our daughters this now. You're a human being. You will feel emotions. So why not learn a system that helps you manage them instead of blaming everyone else?",
                "zh": "我们现在正试图把这种观念传授给女儿们。你们也是人，同样会感受到各种情绪。那么，为什么要不去学习一种能够帮助自己管理情绪的方法呢？何必责怪别人呢？"
            }
        ]
    },
    {
        "id": 26,
        "title_en": "26. Take Extreme Ownership",
        "title_zh": "26. 全力以赴，承担全部责任",
        "quote_en": "It may not be your fault, but it's always your responsibility. Personal power means taking ownership.",
        "quote_zh": "虽然可能不是你的错，但无论如何，你都得承担责任。个人力量意味着摆脱受害者心态。",
        "content": [
            {
                "en": "Take ownership of every single result in your life.",
                "zh": "为自己人生中的每一个结果负责。"
            },
            {
                "en": "This means getting away from victimhood mentality. It may not be your fault, but it's always your responsibility.",
                "zh": "这意味着要摆脱“受害者心态”。虽然这可能不是你的错，但无论如何，你都得承担责任。"
            },
            {
                "en": "When you blame others, you lose agency. You give them power.",
                "zh": "当你责怪他人时，你就失去了自主权。你把权力交给了他们。"
            },
            {
                "en": "Personal power means avoiding blaming others for what's happening in your own life.",
                "zh": "个人力量意味着不要把自己生活中发生的事情归咎于他人。"
            }
        ]
    },
    {
        "id": 27,
        "title_en": "27. Use the Vision Achievement Flywheel",
        "title_zh": "27. 利用“愿景实现飞轮”效应",
        "quote_en": "Start with a 3-year vision → 1-year goal → quarterly projects → monthly tasks → weekly tasks → daily schedule.",
        "quote_zh": "首先设定 3 年远景目标 → 拆分为 1 年目标 → 季度任务 → 月/周任务 → 每日计划。每天完成至少 3 项任务。",
        "content": [
            {
                "en": "Your mind is a goal-seeking machine, and most people give it the wrong goals. You need something to focus on, or a goal will be given to you.",
                "zh": "你的大脑其实是一台追求目标的机器，只不过大多数人给它设定的目标都是错误的。你需要有个明确的焦点或目标来引导自己。"
            },
            {
                "en": "When I first became a trainer, I read an article by Paul Chek about goal setting. He said people are more likely to achieve goals if they write them down. Action step: write down 20 goals.",
                "zh": "当我刚开始从事培训师工作时，我读了关于目标设定的文章。文章说如果把目标写下来，人们就更有可能实现它们。行动建议：请写下 20 个目标吧。"
            },
            {
                "en": "I gave it a shot. Wrote down 20 goals, put the paper in my desk and forgot about it. Six months later, I found that paper and started crossing off goals I'd achieved at least half the list.",
                "zh": "我试过了。列出了 20 个目标，把纸放进抽屉里就没管过。六个月后找到那张纸，发现已经勾掉了至少一半的目标。"
            },
            {
                "en": "Here's my system now: Start with a 3-year vision → Break into 1-year goal → quarterly projects → monthly tasks → weekly tasks → daily schedule.",
                "zh": "我的规划方式如下：首先设定 3 年的远景目标，然后拆分为 1 年目标、季度任务、月度/周度任务和每日任务。"
            },
            {
                "en": "Knock down at least three tasks every day. Start at the end and work backward. Everything you want is attainable.",
                "zh": "每天至少完成三项任务。从终点倒推，你想要的一切都是可以实现的。"
            }
        ]
    },
    {
        "id": 28,
        "title_en": "28. Focus on the Process",
        "title_zh": "28. 专注于过程本身",
        "quote_en": "'I enjoy the climb. I don't care where the summit is.' Focus on each step and make the journey fun.",
        "quote_zh": "“我喜欢攀登的过程。我不在乎顶峰究竟在何处。”从工作中获得快乐，而非只追求成果。",
        "content": [
            {
                "en": "When you set a goal, that becomes the destination, much like GPS. Once it's set, focus on the process. Find ways to have fun doing it.",
                "zh": "当你设定一个目标时，它就相当于一个目的地，就像 GPS 一样。一旦目标确定，只需专注于实现目标的过程。试着找到让这个过程变得有趣的方法吧。"
            },
            {
                "en": "Here's what you realize after attaining goals: you don't feel happy once you attain them. The happiness was the striving. The work. The process.",
                "zh": "实现目标之后，你会意识到：一旦目标达成，你并不会感到长期快乐。真正的快乐在于追求目标的过程、付出努力的过程本身。"
            },
            {
                "en": "Russ has a line: 'I enjoy the climb. I don't care where the summit is.'",
                "zh": "拉斯有这样一句话：“我喜欢攀登的过程。我不在乎顶峰究竟在何处。”"
            },
            {
                "en": "Focus on each step and you make the journey fun. This lets you play an infinite game. Getting joy from the work itself rather than the attainment.",
                "zh": "专注于每一步，就能让整个过程变得有趣。这样，你就能永远享受这个过程了——从工作中获得快乐，而不是只追求成果本身。"
            }
        ]
    },
    {
        "id": 29,
        "title_en": "29. Your Identity Must Change",
        "title_zh": "29. 你必须改变自己的身份认知",
        "quote_en": "Achieving a goal is not about gaining things. It's about becoming the person who attracts the goal.",
        "quote_zh": "实现目标并非是为了获取某种外在东西，而是成为能够自然吸引目标实现的更优秀的人。",
        "content": [
            {
                "en": "Achieving a goal is not about gaining things. It's about becoming the person who attracts the goal as a result of who they are.",
                "zh": "实现目标并非是为了获取某种外在东西。而是通过成为那样的人，从而自然而然地吸引目标的实现。"
            },
            {
                "en": "A goal changes you. It levels you up. You literally cannot be the same person achieving a bigger goal than you were before.",
                "zh": "一个目标能改变一个人。它能让一个人变得更优秀。当你实现了比以前更伟大的目标后，你就再也不是从前的那个人了。"
            },
            {
                "en": "Focus on the behaviors it would take to attain your goal, then keep repeating them until they become who you are.",
                "zh": "专注于实现目标所需的行为，不断重复这些行为，直到它们成为你自身的习惯与身份。"
            }
        ]
    },
    {
        "id": 30,
        "title_en": "30. The Shortcut Is the Long Path",
        "title_zh": "30. 捷径其实是一条更长的路",
        "quote_en": "The shortcut is the long path. The long path is the shortcut.",
        "quote_zh": "捷径其实就是漫长的弯路。看似漫长而扎实的道路，其实才是真正的捷径。",
        "content": [
            {
                "en": "A mentor told me this and it stuck: The shortcut is the long path. The long path is the shortcut.",
                "zh": "一位导师对我说过这句话，我一直记在心里：捷径其实就是漫长的道路。漫长的道路，其实才是捷径罢了。"
            },
            {
                "en": "Think of all the times you tried to lose weight or get money as quickly as possible. How did those end up?",
                "zh": "想想看，你有多少次试图尽快减肥、暴富，结果如何呢？"
            },
            {
                "en": "Chasing shortcuts takes away the skills you need to keep the result you're trying to attain.",
                "zh": "追求捷径会让你失去守住成果所需的能力。"
            },
            {
                "en": "When it comes to getting things in life, choose the long path. It's always going to be the shortest.",
                "zh": "在生活中，当需要取得某样东西时，请选择那条看似漫长的道路。因为那往往才是最短的路径。"
            }
        ]
    },
    {
        "id": 31,
        "title_en": "31. The Three Most Important Decisions",
        "title_zh": "31. 三个最重要的决定",
        "quote_en": "The three most important decisions: What you do, Who you do it with, Where you live.",
        "quote_zh": "你将做出的三个最重要决定：你在做什么、你与谁合作/生活、你住在哪里。",
        "content": [
            {
                "en": "The three most important decisions you'll make:",
                "zh": "你将做出的三个最重要决定："
            },
            {
                "en": "1. What you do",
                "zh": "1. 你到底在做什么（事业与使命）；"
            },
            {
                "en": "2. Who you do it with (who you partner with)",
                "zh": "2. 与你合作/生活的人是谁（伴侣与圈子）；"
            },
            {
                "en": "3. Where you live",
                "zh": "3. 你住在哪里（城市与环境）。"
            },
            {
                "en": "These are where you'll spend most of your time. Make them wisely.",
                "zh": "这些地方是你大部分时间都会待的地方。请好好做决定吧。"
            }
        ]
    },
    {
        "id": 32,
        "title_en": "32. The Formula for Success",
        "title_zh": "32. 成功的通用公式",
        "quote_en": "Step 1: Show up. Step 2: Do the work. Step 3: Look for ways to improve (Kaizen). Simple, but not easy.",
        "quote_zh": "第一步：无论如何都要到位；第二步：认真完成任务；第三步：持续寻求改进（Kaizen）。",
        "content": [
            {
                "en": "Step 1: Show up. Show up when you're motivated or not, feeling it or not. This alone puts you ahead of 80% of people who only show up when they feel like it.",
                "zh": "第一步：无论如何都要到位。无论你是否有动力，无论心情如何，都要去。只要做到这一点，你就已经比那些随性而为的人强多了（这类人占到了 80% 以上）。"
            },
            {
                "en": "Step 2: Do the work. Remove distractions. Put full attention on what you need to do.",
                "zh": "第二步：认真完成任务。排除一切干扰因素，全神贯注于自己需要完成的任务上。"
            },
            {
                "en": "Step 3: Look for ways to improve. Adopt a mindset of Kaizen, meaning constant and never-ending improvement.",
                "zh": "第三步：寻找改进的方法。秉持“持续改进（Kaizen）”的理念，即不断努力提升自己。"
            },
            {
                "en": "I've used this formula to get in shape, build businesses, and grow on social media. It's simple, but don't mistake simple for easy.",
                "zh": "我运用这个方法来保持身材、打造事业。方法很简单，但千万别把简单误认为是容易。"
            }
        ]
    },
    {
        "id": 33,
        "title_en": "33. You Underestimate What You Can Do in a Year",
        "title_zh": "33. 你低估了自己在一年内能够做到的事情",
        "quote_en": "People overestimate what they can do in 6 weeks but underestimate what they can do in a year. Adopt 'As long as it takes'.",
        "quote_zh": "人们高估了自己在 6 周内能做的事，却低估了自己在一年内能完成的任务。坚持下去，无论需要多长时间。",
        "content": [
            {
                "en": "People overestimate what they can do in 6 weeks but underestimate what they can do in a year.",
                "zh": "人们高估了自己在 6 周内能做的事情，却低估了自己在一年内能完成的任务。"
            },
            {
                "en": "Imagine all those things you quit because they got hard. If you'd stuck with them for a full year, you'd be way ahead.",
                "zh": "想象一下那些因为太难而放弃的事情。如果你能坚持做下去一年，你一定会取得巨大的成就。"
            },
            {
                "en": "My biggest regrets come from not doing the thing when I should have.",
                "zh": "我最大的遗憾，就是没有在应该行动的时候采取行动。"
            },
            {
                "en": "While everyone's chasing shortcuts—get rich quick, get fit quick—adopt a different mindset: I'll do it for as long as it takes.",
                "zh": "当大家都在追求捷径——快速致富、快速减肥时，不妨采取另一种心态：我会坚持做下去，无论需要多长的时间。"
            },
            {
                "en": "Give yourself a full year, not 6 weeks. This is one of the best ways to avoid regret.",
                "zh": "给自己一整年的时间，而不是 6 周。这是避免后悔的最佳方法之一。"
            }
        ]
    }
]

def render_bilingual_article(item):
    paras = ""
    for pair in item["content"]:
        paras += f'<div class="bilingual-para"><p class="b-zh">{pair["zh"]}</p><p class="b-en">{pair["en"]}</p></div>'
    
    return f"""
    <div class="item-block" style="margin-bottom: 2.8rem; background: var(--bg-card); border: 1px solid var(--border-color); padding: 28px; border-radius: 18px; box-shadow: var(--shadow-sm);">
        <h2 class="subsection-title" style="font-size: 1.45rem; font-weight: 700; color: var(--text-primary); margin-bottom: 4px;">{item["title_zh"]}</h2>
        <div style="font-family: var(--font-serif); font-style: italic; color: var(--accent-indigo); margin-bottom: 16px; font-size: 1rem;">{item["title_en"]}</div>
        
        <div class="inner-quote" style="margin-bottom: 20px;">
            <p class="b-zh">“{item["quote_zh"]}”</p>
            <p class="b-en">"{item["quote_en"]}"</p>
        </div>
        
        {paras}
    </div>
    """

def main():
    article_html = "\n".join([render_bilingual_article(item) for item in ARTICLES])

    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>46岁的给30多岁的33条人生忠告 | 中英双语版</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="style.css">
    <style>
        .single-column-container {{
            max-width: 840px;
            margin: 0 auto;
            padding: 40px 20px 100px 20px;
        }}
        .header-nav-left {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .back-hub-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
            font-size: 0.88rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .back-hub-btn:hover {{
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--accent-indigo);
            color: #ffffff;
        }}
        .bilingual-para {{
            margin-bottom: 16px;
        }}
        .b-zh {{
            font-size: 1rem;
            line-height: 1.7;
            color: var(--text-primary);
            margin-bottom: 4px;
            font-weight: 400;
        }}
        .b-en {{
            font-size: 0.92rem;
            line-height: 1.6;
            color: var(--text-secondary);
            font-style: italic;
            margin-bottom: 0;
            opacity: 0.88;
        }}
    </style>
</head>
<body>
    <div class="app-layout">
        <header class="main-header" style="justify-content: space-between; padding: 0 24px;">
            <div class="header-nav-left">
                <a href="../index.html" class="back-hub-btn">
                    <i data-lucide="arrow-left" style="width:16px;height:16px;"></i>
                    <span>返回 Hub</span>
                </a>
                <span class="logo-text" style="font-weight:700; color:var(--text-primary);">46岁给30岁的33条忠告 (中英双语)</span>
            </div>

            <div class="header-actions">
                <button class="theme-toggle-btn" id="themeToggle" aria-label="切换主题">
                    <i data-lucide="moon" class="theme-icon-dark"></i>
                    <i data-lucide="sun" class="theme-icon-light hidden"></i>
                </button>
            </div>
        </header>

        <div class="single-column-container">
            <main class="content-panel" style="margin-left: 0; padding: 0;">
                <section class="doc-section active-section">
                    <div class="badge" style="margin-bottom: 12px;">中英双语对照长文</div>
                    <h1 class="section-title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 8px;">46岁的给30多岁的33条人生忠告</h1>
                    <div style="font-family: var(--font-serif); font-style: italic; color: var(--accent-indigo); font-size: 1.15rem; margin-bottom: 24px;">I'm 46. If You're In Your 30s, Read This</div>

                    <div class="overview-banner" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 18px; padding: 24px; box-shadow: var(--shadow-sm); margin-bottom: 2.5rem;">
                        <div class="overview-card">
                            <h3 style="font-size: 1.05rem; color: var(--accent-indigo); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;"><i data-lucide="user-check"></i> 作者前言与背景</h3>
                            <p class="b-zh" style="margin-bottom: 4px;">我在健身领域工作了 25 年，指导过成千上万的企业家，还创立了多家企业。以下是我希望在 30 多岁时能有人告诉我的 33 件事情。</p>
                            <p class="b-en">I've spent 25 years in fitness, coached thousands of entrepreneurs, and built multiple businesses. Here are things I wish someone had told me when I was in my 30s.</p>
                        </div>
                    </div>

                    <div class="content-text">
                        {article_html}
                    </div>
                </section>
            </main>
        </div>
    </div>
    <script src="app.js"></script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("[√] advice-30s index.html compiled cleanly in pure bilingual format.")

if __name__ == "__main__":
    main()
