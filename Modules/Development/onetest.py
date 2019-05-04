#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module
from sopel.tools import stderr


# RPL_WELCOME = '001'
@sopel.module.event('001')
@sopel.module.rule('.*')
def parse_event_001(bot, trigger):
   stderr("\n" + trigger.event + "    " + str(trigger.args) + "\n")


@sopel.module.commands('onetest')
def mainfunction(bot, trigger):

    bot.say("Simulating 001 RPL_Welcome")

    bot.say('001 Foo :Hello', bot.nick)
