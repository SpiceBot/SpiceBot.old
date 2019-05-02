#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module


# imports for system and OS access, directories
import os
import sys

import json
import requests
from operator import itemgetter

# imports based on THIS file
# moduledir = os.path.dirname(__file__)
# shareddir = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(shareddir)
# from BotShared import *

comdict = {
            "author": "deathbybandaid",
            "contributors": [],
            "description": "",
            'privs': [],
            "example": "",
            "exampleresponse": "",
            }

# from pip._internal.utils.misc import get_installed_distributions

# from inspect import getmembers, isfunction


@sopel.module.commands('dbbtest2')
def mainfunction(bot, trigger):

    bot.say("dbb test module2")

    bot.say(str(bot.deathbybandaid))
