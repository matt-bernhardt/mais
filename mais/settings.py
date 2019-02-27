# -*- coding: utf-8 -*-
from __future__ import absolute_import


class Settings():

	def __init__(self, mode, competition, model, batch, season):
		self.values = {}
		self.values['mode'] = mode
		self.values['competition'] = competition
		self.values['model'] = model
		self.values['batch'] = batch
		self.values['season'] = season

	def output(self):
		print('=============================================')
		print('Competition: ' + str(self.values['competition']))
		print('Season:      ' + str(self.values['season']))
		print('Mode:        ' + str(self.values['mode']))
		print('Batch size:  ' + str(self.values['batch']))
		print('Model:       ' + str(self.values['model']))
		print('=============================================')
		print('')
