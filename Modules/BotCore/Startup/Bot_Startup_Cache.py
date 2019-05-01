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
This reads the external config for gif api
"""


@module.event('001')
@module.rule('.*')
@module.thread(True)
def bot_startup_twitter(bot, trigger):

    if bot_startup_requirements_met(bot, ["cache"]):
        return

    # don't run jobs if not ready
    while not bot_startup_requirements_met(bot, ["ext_conf"]):
        pass

    bot.memory["botdict"]["tempvals"]['cache'] = dict()

    bot_startup_requirements_set(bot, "cache")
