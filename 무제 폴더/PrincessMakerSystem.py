import pandas as pd
import numpy as np
import seaborn as sns
import random as rd
import time

class PrincessMaker:
  def __init__(self, file_name):
    self.file_name = file_name
    self.Stats = {'Stamina' : 0, 'MuscularStrength' : 0,
                  'Intellect' : 0, 'Dignity' : 0,
                  'Tenacity' : 0, 'Attractiveness' : 0,
                  'Morality' : 0}
    
  def View_Stats(self):
      print('=' * 100)
      print('캐릭터 능력치')
      print(f'체력 : {self.Stats["Stamina"]}')
      print(f'근력 : {self.Stats["MuscularStrength"]}')
      print(f'지력 : {self.Stats["Intellect"]}')
      print(f'기품 : {self.Stats["Dignity"]}')
      print(f'근성 : {self.Stats["Tenacity"]}')
      print(f'매력 : {self.Stats["Attractiveness"]}')
      print(f'도덕성 : {self.Stats["Morality"]}')
      print('=' * 100)

  def Save_Stats(self):
    Stats = pd.DataFrame({'체력' : [self.Stats['Stamina']], '근력' : [self.Stats['MuscularStrength']],
                          '지력' : [self.Stats['Intellect']], '기품' : [self.Stats['Dignity']],
                          '근성' : [self.Stats['Tenacity']], '매력' : [self.Stats['Attractiveness']],
                          '도덕성' : [self.Stats['Morality']]})
    Stats.to_csv(self.file_name, index = False)

  def Plus_Stats(self, Stats):
    if Stats:  
        for i in Stats:
            self.Stats[i] += rd.randint(20,30)
    return None

  def Minus_Stats(self, Stats):
    if Stats:  
        for i in Stats:
            self.Stats[i] -= rd.randint(20,30)
    return None

  def Choice(self, Question, Option, After_Option, Plus_Stats, Minus_Stats):
    print('=' *100)
    print(Question)
    print(f'1. {Option[0]}')
    print(f'2. {Option[1]}')
    print(f'3. {Option[2]}')
    print(f'4. {Option[3]}')
    print('=' *100)
    while True:
      answer = input('선택 : ')
      if answer == '1':
        for i in After_Option[0]:
          self.speak(i,2)
        self.Plus_Stats(Plus_Stats[0])
        self.Minus_Stats(Minus_Stats[0])
        self.Save_Stats()
        self.View_Stats()
        return None
      elif answer =='2':
        for i in After_Option[1]:
                  self.speak(i,2)
        self.Plus_Stats(Plus_Stats[1])
        self.Minus_Stats(Minus_Stats[1])
        self.Save_Stats()
        self.View_Stats()
        return None
      elif answer == '3':
        for i in After_Option[2]:
                  self.speak(i,2)
        self.Plus_Stats(Plus_Stats[2])
        self.Minus_Stats(Minus_Stats[2])
        self.Save_Stats()
        self.View_Stats()
        return None
      elif answer == '4':
        for i in After_Option[3]:
                  self.speak(i,2)
        self.Plus_Stats(Plus_Stats[3])
        self.Minus_Stats(Minus_Stats[3])
        self.Save_Stats()
        self.View_Stats()
        return None
      else:
        print('잘못된 선택지 입니다.')
        continue

  def Ending1(self):
    up_100 = []
    for i,j in self.Stats.items():
      if j >= 100:
        up_100.append(i)
    if 'Intellect' in up_100 and 'Dignity' in up_100 and 'Attractiveness' in up_100 and 'Morality' in up_100:
      return True
    else:
      return False

  def Ending2(self):
    down_40 = []
    for i,j in self.Stats.items():
      if j <= 40:
        down_40.append(i)
    if 'Intellect' in down_40 and 'Dignity' in down_40 and 'Attractiveness' in down_40 and 'Morality' in down_40:
      return True
    else:
      return False

  def Ending3(self):
    up_100 = []
    for i,j in self.Stats.items():
      if j >= 100:
        up_100.append(i)
    if 'Stamina' in up_100 and 'MuscularStrength' in up_100 and 'Tenacity' in up_100:
      return True
    else:
      return False

  def Ending4(self):
    up_100 = []
    for i,j in self.Stats.items():
      if j >= 100:
        up_100.append(i)
    if 'Morality' in up_100 and 'Stamina' in up_100:
      return True
    else:
      return False

  def Ending5(self):
    up_100 = []
    down_40 = []
    for i,j in self.Stats.items():
      if j <= 40:
        down_40.append(j)
    if 'Morality' in down_40:
      return True
    else:
      return False

  def speak(self, say,wait):
    print(say)
    time.sleep(wait)

  def LegendaryGreatGeneral(self):
    self.speak("18세가 되던 해, 딸은 왕국 기사단 시험을 수석으로 통과하고 수많은 전장에서 승리를 이끌어 왕국 역사상 최초의 '대장군' 자리에 오릅니다.", 6)
    self.speak('거대한 갑옷과 검을 차고 수천 기병을 이끄는 위풍당당한 장군이 되었지만,',3)
    self.speak('퇴근 후 집에 돌아오면 갑옷을 훌훌 벗어 던지고 "아버지! 오늘 훈련 너무 힘들었어요, 밥 주세요!"하며 투정을 부리는 든든한 딸로 남습니다.',6)

  def LegendaryQueen(self):
    self.speak("지혜와 예법, 사교성을 겸비한 딸은 왕실의 높은 신망을 받아 국왕의 뒤를 잇는 최고 통치자 '여왕'의 왕관을 쓰게 됩니다.",5)
    self.speak('국정 연설장에서는 범접할 수 없는 품위와 완벽함으로 백성들을 매료시키지만,',3)
    self.speak(' 매년 아버지의 생일이 되면 아버지만을 위한 비밀 연회를 열고 "제가 세상을 통치할 수 있는 건 모두 아버지 덕분이에요"라며 왕관을 내려놓고 고개 숙여 감사 인사를 올립니다.',7)

  def Thelegendaryinnclerk(self):
      self.speak("화려한 명예나 권력 대신 소박한 행복을 택한 딸은 마을에서 가장 따뜻하고 인기 있는 여관의 정식 점원이 됩니다.",4)
      self.speak("특유의 싹싹함과 정성 어린 요리 솜씨로 마을 사람들과 여행자들에게 큰 사랑을 받으며,",3)
      self.speak('퇴근 후 아버지와 함께 소소한 저녁 식사를 나누며 "오늘도 보람찬 하루였어요, 아빠!"라고 웃어 보이는 따뜻하고 평화로운 일상을 이어갑니다.',5)

  def LegendaryThief(self):
      self.speak("아버지의 훈육을 거부하고 어둠에 빠져든 딸은 왕국 전역을 공포에 떨게 만드는 도적단의 두목이 되어 수배령이 내려집니다.",5)
      self.speak('아버지가 밤마다 딸을 걱정하며 눈물지을 때, 늦은 밤 창문 너머로 훔친 보석 자루가 툭 던져집니다.',4)
      self.speak('딸은 미안함과 죄책감에 차마 얼굴을 비추지 못한 채 씁쓸한 미소를 지으며 어둠 속으로 사라져 갑니다.',4)

  def TheLegendaryDemonQueen(self):
      self.speak("치명적인 매력과 거대한 마력을 갖추게 된 딸은 아버지가 목숨 걸고 싸웠던 원수인 '마왕'의 구혼을 받아들여 마계의 여왕(마왕비)이 됩니다.",5)
      self.speak("마왕조차 딸의 카리스마에 쩔쩔매며 완벽하게 쥐락락당하게 되고, 장인어른이 된 용사 앞에 선 마왕은 식은땀을 흘립니다.",4)
      self.speak('딸은 마계의 희귀한 보석을 선물하며 "아버지, 예전에 아빠 괴롭혔던 마왕 녀석 제가 확실하게 정신 차리게 해줬어요!"라며 능글맞게 웃어 보입니다.',6)

  def knitters(self):
    self.speak('다른 아이들은 저마다 자신의 길을 찾아 세상으로 나아갈 나이가 되었지만, 딸의 방 문은 조용하기만 합니다.',4)
    self.speak('딸: "아빠! 용사 시절에 벌어둔 돈 많잖아요~ 세상은 아빠가 구했으니까, 전 아빠 곁을 지키며 이 평화를 마음껏 누릴게요! 오늘 점심은 뭐예요?"',5)
    self.speak('용사인 아버지가 문을 열고 들어가 보자, 딸은 푹신한 이불 속에서 뒹굴거리며 과자 봉지를 조물딱거리다 멋쩍게 웃어 보입니다.',5)
    self.speak('딸: "어, 아빠... 벌써 아침이에요? 오늘 날씨 진짜 좋다~ 이런 날은 집에서 푹 쉬어야 하는데 말이죠."',4)
    self.speak('큐브: "주인님... 아가씨께서 검술도, 학문도, 요리도, 심지어 나쁜 짓(?)을 할 의욕조차 없이 자라버리셨습니다..."',4)
    self.speak('딸은 용사 아버지가 그동안 몬스터를 잡고 모아둔 전통 있는 퇴직금과 연금의 존재를 깨달아 버린 것이었습니다!',4)
    self.speak('세상을 구한 용사의 집이라는 세상에서 가장 안전하고 따뜻한 둥지에서, 딸은 "우주 제일의 집순이"가 되기로 결심합니다.',4)
    self.speak('하루 종일 만화책을 보고 주전부리를 털어먹으며 빈둥거리지만, 아버지에게 애교 하나만큼은 끝내주게 떨어댑니다.',4)

  def Ending_Choice(self):
    if self.Ending1():
      self.LegendaryQueen()
    elif self.Ending2():
      self.TheLegendaryDemonQueen()
    elif self.Ending3():
      self.LegendaryGreatGeneral()
    elif self.Ending4():
      self.Thelegendaryinnclerk()
    elif self.Ending5():
      self.LegendaryThief()
    else:
      self.knitters()