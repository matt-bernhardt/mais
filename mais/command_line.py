# -*- coding: utf-8 -*-
from __future__ import absolute_import
import click

@click.command()
@click.argument('mode', type=click.Choice(['single','each']), default='single')
@click.argument('competition', type=click.Choice(['mls']), default='mls')
@click.option('--model', '-m', type=click.Choice(['v1','v2']), default='v2', help='Which prediction model should be used?')
@click.option('--batch', '-b', default=5, help='How many seasons should be simulated in a batch?')

def main(batch, mode, competition, model):
	# Reflect back the configuration being used
	click.echo('Competition: ' + competition)
	click.echo('Mode:        ' + mode)
	click.echo('Batch size:  ' + str(batch))
	click.echo('Using model: ' + model)

	# Initialize

	# Run simulations

	# Output data

	# Visualize?
