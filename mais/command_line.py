# -*- coding: utf-8 -*-
from __future__ import absolute_import
import click

@click.command()
@click.option('--batch', '-b', default=1, help='How many seasons should be simulated in a batch?')
@click.argument('mode', type=click.Choice(['single','each']), default='single')

def main(batch, mode):
	click.echo('Operating in \'' + mode + '\' mode')
	click.echo('Batch size: ' + str(batch))
