# this is the generic class, all four classes will adopt from this class but have some skills and stats rolled for it

import numpy as np
import random


class GenClass:
    def __init__(self):
        self._name = ""
        self._prof = ""  # this is the profession or class
        self._max_health = 0  # this is the total health, it will not change
        self._health = 0  # this is current health, it is mutable
        self._race = ""
        self._dmg_type = 0
        self._skill_list = []
        self._stats = []

    def get_name(self):
        return self._name

    def get_prof(self):
        return self._prof

    def get_max_health(self):
        return self._max_health

    def get_health(self):
        return self._health

    def get_race(self):
        return self._race

    def get_dmg_type(self):
        return self._dmg_type

    def get_skill_list(self):
        return self._skill_list

    def get_stats(self):
        return self._stats

    def set_name(self, name):
        self._name = name
        return self._name

    def reset_health(self):
        self._health = self._max_health  # there has to be a better way to do this, I'm trying to make the current
        return self._health  # health the max health, or reset to the max health

    @staticmethod
    def set_stats(self, pwr, dfs, res, dodge, crit):
        self._stats = [pwr, dfs, res, dodge, crit]
        return self._stats

    def add_stat_pts(self, pwr, dfs, res, dodge, crit):
        return np.add(self._stats,
                      [pwr, dfs, res, dodge, crit])  # this is not in use, could be used for level up system

    @staticmethod
    def set_skills(self, attack, heal, dodge):
        self._skill_list = [attack, heal, dodge]  # currently this is not in use, I'm leaving it alone for now
        return self._skill_list  # but this might not be the best way to do this

    def dodge(self):
        dodge_chance = random.random() * 100
        if dodge_chance <= (self.get_stats()[3]):
            return ["Dodge"]

    def attack(self):
        crit_chance = random.random() * 100
        crit = ""
        dmg = self.get_stats()[0] + random.randint(-2, 2)
        if crit_chance <= (self.get_stats()[4] / 1.2):
            dmg = dmg * 2
            crit = "Crit"
        return [dmg, crit]

    def take_damage(self, dmg, attack_type):
        damage_taken = 0
        if attack_type == 0:
            if dmg[0] > self.get_stats()[1]:
                damage_taken = dmg[0] - self.get_stats()[1]
                self._health -= damage_taken
            else:
                damage_taken = 0
        elif attack_type == 1:
            if dmg[0] > self.get_stats()[2]:
                damage_taken = dmg[0] - self.get_stats()[2]
                self._health -= damage_taken
            else:
                damage_taken = 0
        if self._health <= 0:
            life_status = "Dead"
            chance = random.random() * 100
            if chance >= 90:
                print("You live by a miracle.")
                self._health = int((random.random()) * (self.get_max_health() / 4))
                life_status = "Alive"
                return [life_status, damage_taken]
            else:
                return [life_status, damage_taken]
        else:
            life_status = "Alive"
            return [life_status, damage_taken]

    def heal(self, health_pts):
        self._health += health_pts
        if self._health > self._max_health:
            self.reset_health()
        return self._health


class Assassin(GenClass):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._prof = "Assassin"
        self._max_health = 200
        self._health = 200
        self._race = ""
        self._dmg_type = 0  # 0 is physical, 1 is magical
        self._stats = self.set_stats(self, 30, 10, 5, 25, 10)  # power, defense, resistance, dodge, crit chance


class Mystic(GenClass):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._prof = "Mystic"
        self._max_health = 200
        self._health = 200
        self._race = ""  # this feature has not been implemented
        self._dmg_type = 1  # 0 is physical, 1 is magical
        self._stats = self.set_stats(self, 35, 5, 15, 10, 15)  # power, defense, resistance, dodge, crit chance


class Knight(GenClass):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._prof = "Knight"
        self._max_health = 350
        self._health = 350
        self._race = ""  # this feature has not been implemented
        self._dmg_type = 0  # 0 is physical, 1 is magical
        self._stats = self.set_stats(self, 25, 20, 5, 5, 10)  # power, defense, resistance, dodge, crit chance


class Elementalist(GenClass):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._prof = "Elementalist"
        self._max_health = 350
        self._health = 350
        self._race = ""  # this feature has not been implemented
        self._dmg_type = 1  # 0 is physical, 1 is magical
        self._stats = self.set_stats(self, 35, 5, 15, 5, 5)  # power, defense, resistance, dodge, crit chance
