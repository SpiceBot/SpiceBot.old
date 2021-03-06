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
            'privs': ['admin', 'OP'],
            "example": "",
            "exampleresponse": "",
            }


"""
This allows the viewing of systemd logs from within IRC
"""


@module.nickname_commands('debug')
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

    if not bot_permissions_check(bot, botcom):
        return osd(bot, botcom.instigator, 'notice', "I was unable to process this Bot Nick command due to privilege issues.")

    osd(bot, botcom.channel_current, 'action', "Is Examining systemd Log(s).")

    servicepid = str(os.popen("systemctl show " + str(bot.nick) + " --property=MainPID").read()).split("=")[-1]
    debuglines = []
    for line in os.popen(str("sudo journalctl _PID=" + str(servicepid))).read().split('\n'):
        if not str(line).startswith("-- Logs begin at"):
            line = str(line).split(str(os.uname()[1] + " "))[-1]
            if not str(line).startswith("sudo"):
                lineparts = str(line).split(": ")
                del lineparts[0]
                line = spicemanip.main(lineparts, 0)
                debuglines.append(str(line))
        else:
            debuglines.append(str(line))

    if len(debuglines) == 0:
        return osd(bot, botcom.channel_current, 'say', str(bot.nick) + " had no log(s) for some reason")

    for line in debuglines:
        osd(bot, botcom.channel_current, 'say', line)
