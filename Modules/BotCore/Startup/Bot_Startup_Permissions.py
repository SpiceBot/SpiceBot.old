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
This runs at startup to ensure the permissions of the bot directory are available to the bot user
"""


@module.event('001')
@module.rule('.*')
@module.thread(True)
def bot_startup_permissions(bot, trigger):

    if bot_startup_requirements_met(bot, ["permissions"]):
        return

    # os.system("sudo chown -R " + str(os_dict["user"]) + ":sudo /home/spicebot/.sopel/" + str(bot.nick) + "/")

    bot_startup_requirements_set(bot, "permissions")
