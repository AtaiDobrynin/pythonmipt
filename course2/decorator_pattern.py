from abc import ABC, abstractmethod


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
		self.negative_effects = self.base.negative_effects.copy()
		return self.negative_effects.copy()
		
		
class AbstractNegative(AbstractEffect, ABC):
	@abstractmethod
	def get_negative_effects(self):
		return self.negative_effects.copy()
	
	def get_positive_effects(self):
		self.positive_effects = self.base.positive_effects.copy()
		return self.positive_effects.copy()
	
class Berserk(AbstractPositive):
	def get_positive_effects(self):
		self.stats = self.base.stats.copy()
		self.positive_effects = self.base.positive_effects + ['Berserk']
		self.stats['HP'] += 50
		for i in ['Strength', 'Endurance', 'Agility', 'Luck']:
			self.stats[i] += 7
		for i in ['Intelligence', 'Charisma', 'Perception']:
			self.stats[i] -= 3
		return self.positive_effects.copy()
		
	
class Blessing(AbstractPositive):
	def get_positive_effects(self):
		self.stats = self.base.stats.copy()
		base_stats = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
		self.positive_effects = self.base.positive_effects + ['Blessing']
		for i in base_stats:
			self.stats[i] += 2
		
		return self.positive_effects.copy()
	
	
class Curse(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.stats.copy()
		base_stats = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
		self.negative_effects = self.base.negative_effects + ['Curse']
		for i in base_stats:
			self.stats[i] -= 2
		
		return self.negative_effects.copy()

	
class Weakness(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.stats.copy()
		self.negative_effects = self.base.negative_effects + ['Weakness']
		for i in ['Strength', 'Agility', 'Endurance']:
			self.stats[i] -= 4
		
		return self.negative_effects.copy()

		
class EvilEye(AbstractNegative):
	def get_negative_effects(self):
		self.stats = self.base.stats.copy()
		self.negative_effects = self.base.negative_effects + ['EvilEye']
		self.stats['Luck'] -= 10
		return self.negative_effects.copy()