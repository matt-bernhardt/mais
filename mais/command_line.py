# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import date
import click


@click.command()
@click.argument('mode', type=click.Choice(['single', 'each']),
                default='single')
@click.argument('competition', type=click.Choice(['mls']), default='mls')
@click.option('--model', '-m', type=click.Choice(['v1', 'v2']), default='v2',
              help='Which prediction model should be used?')
@click.option('--batch', '-b', default=5,
              help='How many seasons should be simulated in a batch?')
@click.option('--season', '-s', type=click.IntRange(2011, date.today().year),
              default=date.today().year,
              help='What season should be simulated? (2011-present)')
@click.version_option(message='%(version)s')
def main(mode, competition, model, batch, season):
    # Reflect back the configuration being used
    click.echo('Competition: ' + competition)
    click.echo('Season:      ' + str(season))
    click.echo('Mode:        ' + mode)
    click.echo('Batch size:  ' + str(batch))
    click.echo('Using model: ' + model)

    # Initialize

    # Run simulations

    # Output data

    # Visualize?
