class Login:
    def __init__(self, my_id, my_name, daughter_name, password, stats=None, current_scene=1):
        self.my_id = my_id
        self.my_name = my_name
        self.daughter_name = daughter_name
        self.password = password
        self.current_scene = int(current_scene)  # 현재 진행 중인 Scene 번호 (기본값 1)
        
        if stats is None:
            self.stats = {
                'Stamina': 0,
                'MuscularStrength': 0,
                'Intellect': 0,
                'Dignity': 0,
                'Tenacity': 0,
                'Attractiveness': 0,
                'Morality': 0
            }
        else:
            self.stats = stats