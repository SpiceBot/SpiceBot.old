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






comdict = {
            "author": "deathbybandaid",
            "contributors": [],
            "description": "",
            'privs': [],
            "example": "",
            "exampleresponse": "",
            }


@module.rule(r'(?i)(Damnit|Lazy)? $nickname[ \t]*$')
@module.thread(True)
def bot_command_hub(bot, trigger):

    botcom = botcom_nick(bot, trigger)

    # Bots block
    if bot_check_inlist(bot, botcom.instigator, [bot.nick]):
        return

    # does not apply to bots
    if "altbots" in bot.memory:
        if bot_check_inlist(bot, botcom.instigator, bot.memory["altbots"].keys()):
            return

    osd(bot, botcom.channel_current, 'say', "I do not tell you how to do your job, " + botcom.instigator + "!!!")
