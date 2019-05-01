#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module

# imports for system and OS access, directories
import os
import sys

# imports based on THIS file
moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(shareddir)
from BotShared import *






"""
This saves all of the botdict after the bot monologue
"""


@module.event('001')
@module.rule('.*')
@module.thread(True)
def bot_startup_monologue(bot, trigger):

    if bot_startup_requirements_met(bot, ["savedict"]):
        return

    # don't run jobs if not ready
    while not bot_startup_requirements_met(bot, ["monologue"]):
        pass

    botdict_save(bot)

    bot_startup_requirements_set(bot, "savedict")
