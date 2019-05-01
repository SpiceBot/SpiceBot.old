#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module
from sopel.tools import stderr, Identifier
from sopel.db import _deserialize


def setup(bot):

    bot.memory['Sopel_DatabaseCache'] = dict()

    # Inject OSD
    stderr("[Sopel_DatabaseCache] Implanting Database functions into bot.")
    bot.db.reset_nick_value = SopelDBCache.reset_nick_value


class SopelDBCache:

    def reset_nick_value(self, nick, key):
        """Resets the value for a given key to be associated with the nick."""
        nick = Identifier(nick)
        nick_id = self.get_nick_id(nick)
        self.execute('DELETE FROM nick_values WHERE (?, ?)', [nick_id, key])


@sopel.module.commands('dbreset')
def mainfunction(bot, trigger):

    testval = 1
    bot.say("value is " + str(bot.db.get_nick_value('nick', 'key')))

    bot.say("setting value to " + str(testval))
    bot.db.set_nick_value('nick', 'key', testval)

    bot.say("value is " + str(bot.db.get_nick_value('nick', 'key')))

    bot.say("resetting value")
    bot.db.reset_nick_value('nick', 'key')

    bot.say("value is " + str(bot.db.get_nick_value('nick', 'key')))
