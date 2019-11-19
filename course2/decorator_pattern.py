from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
	def __init__(self, base):
		self.base = base
		self.get_stats()
		
	@abstractmethod
	def get_negative_effects(self):
		pass
		
	@abstractmethod	
	def get_positive_effects(self):
		pass
		
	def get_stats(self):
		self.get_positive_effects()
		self.get_negative_effects()
		return self.stats.copy()
		
		
class AbstractPositive(AbstractEffect, ABC):
	@abstractmethod
	def get_positive_effects(self):
		return self.positive_effects.copy()
	
	def get_negative_effects(self):
		self.negative_effects = self.base.get_negative_effects()
		return self.negative_effects.copy()
		
		
class AbstractNegative(AbstractEffect, ABC):
	@abstractmethod
	def get_negative_effects(self):
		return self.negative_effects.copy()
	
	def get_positive_effects(self):
		self.positive_effects = self.base.get_positive_effects()
		return self.positive_effects.copy()
	
class Berserk(AbstractPositive):
	def get_positive_effects(self):
		self.stats = self.base.get_stats()
		self.positive_effects = self.base.get_positive_effects() + ['Berserk']
		self.stats['HP'] += 50
		for i in ['Strength', 'Endurance', 'Agility', 'Luck']:
			self.stats[i] += 7
		for i in ['Intelligence', 'Charisma', 'Perception']:
			self.stats[i] -= 3
		return self.positive_effects.copy()
		
	
class Blessing(AbstractPositive):
	def get_positive_effects(self):
		self.stats = self.base.get_stats()
		base_stats = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
		self.positive_effects = self.base.get_positive_effects() + ['Blessing']
		for i in base_stats:
			self.stats[i] += 2
		
		return self.positive_effects.copy()
	
	
class Curse(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.get_stats()
		base_stats = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
		self.negative_effects = self.base.get_negative_effects() + ['Curse']
		for i in base_stats:
			self.stats[i] -= 2
		
		return self.negative_effects.copy()

	
class Weakness(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.get_stats()
		self.negative_effects = self.base.get_negative_effects() + ['Weakness']
		for i in ['Strength', 'Agility', 'Endurance']:
			self.stats[i] -= 4
		
		return self.negative_effects.copy()

		
class EvilEye(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.get_stats()
		self.negative_effects = self.base.get_negative_effects() + ['EvilEye']
		self.stats['Luck'] -= 10
		return self.negative_effects.copy()