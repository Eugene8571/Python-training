class Warrior:
    """Warrior"""
    def __init__(self):
        self.experience = 100
        self.level = 1
        self.rank = 'Pushover'
        self.achievements = []

    def training(self, A):
        if self.level < A[2]:
            return 'Not strong enough'
        #if A[1] > 0 and self.level <= 100:
        self.achievements.append(A[0])
        plus_exp = A[1]
        self.update(plus_exp)
        return A[0]


    def battle(self, enemy_lvl):
        if enemy_lvl < 1 or enemy_lvl > 100:
            return 'Invalid level'
        respons = self.respons(enemy_lvl)    
        plus_exp = self.exp_calculator(enemy_lvl)
        self.update(plus_exp)
        return respons


    def update(self, plus_exp):
        self.experience += plus_exp
        if self.experience > 10000:
            self.experience = 10000
        self.level = self.experience // 100
        all_ranks = ["Pushover", "Novice", "Fighter", "Warrior", \
        "Veteran", "Sage", "Elite", "Conqueror", "Champion", \
        "Master", "Greatest"]
        self.rank = all_ranks[self.level // 10]


    def exp_calculator(self, enemy_lvl):
        lvl_diff = self.level - enemy_lvl
        if lvl_diff >= 2:
            return 0
        if lvl_diff == 1:
            return 5
        if self.level == enemy_lvl:
            return 10
        if self.level // 10 < enemy_lvl // 10 and lvl_diff <= -5:
            return 0
        if self.level < enemy_lvl:
            return 20 * lvl_diff * lvl_diff
        else:
            return 0
            
            
    def respons(self, enemy_lvl):
        lvl_diff = self.level - enemy_lvl
        if lvl_diff <= -5 and self.level//10 < enemy_lvl // 10:
            return "You've been defeated"
        if lvl_diff < 0:
            return "An intense fight"
        if lvl_diff in (0, 1):
            return "A good fight"
        if lvl_diff > 1:
            return "Easy fight"
        

        
Chack_Norris = Warrior()
print(Chack_Norris.level, Chack_Norris.experience, \
    Chack_Norris.rank, Chack_Norris.achievements)
print(Chack_Norris.training(['10 push-ups', 0, 1]))
print(Chack_Norris.level, Chack_Norris.experience, \
    Chack_Norris.rank, Chack_Norris.achievements)



print(Chack_Norris.battle(3))
#print(Chack_Norris.training(["Defeated Chuck Norris", 9000, 1]))
print(Chack_Norris.level, Chack_Norris.experience, \
    Chack_Norris.rank, Chack_Norris.achievements)
print(Chack_Norris.battle(1))
print(Chack_Norris.level, Chack_Norris.experience, \
    Chack_Norris.rank, Chack_Norris.achievements)

        
bruce_lee = Warrior()
print(bruce_lee.experience)
print(bruce_lee.level)
print(bruce_lee.training(['Chack', 9000, 1]))
print(bruce_lee.experience)
print(bruce_lee.level)
print(bruce_lee.rank)

'''
bruce_lee = Warrior()
Test.assert_equals(bruce_lee.level, 1)
Test.assert_equals(bruce_lee.experience, 100)
Test.assert_equals(bruce_lee.rank, "Pushover")
Test.assert_equals(bruce_lee.achievements, [])
Test.assert_equals(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
Test.assert_equals(bruce_lee.experience, 9100)
Test.assert_equals(bruce_lee.level, 91)
Test.assert_equals(bruce_lee.rank, "Master")
Test.assert_equals(bruce_lee.battle(90), "A good fight")
Test.assert_equals(bruce_lee.experience, 9105)
Test.assert_equals(bruce_lee.achievements, ["Defeated Chuck Norris"])
'''

