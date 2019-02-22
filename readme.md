# Mais

[![Code Climate](https://codeclimate.com/github/matt-bernhardt/mais/badges/gpa.svg)](https://codeclimate.com/github/matt-bernhardt/mais)

Mais is a Python project to build a Monte Carlo simulation tool for Major
League Soccer.

## Requirements

Mais is being developed using Python 3.6, but the goal is for it to be useful
on any 3.x release. If push comes to shove I'll give preference to newer
releases.

It also assumes that you have a MySQL database available, whose schema can
probably be inferred by looking at the queries it issues. This is the same
database used by Trapp.

## Installation

My hope is that this tool gets installed in the usual fashion for Python
packages. However, I confess that I'm not a full-time Python developer so I
might have gotten something wrong. File an issue if that's the case.

## Usage

The simplest way to run the tool is just to invoke it:

```
> mais
```

There are options and arguments available to alter the following parameters:

* **mode** - can be one of two values. `single` runs one batch of simulations,
starting from the current date and through the rest of the season. `each` will
run a batch of simulations for every date on which games have been played in
the current season.
* **competition** - for now this tool is specific to Major League Soccer.
Future work will hopefully add the lower divisions, but that isn't a firm
roadmap.
* **model** - will switch between two different prediction models. Details
coming here.
* **batch** - will change how many simulation runs are included in each batch.
The default will be 10,000 runs per batch.
* **season** - gives the ability to simulate past seasons, at least going back
to 2011.

## About the name

[Brian Maisonneuve](https://en.wikipedia.org/wiki/Brian_Maisonneuve) - nicknamed "Mais" - played midfield for the Columbus Crew
and US National team from 1996 through 2004. He was a member of the 1998 US
World Cup team, appearing in all three games.

During his playing career, Mais developed a reputation as a player with great
awareness of the field, and was able to anticipate plays with an uncanny
regularity. This skillset makes him a suitable inspiration for a tool that
attempts to predict soccer games.
