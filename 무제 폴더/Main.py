from PrincessMakerSystem import PrincessMaker
from Story import MainStory
from Story import skip
from system import LoginSystem
from login import Start_Menu
import pandas as pd
import numpy as np
import seaborn as sns
import time

def main():
    Princess = PrincessMaker('/Users/dgsw12/Desktop/미유고/무제 폴더/Stats.csv')
    Story = MainStory

    Start_Menu()
    
    Princess.Save_Stats()
    Story.Opening()

    Story.Scene1()
    question1 = '딸이 방에서 주로 시간을 보낼 때의 모습은?'
    option1 = ['마당에서 나무 막대기를 휘두르며 노는 데 몰두한다.', '어려워 보이는 책을 펼쳐두고 집중해서 읽는다.', '집안 구석구석을 쓸고 닦으며 집사를 돕는다.', '거울 앞에 앉아 옷을 대어보며 미소를 짓는다.']
    after_option1 = [['큐브: 아가씨께서는 쉴때 나무 막대기를 휘두르시네요. 운동에 자질이 있는것 같습니다.', '딸: 아빠도 같이 할래?', '그날은 하루종일 훈련을 했다'],
                    ['큐브: 아가씨께서는 쉴때 어려운 책을 읽으시네요. 공부에 자질이 있는것 같습니다.', '딸: 아빠 모르겠는 부분이 있어, 알려줘!', '아빠: 그럼 당연히 알려주지'],
                    ['큐브: 아가씨께서는 쉴때 청소를 하시네요.', '딸 : 아빠 아빠도 같이 청소하자!', '아빠: 그래 같이 하자'],
                    ['큐브: 아가씨께서는 쉴때 거울을 보시네요. 꾸미는데 관심이 있는 것 같습니다', '딸: 아빠 나 어때 예뻐?', '아빠: 그럼 당연히 예쁘지']]
    plus_stats1 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Intellect', 'Morality', 'Tenacity'],
                    ['Stamina', 'Tenacity'], ['Attractiveness', 'Dignity']]
    minus_stats1 = [None, None, None, None]
    Princess.Choice(question1, option1, after_option1, plus_stats1, minus_stats1)

    Story.Scene2()
    question2 = '저자거리에서 딸이 가장 오랫동안 시선을 떼지 못하는 물건은?'
    option2 = ["단단하고 잘 다듬어진 연습용 목검.", "다른 나라의 역사와 지리가 적힌 고급 양장본 책.", "가족들과 함께 요리할 수 있는 신선한 식재료 모음.", "반짝거리는 보석이 박힌 예쁜 장신구."]
    after_option2 = [['큐브: 아가씨께서 목검이 마음에 드는 모양입니다. 사주실 겁니까?', '딸: 아빠 이거 사주면 안돼?', '딸: 이거 있으면 훈련할때도 좋을것 가튼데..', '귀여운 표정을 하고 애교를 부려 어쩔수 없이 사줬다.'],
                    ['큐브: 아가씨께서 저 책이 마음에 드는 모양입니다. 사주실 겁니까?', '딸: 아빠 이거 사주면 안돼?', '딸: 이 책 있으면 공부하기 조을것 같은데...', '귀여운 표정을 하고 애교를 부려 어쩔수 없이 사줬다.'],
                    ['큐브: 아가씨께서 식재료들이 마음에 드는 모양입니다. 사주실 겁니까?', '딸: 아빠 이거 사주면 안돼?', '딸: 이걸로 밥 만들어 먹으면 맛있을것 같은뎅...', '귀여운 표정을 하고 애교를 부려 어쩔수 없이 사줬다.'],
                    ['큐브: 아가씨께서 저 장신구가 마음에 드는 모양입니다. 사주실 겁니까?', '딸: 아빠 이거 사주면 안돼?', '딸: 이거 예쁜데 내가 끼면 더 예쁠것 같은뎀...', '귀여운 표정을 하고 애교를 부려 어쩔수 없이 사줬다.']]
    plus_stats2 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Intellect', 'Morality'], 
                    ['Stamina', 'Tenacity'], ['Attractiveness', 'Dignity']]
    minus_stats2 = [None, None, None, None]
    Princess.Choice(question2, option2, after_option2, plus_stats2, minus_stats2)

    Story.Scene3()
    question3 = "숲속에서 야생 몬스터를 마주쳤을 때 딸의 반응은?"
    option3 = ["망설임 없이 기세를 올려 정면으로 덤벼든다.","주변 지형을 파악하여 몬스터가 다가오지 못하게 차단한다.",'깜짝 놀라 짐을 챙겨들고 온 힘을 다해 도망친다.','몬스터의 눈을 가만히 노려보며 이상한 주문을 외운다.']
    after_option3 = [['큐브 : 앞에 몬스터가 있습니다. 어떻게 하시겠습니까 아가씨?', '딸: 당연히 정면 승부지 간다!!', '당신은 딸과 함께 몬스터와 싸워 승리했다'],
                    ['큐브 :  앞에 몬스터가 있습니다. 어떻게 하시겠습니까 아가씨?', '딸 : 저 나무 위로 올라가 몬스터의 시야에서 벗어나고 갈때까지 기다려야 겠어', '몇 분후, 몬스터가 다른곳으로 이동하였다'],
                    ['큐브 : 앞에 몬스터가 있습니다. 어떻게 하시겠습니까 아가씨?', '딸 : 뭐야?? 그런게 있으면 빨리 말해줬어야지!!!', '딸 : 뛰어!!!!'],
                    ['큐브 : 앞에 몬스터가 있습니다. 어떻게 하시겠습니까 아가씨?', '딸 : 빛이 닿지 않는 심연의 기억이여, 내 손끝에 서려라. 계약의 피를 마시고 깨어난 혼돈이여, 이 대지를 물들이고 적을 집어삼켜라!', '갑자기 몬스터가 사라졌다.']]
    plus_stats3 = [['Stamina', 'MuscularStrength'], ['Intellect','Morality'],
                    ['Stamina', 'Tenacity'],['Attractiveness','Dignity', 'Tenacity']]
    minus_stats3 = [None, None, None, None]
    Princess.Choice(question3, option3, after_option3, plus_stats3, minus_stats3)

    Story.Scene4()
    question4 = "수확제 날, 딸이 가장 흥미를 보이는 장소는?"
    option4 = ["검투사들이 서로 겨루는 중앙 무투장.", "귀족들과 학자들이 모여 담소를 나누는 연회장.", "맛있는 음식 냄새가 솔솔 풍기는 먹거리 장터.", "축제 뒤편, 가면을 쓴 사람들이 모이는 비밀 천막."]
    after_option4 = [
        ['딸: 아빠 무투장 같이 가자! 사람들이 싸우는거 보고 어떻게 싸우는지 배우고 싶어!!!', '아빠 : 그래그래 빨리 가자 실제로 싸우는거 보면 좋은 경험이 될꺼야'],
        ['딸 : 아빠 연회장 같이 가자! 사람들이랑 대화 해보고 싶어!', '아빠 : 그래그래 빨리 가자 사람들이랑 대화 하고 친해져봐'],
        ['딸 : 아빠 같이 먹거리 장터 가자! 배고파…', '아빠 :안돼 오기 전에 먹고 왔잖아', '딸 : 아니 맛있어 보이잖아 그리고 놀러 왔는데 하나만 사주면 안돼....?', '아빠 : 알았어 가자', '딸 : 히히 아빠 최고!'],
        ['딸 : 아빠 쩌어어기 뒤편에 어떤 천막있는데 가봐도 돼?', '아빠 : 뭔가 꺼림직 한데 안가면 안될까?', '딸 : 에이 한번만 가볼께 궁금하잖아', '들어 갔더니 이상한 가면쓴 사람들이 모여있다', '대화를 좀 들어보니 이상한 말들을 한다']
    ]
    plus_stats4 = [['Stamina', 'MuscularStrength'], ['Intellect', 'Morality', 'Dignity'], ['Stamina', 'Tenacity'], ['Attractiveness']]
    minus_stats4 = [None, None, None, ['Morality']]
    Princess.Choice(question4, option4, after_option4, plus_stats4, minus_stats4)

    Story.Scene5()
    question5 = "성문 근처에서 또래의 청년을 만났을 때 딸의 행동은?"
    option5 = ['어깨를 툭 치며 "너 운동 좀 했어?" 하고 아는 척한다.', '마을에 관한 이런저런 이야기를 나누며 차분히 대화한다.', '"길을 잃으셨나요?" 하며 싹싹하게 도움을 준다.',  "상대의 주머니에 있는 돈주머니를 슬쩍 눈여겨본다."]
    after_option5 = [
        ['딸 : 야 운동 좀 했다?', '청년 : 누구세요? 저를 아십니까?', '딸: 아.. 죄송합니다'],
        ['딸 : 요즘 왕자님이 방에 박혀서 안나오고 계신다는 소문이 도는데 아는거 있으신가요?', '청년 : 아어음 아마도 아프신거 아닐까요? ;;'],
        ['딸: 혹시 길을 잃으셨나요?', '청년 : 네, 혹시 저기 왕성이 어디인지 아세요?', '딸: 저 길로 3블록 정도 가다가 오른쪽으로 3블록만 가시면 있어요', '청년 : 아 감사합니다.'],
        ['딸이 은밀하게 청년의 돈주머니를 훔치려 다가간다', '딸이 손을 청년의 주머니로 손을 뻗었을 그때', '청년이 딸의 손을 붙잡았다', '청년 : 지금 뭐하시는거죠?', '딸: 아... 죄송합니다']
    ]
    plus_stats5 = [None, ['Intellect', 'Dignity', 'Morality'], ['Morality', 'Dignity'], None]
    minus_stats5 = [['Dignity', 'Morality'], None, None, ['Intellect', 'Morality', 'Dignity']]
    Princess.Choice(question5, option5, after_option5, plus_stats5, minus_stats5)

    Story.Scene6()
    question6 = "사춘기가 되어 방에서 나오지 않을 때 방 안의 모습은?"
    option6 = ["문을 두드리고 들어가 체력 단련장으로 끌고 나온다.", "따뜻한 차를 끓여 들고 가서 조용히 대화를 시도한다.", "스스로 마음이 풀릴 때까지 조용히 기다려준다.", "문틈으로 수상한 향 냄새와 검은 연기가 새어 나온다."]
    after_option6 = [
        ['딸 : 아 아빠 나가라고 !!!', '아빠 : 방에서 나와!!!', '딸 : 아 알았어..', '체력 단련장으로 가서 하루종일 훈련 당한다'],
        ['딸 : 아 아빠 나가라고 !!!', '아빠 : 딸 그러지 말고 차 끓여 왔는데 마시면서 대화 좀 할까?', '딸 : 알았어…'],
        ['아무일도 일어나지 않았다.'],
        ['딸 : 아….?', '딸 : 아니..그게;;']
    ]
    plus_stats6 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Morality', 'Attractiveness'], None, ['Attractiveness']]
    minus_stats6 = [None, None, None, None]
    Princess.Choice(question6, option6, after_option6, plus_stats6, minus_stats6)

    Story.Scene7()
    question7 = "수상한 약장수가 찾아와 약을 건넬 때 딸의 선택은?"
    option7 = ['약을 받아 들고 "먹으면 몸이 더 튼튼해지나요?" 하고 묻는다.', "출처가 불분명한 약이라며 정중히 거절한다.", '"너무 비싸요" 하며 그냥 지나친다.', "약을 삼키자 딸의 피부와 눈빛이 묘하게 매혹적으로 변한다."]
    after_option7 = [
        ['약장수: 그럼 당연히 그런 약도 있긴하지...', '딸 : 그럼 그 약 주세요', '약장수: 여기 있단다…', '딸 : 감사합니다!', '약을 먹었더니 몸이 튼튼 해졌지만 어딘가 이상해졌다'],
        ['딸: 죄송합니다. 아빠가 모르는 사람이 주는거는 먹지 말랬어요.', '갑자기 약장수가 사라졌다', '딸: ? 뭐지'],
        ['딸: 죄송합니다. 돈이 없어서요..', '갑자기 약장수가 사라졌다', '딸: ? 뭐지'],
        ['딸: 감사합니다', '약을 먹었더니 눈빛이 묘하게 매혹적이게 되었다']
    ]
    plus_stats7 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Intellect', 'Morality', 'Dignity', 'Attractiveness'], ['Intellect', 'Morality', 'Dignity'], ['Attractiveness', 'Attractiveness', 'Attractiveness']]
    minus_stats7 = [['Intellect', 'Intellect'], None, None, None]
    Princess.Choice(question7, option7, after_option7, plus_stats7, minus_stats7)

    Story.Scene8()
    question8 = "사막 오아시스에서 거친 사내를 만났을 때 딸의 태도는?"
    option8 = ['즉시 무기를 다잡으며 경계 태세를 취한다.', '차분한 태도로 누구인지, 왜 이곳에 있는지 물어본다.', '눈이 마주치자 멋쩍게 웃으며 살금살금 뒤로 물러난다.', '사내가 건네는 붉은 술잔을 망설임 없이 받아 마신다.']
    after_option8 = [
        ['딸 : 너는 누구지?? 정체를 밝히지 않으면 죽이겠다!', '사내 : 하하 감히 나의 정체를 묻다니', '딸: 말하지 않겠다면 말하게 만들어..', '딸의 말이 끝나기도 전에 사내가 딸을 기절 시킨다', '사내: 여기까지 온것은 용감했지만 나에게 도전하다니 어리석군'],
        ['딸 : 누구시죠, 누구길래 여기 있는거죠?', '사내: 나는 마왕이다. 지금 당장 이 사막을 떠나라 떠나지 않겠다면 널 죽이도록 하겠다', '딸 : 뭐래 내가 속을줄 알고? 내가 있는 오아시스가 탐나는거냐? 너야말로 떠나지 않겠다면 죽이겠다', '사내가 딸을 기절 시키고 밖으로 내보냈다'],
        ['딸: 하하, 저는 이제 목을 다 축여서 다시 모험을 떠나로 가겠습니다.', '사내: 쫄았군'],
        ['딸 : 마침 목말랐는데 감사합니다.']
    ]
    plus_stats8 = [['Tenacity'], ['Tenacity'], None, ['Intellect', 'Morality', 'Dignity', 'Stamina', 'MuscularStrength', 'Tenacity', 'Attractiveness']]
    minus_stats8 = [['Intellect', 'Morality', 'Dignity', 'Stamina', 'MuscularStrength'], ['Intellect', 'Morality', 'Dignity', 'Stamina', 'MuscularStrength'], ['Tenacity'], None]
    Princess.Choice(question8, option8, after_option8, plus_stats8, minus_stats8)

    Story.Scene9()
    question9 = "어두운 골목길에서 누군가 제안해 올 때 딸의 반응은?"
    option9 = ['상대의 수상한 덜미를 잡아채 관가로 끌고 간다.', '"바르지 못한 일입니다"라며 차갑게 돌아서 나온다.', '무서워서 아무 말도 못 하고 집으로 뛰어온다.', '상대가 내민 돈주머니의 무게를 슬쩍 달아본다.']
    after_option9 = [
        ['딸 : 가만히 있어요 아저씨 뭘 잘했다고 그래요?'],
        ['딸 : 이건 바르지 못하잖아요 아저씨 저 갈꺼에요.'],
        ['…', '딸 : 헉헉.. 무서웠어ㅠㅠ', '아빠 : 딸 무슨일이야?'],
        ['딸: 오 이정도면 괜찮은데요? 같이 해요', '수상한 인물 : 그러면 같이 저기 가자', '청년 : 지금 뭐하시는 거죠?']
    ]
    plus_stats9 = [['Intellect', 'Stamina', 'MuscularStrength', 'Morality', 'Dignity'], ['Intellect', 'Morality', 'Dignity', 'Attractiveness'], ['Stamina'], None]
    minus_stats9 = [None, None, None, ['Morality']]
    Princess.Choice(question9, option9, after_option9, plus_stats9, minus_stats9)

    Story.Scene10()
    question10 = "성에 방문하여 국왕을 접견할 때 딸의 시선은?"
    option10 = ['국왕을 호위하는 기사들의 무기와 자세를 유심히 살핀다.', '왕실의 예법에 맞춰 완벽하고 품위 있게 인사를 올린다.', '옆에 있는 하녀와 눈이 마주치자 반갑게 목인사를 한다.', '국왕이 앉은 왕좌와 반짝이는 왕관을 유심히 바라본다.']
    after_option10 = [
        ['국왕 : 우리 기사들의 무기와 자세를 유심히 보는것을 보니 검술에 관심히 있나 보구나. 우리 기사단장과 한번 결투 해보지 않겠나?', '딸: 그렇게 해주시면 감사하겠습니다.', '국왕 : 뭘 감사하기까지 그럼 전투장으로 따라오게'],
        ['국왕 : 예법을 제대로 준비해 왔구만 허허', '딸 : 감사합니다!'],
        ['국왕 : 방금 하녀한테 목인사를 한 것이냐?', '딸 : 네 아버지께서는 누구든지 공평하게 대하라 하셨죠!', '하녀(?) : 하하 요즘 하녀에게 인사하는 사람은 없던데 참된 인재구만', '왕비 : 하하 정말 잘 배웠군'],
        ['국왕 : 이 모자와 왕자가 탐나는가?', '딸 : 아닙니다. 그렇지 않습니다.', '국왕 : 괜찮다. 대신 실력으로 증명하라']
    ]
    plus_stats10 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Dignity', 'Attractiveness'], ['Dignity', 'Morality', 'Attractiveness'], ['Tenacity']]
    minus_stats10 = [None, None, None, None]
    Princess.Choice(question10, option10, after_option10, plus_stats10, minus_stats10)

    Story.Scene11()
    question11 = "주점에서 손님들 사이에 싸움이 났을 때 딸의 대처는?"
    option11 = ['싸움판 한가운데로 걸어가 소리를 지르며 난동꾼을 제압한다.', '상황을 냉정하게 파악한 뒤 경비병을 불러 정돈한다.', '따뜻한 음료와 안주를 챙겨 오며 손님들의 기분을 풀어준다.', '혼란스러운 틈을 타 탁자 위에 남겨진 동전들을 슬쩍한다.']
    after_option11 = [
        ['딸 : 여기서 싸우면서 피해주시지 마세요!!', '딸이 둘을 기절 시킨다', '사람들 : 젊은 아가씨가 대단하네'],
        ['딸 : 그만하세요 !!', '싸움이 끝나지 않는다', '딸 : 하… 내가 해선 안끝나겠네', '경비병을 부른다'],
        ['딸 : 손님들 죄송합니다. 잠시 소란이 있었습니다.', '딸 : 여기 서비스로 따뜻한 음료와 안주입니다. 다시한번 죄송합니다.', '손님들 : 여기 대처가 좋다'],
        ['지나가던 청년(?): 저기요 여기 직원 같은데 저기서 싸우고 있다고 몰래 돈을 훔쳐도 됩니까?', '딸 : 아 죄송합니다..', '지나가던 청년(?): 저한테 사과할게 아니라 손님들한테 사과하세요!']
    ]
    plus_stats11 = [['Dignity', 'Morality', 'Stamina', 'MuscularStrength'], ['Intellect'], ['Morality', 'Attractiveness'], None]
    minus_stats11 = [None, None, None, ['Dignity', 'Morality']]
    Princess.Choice(question11, option11, after_option11, plus_stats11, minus_stats11)

    Story.Scene12()
    question12 = "북부 빙원에서 아버지의 옛 정적과 마주쳤을 때 딸의 한마디는?"
    option12 = ['"아버지의 이름을 더럽히게 두지 않는다!"며 검을 뽑는다.', '상대의 약점을 냉철하게 분석하며 대치한다.', '차가운 기운에 눌려 일단 뒤로 후퇴한다.', '"나에게 관심이 있나요?"라며 여유롭게 미소를 띤다.']
    after_option12 = [
        ['딸: 덤벼라! 내가 이 악연을 끊겠다!', '옛 정적: 패기는 좋구나 실력도 좋은지 보겠다!', '비등비등한 싸움이였지만 마지막에 딸의 검이 옛 정적의 팔을 잘랐다', '옛 정적 : 크윽 강하구나 역시 그의 딸인가….'],
        ['딸: 덤벼라! 내가 이 악연을 끊겠다!', '옛 정적: 패기는 좋구나 실력도 좋은지 보겠다!', '딸은 옛 정적이 싸우는 방식을 보면서 대치했다', '딸 : 너의 약점은 여기다!!', '딸의 검은 그의 팔을 잘랐다', '옛 정적 : 내가 팔이 다친건 어떻게 알았냐', '딸 : 너가 한쪽 팔을 최대한 안쓰려고 하길래 여기가 약점인걸 알았다', '옛 정적 : 그를 닮아 전투센스까지 뛰어나군…'],
        ['옛 정적 : 도망가는거냐!!!', '옛 정적 : 너의 아버지도 이렇게 도망 갔지!!!', '딸 : 우리 아버지를 모욕하지 마라!!!', '딸은 옛 정적에게 달려 들었다', '딸은 멋지게 그의 팔을 잘랐다', '옛 정적 : 그와 다르게 잘 싸우는군….', '딸 : 우리 아버지를 모욕하지 말라 했지 않았냐!!! 너는 천천히 고통 받다 죽어라', '딸은 옛 정적에 두다리와 남은 팔 한쪽을 잘랐다'],
        ['옛 정적 : 당연히 관심이 있지 그의 딸은 얼마나 강할지 궁금하구나!!', '딸 : 그러면 보여주는 수 밖에 없군요', '딸은 일격에 그를 쓰려뜨렸다', '저희 아버지의 정적이니 살려는 드리겠습니다.']
    ]
    plus_stats12 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Stamina', 'MuscularStrength', 'Intellect'], ['Stamina', 'MuscularStrength'], ['Stamina', 'MuscularStrength']]
    minus_stats12 = [None, None, ['Dignity', 'Morality'], None]
    Princess.Choice(question12, option12, after_option12, plus_stats12, minus_stats12)

    Story.Scene13()
    question13 = "집사 큐브가 누웠을 때 딸이 한 행동은?"
    option13 = ['큐브가 하던 장작 패기와 무거운 짐 들기를 대신한다.', '의사를 불러오고 약의 효능을 체크하며 간호한다.', '정성껏 죽을 끓이고 이불을 덮어주며 밤을 새운다.', '"아픈 건 어쩔 수 없지" 하며 자기 방으로 들어가 버린다.']
    after_option13 = [
        ['딸: 아니야 누워있어, 너가 하던 일 내가 대신 할께', '큐브 : 감사합니다. 아가씨..', '딸은 큐브가 맨날 하던 일을 한다', '큐브가 이렇게 힘든 일을 했구나… 없으니깐 허전하다…', '딸은 큐브의 빈자리가 이렇게 컸었나 체감했다'],
        ['딸 : 의사 데려왔어 빨리 나아..', '큐브 : 감사합니다.. 쿨럭쿨럭'],
        ['딸 : 죽 끓여 왔어 먹어', '큐브 : 감사합니다 저를 위해 죽도 끓여 주시고', '딸 : 뭘 고마워해 이건 당연한거지 빨리 자', '큐브: 그럼 좀만 자겠습니다', '다음날 아침', '딸 : 일어났어??', '큐브 : 밤을 새운겁니까?', '딸 : 그럼 뭐 어떻게 해? 일어나면 도와줘야 하니깐..'],
        ['딸 : 안 옮으려면 어쩔 수 없지', '딸은 자기 방으로 들어가 버렸다']
    ]
    plus_stats13 = [['Stamina', 'MuscularStrength', 'Morality', 'Tenacity'], ['Morality', 'Attractiveness'], ['Morality', 'Dignity'], None]
    minus_stats13 = [None, None, None, ['Morality']]
    Princess.Choice(question13, option13, after_option13, plus_stats13, minus_stats13)

    Story.Scene14()
    question14 = "17세 마지막밤, 언덕에서 밤하늘을 바라볼 때 딸의 생각은?"
    option14 = ["더 강해져서 누구에게도 지지 않는 사람이 되고 싶어.", "언젠가 많은 사람을 이끄는 높고 훌륭한 자리에 서고 싶어.", "소박하더라도 내가 사랑하는 사람들과 평화롭게 살고 싶어.", "규율 같은 건 답답해, 세상이 내 발아래 있었으면 좋겠어."]
    after_option14 = [
        ['딸 : 난 더 강해져 누구보다 강해져 절대 지지 않아 내 가족들을 지킬꺼야'],
        ['딸 : 난 언젠가 많은 사람들을 이끌고 더 높은 자리에 서 내 가족들에게 인정 받을 거야'],
        ['딸 : 난 소박하더라도 내가 사랑받는 가족들과 함께 평화롭게 지낼꺼야'],
        ['딸 : 난 규율 같은건 답답해, 세상을 내 발 믿에 두고 모든 규율을 무시할꺼야']
    ]
    plus_stats14 = [['Stamina', 'MuscularStrength', 'Tenacity'], ['Intellect', 'Dignity'], ['Morality', 'Tenacity', 'Attractiveness'], ['Attractiveness']]
    minus_stats14 = [None, None, None, ['Morality', 'Dignity']]
    Princess.Choice(question14, option14, after_option14, plus_stats14, minus_stats14)

    Princess.Ending_Choice()

main()