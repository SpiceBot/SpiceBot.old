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






@module.event('001')
@module.rule('.*')
@module.thread(True)
def auto_feeds(bot, trigger):

    # don't run jobs if not ready
    while not bot_startup_requirements_met(bot, ["botdict", "monologue", "feeds"]):
        pass

    for feed in bot.memory["botdict"]["tempvals"]['feeds'].keys():
        Thread(target=feeds_thread, args=(bot, feed,)).start()


def feeds_thread(bot, feed):
    while True:
        time.sleep(57)
        dispmsg = bot_dictcom_feeds_handler(bot, feed, False)
        if dispmsg != []:

            for channel in bot.channels.keys():
                feeds_enabled = get_channel_value(bot, channel, "long", "feeds", "enabled") or []
                if feed in feeds_enabled:
                    osd(bot, str(channel), 'say', dispmsg)

            for user in bot.memory["botdict"]["tempvals"]["servers_list"][str(bot.memory["botdict"]["tempvals"]['server'])]['all_current_users']:
                feed_enabled = get_nick_value(bot, user, "long", "feeds", "enabled") or []
                if feed in feed_enabled:
                    osd(bot, user, 'notice', dispmsg)
