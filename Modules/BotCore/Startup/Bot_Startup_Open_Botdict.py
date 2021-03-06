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
At bot startup, open botdict
"""


@module.event('001')
@module.rule('.*')
@module.thread(True)
def bot_startup_botdict_open(bot, trigger):

    if bot_startup_requirements_met(bot, ["botdict"]):
        return

    # don't run jobs if not ready
    while not bot_startup_requirements_met(bot, ["connected"]):
        pass

    # Open Botdict
    botdict_setup_open(bot)

    # Tempvals section
    bot.memory["botdict"]["tempvals"] = dict()
    bot.memory["botdict"]["tempvals"]["uservals"] = dict()

    bot_startup_requirements_set(bot, "botdict")
