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
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from BotShared import *






@sopel.module.commands('feedtest')
def mainfunction(bot, trigger):

    botcom = bot_module_prerun(bot, trigger)
    if not botcom.modulerun:
        return

    if not botcom.multiruns:
        execute_main(bot, trigger, botcom)
    else:
        # IF "&&" is in the full input, it is treated as multiple commands, and is split
        commands_array = spicemanip.main(botcom.triggerargsarray, "split_&&")
        if commands_array == []:
            commands_array = [[]]
        for command_split_partial in commands_array:
            botcom.triggerargsarray = spicemanip.main(command_split_partial, 'create')
            execute_main(bot, trigger, botcom)

    botdict_save(bot)


def execute_main(bot, trigger, botcom):
    bot.say("DBB Testing")

    # for feed in bot.memory["botdict"]["tempvals"]['feeds'].keys():

    #    url = bot.memory["botdict"]["tempvals"]['feeds'][feed]["url"]

    d = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UCXuqSBlHAE6Xw-yeJA0Tunw')
    # bot.say(str(d.entries[0].published))

    # bot.say(str(d['feed']['title']))
    # bot.say(str(d['feed']['link']))
    # bot.say(str(d['feed']['subtitle']))
    # bot.say(str(len(d['entries'])))
    # bot.say(str(d['entries'][0]['title']))
    # bot.say(str(d['entries'][0]['link']))
    # for post in d['entries']:
    #    bot.say(str(post.title + ": " + post.link))
