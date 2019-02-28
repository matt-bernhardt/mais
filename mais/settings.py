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
        output =  '=============================================\n'
        output += 'Competition: ' + str(self.values['competition']) + '\n'
        output += 'Season:      ' + str(self.values['season']) + '\n'
        output += 'Mode:        ' + str(self.values['mode']) + '\n'
        output += 'Batch size:  ' + str(self.values['batch']) + '\n'
        output += 'Model:       ' + str(self.values['model']) + '\n'
        output += '=============================================\n'
        return output
