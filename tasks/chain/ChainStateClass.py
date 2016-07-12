# Python libs. 
import sys
import os

# Local libs.
from mdp.StateClass import State

class ChainState(State):
	''' Class for Chain MDP States '''

	def __init__(self, num):
		self.num = num

	def __hash__(self):
		return self.num

	def __add__(self, val):
		return ChainState(self.num + val)

	def __lt__(self, val):
		if self.num < val:
			return True
		else:
			return False

	def __str__(self):
		return "s." + str(self.num)

	def __eq__(self, other):
		'''
		Summary:
			Chain states are equal when their num is the same
		'''
		if isinstance(other, ChainState) and self.num == other.num:
			return True
		else:
			return False