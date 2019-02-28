# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import date
import click
from mais.database import Database
from mais.log import Log
from mais.league import League
from mais.settings import Settings


def check_db(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('=============================================')
    click.echo('Checking database connection...')
    # Load the connection details
    db = Database()
    connection = db.loadConnection()
    click.echo('Credentials:')
    click.echo('dbuser:   ' + str(connection['dbuser']))
    click.echo('dbpwd:    ' + str(connection['dbpwd']))
    click.echo('dbhost:   ' + str(connection['dbhost']))
    click.echo('dbschema: ' + str(connection['dbschema']))
    # Try to establish the connection
    db.connect()
    # print result
    click.echo(str(db.cnx))
    click.echo(str(db.cursor))
    click.echo('Warnings: ' + str(db.warnings()))
    ctx.exit()


@click.command()
@click.argument('mode', type=click.Choice(['single', 'each']),
                default='single')
@click.argument('competition', type=click.Choice(['mls']), default='mls')
@click.option('--check-db', is_flag=True, callback=check_db, is_eager=True,
              expose_value=False, help='Check database connection')
@click.option('--model', '-m', type=click.Choice(['v1', 'v2']), default='v2',
              help='Which prediction model should be used?')
@click.option('--batch', '-b', default=5,
              help='How many seasons should be simulated in a batch?')
@click.option('--season', '-s', type=click.IntRange(2011, date.today().year),
              default=date.today().year,
              help='What season should be simulated? (2011-present)')
@click.version_option(message='%(version)s')
def main(mode, competition, model, batch, season):
    settings = Settings(mode, competition, model, batch, season)

    # Reflect back the configuration being used
    click.echo(settings.output())

    # Initialize tooling
    click.echo('Initializing tooling...')
    datestamp = date.today().strftime("%y%m%d")
    log = Log('mais-' + datestamp + '-' + mode + '-' + model + '.log')
    log.message('Started')
    db = Database()
    db.connect()
    log.message('Database connected')

    # Initialize data
    click.echo('Initializing data...')
    league = League()
    league.connectDB()
    league.lookupTeamsBySeason(1996, 'mls', log)
    for item in league.teams:
        click.echo(str(item))
    click.echo('=============================================')
    click.echo('')

    # Teardown
    click.echo('Finishing...')
    db.disconnect()
    log.message('Database disconnected')
    log.end()
