#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import datetime
import os
import sys
moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from BotShared import *


@module.interval(1)
def timed_logcheck(bot):
    if "timed_logcheck" not in bot.memory:
        bot.memory["timed_logcheck"] = 1

        searchphrasefound = 0
        for line in os.popen("sudo service " + bot.nick + " status").read().split('\n'):
            if not searchphrasefound and "modules failed to load" in str(line) and "0 modules failed to load" not in str(line):
                searchphrasefound = str(line).split("]:", -1)[1]

        if searchphrasefound:
            for channel in bot.channels:
                osd(bot, channel, 'say', "Notice to Bot Admins: " + str(searchphrasefound) + ". Run the debug command for more information.")
