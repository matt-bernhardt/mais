# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import date


class Settings():

    def __init__(self, mode, competition, model, batch, season, start):
        self.values = {}
        self.values['mode'] = mode
        self.values['competition'] = competition
        self.values['model'] = model
        self.values['batch'] = batch
        self.values['season'] = season
        self.values['start'] = date(
            year=season,
            month=int(date.strftime(start, '%m')),
            day=int(date.strftime(start, '%d'))
        )

    def output(self):
        output = '=============================================\n'
        output += 'Competition: ' + str(self.values['competition']) + '\n'
        output += 'Season:      ' + str(self.values['season']) + '\n'
        output += 'Start:       ' + str(self.values['start']) + '\n'
        output += 'Mode:        ' + str(self.values['mode']) + '\n'
        output += 'Batch size:  ' + str(self.values['batch']) + '\n'
        output += 'Model:       ' + str(self.values['model']) + '\n'
        output += '=============================================\n'
        return output
